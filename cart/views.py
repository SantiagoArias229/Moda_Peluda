from django.shortcuts import render
from . import models
from products.models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.
def add_to_cart_view(request,pk):
    products=Product.objects.all()
    quantity = request.GET.get('quantity', 1)

    #for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=1
    response = render(request, 'cart/cart_success.html',{'quantity':quantity})
    #response = render(request, 'cart/cart_success.html',{'products':products,'product_count_in_cart':product_count_in_cart,'msj':'Producto añadido al carrito'})
    
    #adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    product=Product.objects.get(id=pk)
    #messages.info(request, product.name + ' added to cart successfully!')

    #return redirect("..")
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
    #for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # fetching product details from db whose id is present in cookie
    products=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=Product.objects.all().filter(id__in = product_id_in_cart)

            #for total price shown in cart
            for p in products:
                total=total+p.price
    return render(request,'cart/cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})

def remove_from_cart_view(request,pk):
    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # removing product id from cookie
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=Product.objects.all().filter(id__in = product_id_in_cart)
        #for total price shown in cart after removing product
        for p in products:
            total=total+p.price

        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = render(request, 'cart/cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        return response


