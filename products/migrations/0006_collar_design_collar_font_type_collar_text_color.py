# Generated by Django 4.1.2 on 2024-03-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_talla_collar_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='collar',
            name='design',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='collar',
            name='font_type',
            field=models.CharField(choices=[('Impact', 'Impact'), ('Verdana', 'Verdana'), ('Comic Sans MS', 'Comic Sans MS')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='collar',
            name='text_color',
            field=models.CharField(choices=[('Negro', 'Negro'), ('Rojo', 'Rojo'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Rosado', 'Rosado'), ('Morado', 'Morado')], max_length=30, null=True),
        ),
    ]
