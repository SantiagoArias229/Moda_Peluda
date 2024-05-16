from django.shortcuts import render
from . import models
from products.models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from urllib.parse import quote, unquote

#Este codigo fue hecho por Luis Miguel Giraldo Gonzalez

def add_to_cart_view(request, pk):
    quantity = request.GET.get('quantity', 1)
    product = Product.objects.get(id=pk)
    product_cookie_value = f"{pk}:{quantity}"
    if 'product_ids' in request.COOKIES:
        product_ids = unquote(request.COOKIES['product_ids'])
        product_list = product_ids.split('|')
        updated_product_list = []
        product_found = False
        for item in product_list:
            if ':' in item:
                product_id, existing_quantity = item.split(':')
                if product_id == str(pk):
                    item = f"{pk}:{quantity}"
                    product_found = True
            updated_product_list.append(item)
        
        if not product_found:
            updated_product_list.append(product_cookie_value)
        
        new_product_ids = '|'.join(updated_product_list)
    else:
        new_product_ids = product_cookie_value

    encoded_product_ids = quote(new_product_ids)
    response = render(request, 'cart/cart_success.html', {'quantity': quantity})
    response.set_cookie('product_ids', encoded_product_ids)

    print(request.COOKIES)
    return response

def cart_view(request):
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

    return render(request, 'cart/cart.html', {
        'products_with_quantities': products_with_quantities,
        'total': total,
        'product_count_in_cart': product_count_in_cart
    })

    
def remove_from_cart_view(request, pk):
    new_product_ids = []

    if 'product_ids' in request.COOKIES:
        product_ids = unquote(request.COOKIES['product_ids'])
        product_id_list = product_ids.split('|')
        

        for item in product_id_list:
            product_id, quantity = item.split(':')
            if int(product_id) != pk: 
                new_product_ids.append(f"{product_id}:{quantity}")
                

        new_product_ids_string = "|".join(new_product_ids)

        
        response = redirect('cart')  
        if new_product_ids_string:
            response.set_cookie('product_ids', quote(new_product_ids_string))  
        else:
            response.delete_cookie('product_ids')  

        return response
    else:
        return redirect('cart')

def buy_now_view(request, pk):
    quantity = request.GET.get('quantity', 1)
    product = Product.objects.get(id=pk)
    product_cookie_value = f"{pk}:{quantity}"
    if 'product_ids' in request.COOKIES:
        product_ids = unquote(request.COOKIES['product_ids'])
        product_list = product_ids.split('|')
        updated_product_list = []
        product_found = False
        for item in product_list:
            if ':' in item:
                product_id, existing_quantity = item.split(':')
                if product_id == str(pk):
                    item = f"{pk}:{quantity}"
                    product_found = True
            updated_product_list.append(item)
        
        if not product_found:
            updated_product_list.append(product_cookie_value)
        
        new_product_ids = '|'.join(updated_product_list)
    else:
        new_product_ids = product_cookie_value

    encoded_product_ids = quote(new_product_ids)
    response = redirect('cart')
    response.set_cookie('product_ids', encoded_product_ids)

    return response
