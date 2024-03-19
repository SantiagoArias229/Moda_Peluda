
from django.db import models

#Hecho por: Vanessa Velez Restrepo

class Product(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length = 70)
    quantity = models.IntegerField()
    def __str__(self):
        return str(self.name)
    
class Collar(models.Model):
    
    MATERIAL_OPTIONS = [
        ('Algodón', 'Algodón'),
        ('Poliéster', 'Poliéster'),
        ('Cuero', 'Cuero'),
        ('Metálico', 'Metálico'),
    ]
    
    COLOR_OPTIONS = [
        ('Negro', 'Negro'),
        ('Blanco', 'Blanco'),
        ('Rojo', 'Rojo'),
        ('Azul', 'Azul'),
        ('Verde', 'Verde'),
        ('Rosado', 'Rosado'),
        ('Morado', 'Morado'),
    ]
    
    SIZE_OPTIONS = [
        ('Pequeño', 'Pequeño'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    
    TEXT_COLOR_OPTIONS = [
        ('Negro', 'Negro'),
        ('Rojo', 'Rojo'),
        ('Azul', 'Azul'),
        ('Verde', 'Verde'),
        ('Rosado', 'Rosado'),
        ('Morado', 'Morado'),
    ]
    
    FONT_TYPE_OPTIONS = [
        ('Impact', 'Impact'),
        ('Verdana', 'Verdana'),
        ('Comic Sans MS', 'Comic Sans MS'),
    ]
    material = models.CharField(max_length=30, choices=MATERIAL_OPTIONS)
    color = models.CharField(max_length=30, choices=COLOR_OPTIONS)
    size = models.CharField(max_length=30, choices=SIZE_OPTIONS)
    
    text_color = models.CharField(max_length=30, choices=TEXT_COLOR_OPTIONS, null=True)
    font_type = models.CharField(max_length=30, choices=FONT_TYPE_OPTIONS, null=True)
    design = models.CharField(max_length= 100, null=True)
    def __str__(self):
        return str(self.id)