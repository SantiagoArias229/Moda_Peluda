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
        return self.name