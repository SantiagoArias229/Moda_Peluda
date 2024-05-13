from django import forms
from . import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'product_image', 'price', 'category', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'product_image': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'min': 1}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CollarForm(forms.ModelForm):
    class Meta:
        model = models.Collar
        fields = ['material', 'color', 'size', 'text_color', 'font_type', 'design']
        widgets = {
            'material': forms.Select(attrs={'class': 'form-select'}),
            'color': forms.Select(attrs={'class': 'form-select'}),
            'size': forms.Select(attrs={'class': 'form-select'}),
            'text_color': forms.Select(attrs={'class': 'form-select'}),
            'font_type': forms.Select(attrs={'class': 'form-select'}),
            'design': forms.Textarea(attrs={'class': 'form-control'}),
        }

