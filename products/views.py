from django.shortcuts import render
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    products=models.Product.objects.all()
    return render(request,'customer_home.html',{'products':products})

##----------------------CUIDADO NO OLVIAR!!!!!!!!!!!!!!!!---------------------------------
##CUANDO CREE EL LOGIN DE ADMIN SE HABILITA ESTA FUNCION @login_required(login_url='adminlogin')
@login_required
def crate_product_view(request):
    productForm=forms.ProductForm()
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
        return HttpResponseRedirect('..')
    return render(request,'products/createProduct.html',{'productForm':productForm})

##----------------------CUIDADO NO OLVIAR!!!!!!!!!!!!!!!!---------------------------------
@login_required
def delete_product_view(request,pk):
    product=models.Product.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect('..')

##----------------------CUIDADO NO OLVIAR!!!!!!!!!!!!!!!!---------------------------------
@login_required
def update_product_view(request,pk):
    product=models.Product.objects.get(id=pk)
    productForm=forms.ProductForm(instance=product)
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST,request.FILES,instance=product)
        if productForm.is_valid():
            productForm.save()
            return HttpResponseRedirect('..')
    return render(request,'products/updateProduct.html',{'productForm':productForm})
