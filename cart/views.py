from django.shortcuts import render
from . import models
from products.models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from urllib.parse import quote, unquote


def add_to_cart_view(request, pk):
    
    quantity = request.GET.get('quantity', 1)
    product = Product.objects.get(id=pk)

    # Crear o actualizar la cookie de 'product_ids'
    product_cookie_value = f"{pk}:{quantity}"
    if 'product_ids' in request.COOKIES:
        product_ids = unquote(request.COOKIES['product_ids'])
        product_list = product_ids.split('|')
        
        # Inicializar la lista actualizada como vacía
        updated_product_list = []
        
        # Verificar si el producto ya está en el carrito y actualizar la cantidad
        product_found = False
        for item in product_list:
            # Verificar si el item contiene el delimitador esperado ':'
            if ':' in item:
                product_id, existing_quantity = item.split(':')
                if product_id == str(pk):
                    # Actualizar cantidad si el producto ya existe
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


    
# def cart_view(request):
#     # Inicializar las variables
#     products = None
#     total = 0
#     product_count_in_cart = 0

#     # Obtener los IDs de los productos del carrito desde las cookies
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids'].split('|')
#         product_count_in_cart = len(set(product_ids))

#         # Obtener los productos del carrito junto con sus cantidades
#         products = []
#         for product_id in product_ids:
#             product = Product.objects.get(id=product_id)
#             # Obtener la cantidad de este producto del parámetro 'quantity' en la URL
#             quantity = int(request.GET.get('quantity', 4))
#             # Calcular el precio total del producto (precio por cantidad)
#             total_product_price = product.price * quantity
#             total += total_product_price
#             # Agregar el producto junto con la cantidad y el precio total a la lista de productos
#             products.append({'product': product, 'quantity': quantity, 'total_product_price': total_product_price,'price':product.price})

#     return render(request, 'cart/cart.html', {'products': products, 'total': total, 'product_count_in_cart': product_count_in_cart})



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
        
        # Revisar cada entrada y reconstruir la lista sin el producto a eliminar
        for item in product_id_list:
            product_id, quantity = item.split(':')
            if int(product_id) != pk:  # Conservar solo si no es el producto a eliminar
                new_product_ids.append(f"{product_id}:{quantity}")
                
        # Rehacer la string de product_ids para la cookie
        new_product_ids_string = "|".join(new_product_ids)

        # Preparar la respuesta y actualizar/eliminar la cookie
        response = redirect('cart')  # Suponiendo que 'cart' es el nombre de la URL para la vista del carrito
        if new_product_ids_string:
            response.set_cookie('product_ids', quote(new_product_ids_string))  # Actualizar la cookie
        else:
            response.delete_cookie('product_ids')  # Borrar la cookie si no hay más productos

        return response
    else:
        # Si no hay productos, simplemente redirige al carrito o a otra página relevante
        return redirect('cart')

