from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Product, Collar

class ProductTestCase(TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas, como crear instancias de modelos.
        Product.objects.create(name="Pelota",
            description="Pelota cubierta de tocineta",
            price=1500,
            category="Juguete",
            quantity=10
        )

    def test_product_creation(self):
        # Recuperar la instancia creada en setUp
        laptop = Product.objects.get(name="Pelota")
        
        # Verificar que los campos sean los correctos
        self.assertEqual(laptop.description, "Pelota cubierta de tocineta")
        self.assertEqual(laptop.price, 1500)
        self.assertEqual(laptop.category, "Juguete")
        self.assertEqual(laptop.quantity, 10)

    def test_string_representation(self):
        # Prueba el método __str__ del modelo
        laptop = Product.objects.get(name="Pelota")
        self.assertEqual(str(laptop), "Pelota")
        
        
        
        
class CollarModelTest(TestCase):
    def setUp(self):
        # Crear una instancia de Collar
        Collar.objects.create(
            material='Cuero',
            color='Negro',
            size='Mediano',
            text_color='Rojo',
            font_type='Verdana',
            design='Collar resistente con nombre bordado'
        )

    def test_design_in_spanish(self):
        # Recuperar la instancia creada en setUp
        collar = Collar.objects.get(design='Collar resistente con nombre bordado')
        
        # Verificar que el campo 'design' maneje correctamente el español
        self.assertEqual(collar.design, 'Collar resistente con nombre bordado')

    def test_model_options(self):
        # Verificar que las opciones de los campos estén correctamente configuradas
        collar = Collar.objects.get(design='Collar resistente con nombre bordado')
        self.assertIn(collar.material, [choice[0] for choice in Collar.MATERIAL_OPTIONS])
        self.assertIn(collar.color, [choice[0] for choice in Collar.COLOR_OPTIONS])
        self.assertIn(collar.size, [choice[0] for choice in Collar.SIZE_OPTIONS])
        self.assertIn(collar.text_color, [choice[0] for choice in Collar.TEXT_COLOR_OPTIONS])
        self.assertIn(collar.font_type, [choice[0] for choice in Collar.FONT_TYPE_OPTIONS])