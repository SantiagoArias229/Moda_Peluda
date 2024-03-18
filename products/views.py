from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from . import forms,models



def home_view(request):
    products=models.Product.objects.all()
    return render(request,'customer_home.html',{'products':products})


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
        # Al cargar la página, inicializa el formulario con los datos actuales del producto
        product_form = forms.ProductForm(instance=product)
    return render(request,'products/update_product.html',{'productForm':product_form})


def product_detail_view(request, pk):
    collar = models.Collar.objects.all()
    try:
        product = models.Product.objects.get(id=pk)
    except models.Product.DoesNotExist:
        # Manejo de error si el producto no existe
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

    products = None  # Inicializa como None
    
    if category and category.strip():  # Verifica si query no está vacío ni solo contiene espacios en blanco
        if category:
            products = models.Product.objects.filter(category__icontains=category)
        else:
            products = models.Product.objects.filter(name__icontains=query)

    return render(request, 'products/search_results.html', {'products': products, 'query': query})