from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'payment_type', 'address', 'email']
        labels = {
            'customer_name': 'Nombre del Cliente',
            'payment_type': 'Tipo de Pago',
            'address': 'Dirección',
            'email': 'Correo Electrónico',
        }
