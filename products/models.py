from django.db import models

# Create your models here.
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
    
    OPCIONES_MATERIAL = [
        ('Algodón', 'Algodón'),
        ('Poliéster', 'Poliéster'),
        ('Cuero', 'Cuero'),
        ('Metálico', 'Metálico'),
    ]
    
    OPCIONES_COLOR = [
        ('Negro', 'Negro'),
        ('Blanco', 'Blanco'),
        ('Rojo', 'Rojo'),
        ('Azul', 'Azul'),
        ('Verde', 'Verde'),
        ('Rosado', 'Rosado'),
        ('Morado', 'Morado'),
    ]
    
    OPCIONES_TALLA = [
        ('Pequeño', 'Pequeño'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]
    
    material = models.CharField(max_length=30, choices=OPCIONES_MATERIAL)
    color = models.CharField(max_length=30, choices=OPCIONES_COLOR)
    talla = models.CharField(max_length=30, choices=OPCIONES_TALLA)
    
    def __str__(self):
        return self.id