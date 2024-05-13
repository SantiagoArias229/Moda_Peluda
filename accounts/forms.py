# from django.contrib.auth.forms import UserCreationForm
# from .models import UserProfile
# from django import forms

# class UserCreateForm(UserCreationForm):
#     nombre=forms.TextInput()
#     correo=forms.TextInput()
#     direccion=forms.TextInput()
#     telefono=forms.IntegerField()
        
#     class Meta(UserCreationForm.Meta):
#         model = UserProfile  # Utiliza tu modelo de usuario personalizado
#         fields = UserCreationForm.Meta.fields + ('nombre','correo','direccion','telefono')
    
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args,**kwargs)

#         for fieldname in ['username', 'password1','password2','nombre','correo','direccion','telefono']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.utils.translation import gettext_lazy as _

class AuthenticationForm(BaseAuthenticationForm):
    username = forms.CharField(label=_("Nombre de usuario"))
    password = forms.CharField(widget=forms.PasswordInput, label=_("Contraseña"))
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = _('Nombre de usuario')
        self.fields['password'].label = _('Contraseña')
        
        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
    

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = _('Nombre de usuario')
        self.fields['password1'].label = _('Contraseña')
        self.fields['password2'].label = _('Contraseña (confirmación)')
        
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})