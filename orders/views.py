from django.shortcuts import get_object_or_404, render, redirect
from orders.models import Order
from products.models import Product
from .forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import unquote
from django.db.models.functions import TruncMonth
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import Count
from django.shortcuts import render


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            product_ids_quantities = unquote(request.COOKIES.get('product_ids', ''))
            product_ids = []
            if product_ids_quantities:
                for item in product_ids_quantities.split('|'):
                    product_id, _ = item.split(':')
                    product_ids.append(int(product_id))
            products = Product.objects.filter(id__in=product_ids)
            for product in products:
                order.products.add(product)  


            response = HttpResponseRedirect(reverse('order_confirmation', args=(order.id,)))
            #response.delete_cookie('product_ids')
            return response
    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'form': form})




def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    products = order.products.all()

    product_count_in_cart = 0
    product_quantities = {}

    if 'product_ids' in request.COOKIES:
        product_ids = unquote(request.COOKIES['product_ids'])
        if product_ids:
            for item in product_ids.split('|'):
                product_id, quantity = item.split(':')
                product_id = int(product_id)
                product_quantities[product_id] = int(quantity)

    product_count_in_cart = len(product_quantities)
    products_with_quantities = []
    total = 0

    if product_quantities:
        product_ids = list(product_quantities.keys())
        products = Product.objects.filter(id__in=product_ids)

        for p in products:
            qty = product_quantities[p.id]
            subtotal = p.price * qty
            total += subtotal
            products_with_quantities.append({'product': p, 'quantity': qty, 'subtotal': subtotal})
    

    context = {'order': order, 'products': products,'products_with_quantities': products_with_quantities,'total': total,'product_count_in_cart': product_count_in_cart}
    response = render(request, 'orders/order_comfirmation.html', context)
    response.delete_cookie('product_ids')  
    return response

def view_stadistics(request):


    orders_per_month = Order.objects.annotate(month=TruncMonth('date')).values('month').annotate(total=Count('id')).order_by('month')

    months = [order['month'].strftime("%Y-%m") for order in orders_per_month]
    totals = [order['total'] for order in orders_per_month]

    months_json = json.dumps(months, cls=DjangoJSONEncoder)
    totals_json = json.dumps(totals, cls=DjangoJSONEncoder)

    context = {
        'months': months_json,
        'totals': totals_json,
    }

    return render(request, 'orders\order_stadistics.html', context)