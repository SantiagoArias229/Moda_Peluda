#Hecho por: Vanessa Velez Restrepo
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator




class Product(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True , default="product_image/aaaa.jpg")
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    category = models.CharField(max_length = 70)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    def __str__(self):
        return str(self.name)
    
class Collar(models.Model):
    
    MATERIAL_OPTIONS = [
        ('Algodón', _('Algodón')),
        ('Poliéster', _('Poliéster')),
        ('Cuero', _('Cuero')),
        ('Metálico', _('Metálico')),
    ]
    
    COLOR_OPTIONS = [
        ('Negro', _('Negro')),
        ('Blanco', _('Blanco')),
        ('Rojo', _('Rojo')),
        ('Azul', _('Azul')),
        ('Verde', _('Verde')),
        ('Rosado', _('Rosado')),
        ('Morado', _('Morado')),
    ]
    
    SIZE_OPTIONS = [
        ('Pequeño', _('Pequeño')),
        ('Mediano', _('Mediano')),
        ('Grande', _('Grande')),
    ]
    
    TEXT_COLOR_OPTIONS = [
        ('Negro', _('Negro')),
        ('Rojo', _('Rojo')),
        ('Azul', _('Azul')),
        ('Verde', _('Verde')),
        ('Rosado', _('Rosado')),
        ('Morado', _('Morado')),
    ]
    
    FONT_TYPE_OPTIONS = [
        ('Impact', _('Impact')),
        ('Verdana', _('Verdana')),
        ('Comic Sans MS', _('Comic Sans MS')),
    ]
    
    material = models.CharField(max_length=30, choices=MATERIAL_OPTIONS)
    color = models.CharField(max_length=30, choices=COLOR_OPTIONS)
    size = models.CharField(max_length=30, choices=SIZE_OPTIONS)
    
    text_color = models.CharField(max_length=30, choices=TEXT_COLOR_OPTIONS, null=True)
    font_type = models.CharField(max_length=30, choices=FONT_TYPE_OPTIONS, null=True)
    design = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)