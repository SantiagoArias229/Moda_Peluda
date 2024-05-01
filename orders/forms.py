from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'payment_type', 'address', 'email']
        labels = {
            'customer_name': _('Nombre del cliente'),
            'payment_type': _('Tipo de pago'),
            'address': _('Dirección'),
            'email': _('Correo electronico'),
        }
