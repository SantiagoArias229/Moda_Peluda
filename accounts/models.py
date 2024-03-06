from django.db import models

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega los campos adicionales que desees
    nombre = models.TextField(max_length=50, blank=True)
    correo = models.TextField(max_length=250, blank=True)
    direccion = models.TextField(max_length=350, blank=True)
    telefono=models.IntegerField(null=True)
