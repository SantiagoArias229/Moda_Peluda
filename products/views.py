
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from . import forms,models
from django.db.models import Q
from django.http import JsonResponse
from django.utils.translation import gettext as _

#Hecho por: Vanessa Velez Restrepo

def home_view(request):
    price_filter = request.GET.get('price', None)
    queries = {
        'menos10': Q(price__lt=10000),
        '10a50': Q(price__gte=10000, price__lt=50000),
        '50a80': Q(price__gte=50000, price__lt=80000),
        '80a100': Q(price__gte=80000, price__lt=100000),
        'mas100': Q(price__gte=100000),
    }
    query = queries.get(price_filter, Q())
    products = models.Product.objects.filter(query)

    return render(request, 'customer_home.html', {'products': products})


@login_required
def crate_product_view(request):
    product_form=forms.ProductForm()
    if request.method=='POST':
        product_form=forms.ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
        return HttpResponseRedirect('..')
    return render(request,'products/create_product.html',{'productForm':product_form})


@login_required
def delete_product_view(request,pk):
    product=models.Product.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect('..')


@login_required
def update_product_view(request,pk):
    product=models.Product.objects.get(id=pk)
    product_form=forms.ProductForm(instance=product)
    if request.method == 'POST':
        product_form = forms.ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect('..')
    else:
        product_form = forms.ProductForm(instance=product)
    return render(request,'products/update_product.html',{'productForm':product_form})


def product_detail_view(request, pk):
    collar = models.Collar.objects.all()
    try:
        product = models.Product.objects.get(id=pk)
    except models.Product.DoesNotExist:
        return HttpResponseNotFound("Producto no encontrado")

    return render(request, 'products/detail.html', {'product': product,'collar': collar})

def create_collar_view(request):
    product = get_object_or_404(models.Product, pk=1)
    if request.method == 'POST':
        collar_form = forms.CollarForm(request.POST, request.FILES)
        if collar_form.is_valid():
            collar_form.save()
            return redirect('..') 
    else:
        collar_form = forms.CollarForm()
    return render(request, 'products/create_collar.html', {'product': product, 'collar_form': collar_form})


def search_view(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    products = None
    if category and category.strip():
        if category:
            products = models.Product.objects.filter(category__icontains=category)
        else:
            products = models.Product.objects.filter(name__icontains=query)
    return render(request, 'products/search_results.html', {'products': products, 'query': query})


### API para obtener los collares que han creado los clientes ###
def get_personalized_collar_view(request):
    collares = models.Collar.objects.all()
    collares_json = [{
        'id': collar.id,
        'material': collar.material,
        'color': collar.color,
        'size': collar.size,
        'text_color': collar.text_color,
        'font_type': collar.font_type,
        'design': collar.design,
    } for collar in collares]
    return JsonResponse({'collares_personalizados': collares_json})