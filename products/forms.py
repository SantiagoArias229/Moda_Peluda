from django import forms
from . import models

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','description','product_image','price','category','quantity']