# Generated by Django 5.0.1 on 2024-03-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_collar_design_collar_font_type_collar_text_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, verbose_name='Nombre del Cliente')),
                ('payment_type', models.CharField(choices=[('COD', 'Contraentrega'), ('CC', 'Tarjeta de Crédito'), ('EFTY', 'Efecty')], max_length=4, verbose_name='Tipo de Pago')),
                ('address', models.CharField(max_length=255, verbose_name='Dirección')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('products', models.ManyToManyField(to='products.product', verbose_name='Productos en el Carrito')),
            ],
        ),
    ]
