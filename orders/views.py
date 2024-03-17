from django.shortcuts import get_object_or_404, render, redirect
from orders.models import Order
from products.models import Product
from .forms import OrderForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            product_ids = request.COOKIES.get('product_ids', '').split('|')
            if product_ids:
                products = Product.objects.filter(id__in=product_ids)
                for product in products:
                    order.products.add(product)

            return HttpResponseRedirect(reverse('order_confirmation', args=(order.id,)))
    else:
        form = OrderForm()

    return render(request, 'orders\order_form.html', {'form': form})

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    products = order.products.all()

    context = {'order': order, 'products': products}
    return render(request, 'orders\order_comfirmation.html', context)
