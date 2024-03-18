from django.db import models

class Order(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('COD', 'Contraentrega'),
        ('CC', 'Tarjeta de Crédito'),
        ('EFTY', 'Efecty'),
    ]

    # Este campo es el ID de la orden, Django lo genera automáticamente como una clave primaria.
    customer_name = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    payment_type = models.CharField(max_length=4, choices=PAYMENT_TYPE_CHOICES, verbose_name="Tipo de Pago")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    email = models.EmailField(verbose_name="Correo Electrónico")
    products = models.ManyToManyField('products.Product', verbose_name="Productos en el Carrito")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la Orden") 

    def __str__(self):
        return f"Orden {self.id} - {self.customer_name}"


    def __str__(self):
        return self.name