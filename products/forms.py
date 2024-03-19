
from django import forms
from . import models

#Hecho por: Vanessa Velez Restrepo

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','description','product_image','price','category','quantity']
        
        
        
class CollarForm(forms.ModelForm):
    class Meta:
        model=models.Collar
        fields=['material','color','size', 'text_color', 'font_type', 'design']