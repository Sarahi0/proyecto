import os
import django
from django.utils import timezone

# Establecer el entorno de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esteticaJazmine.settings')
django.setup()

# Importar los modelos
from appJazmine.models import CategoriaServicio, Servicio, Producto

# Datos para Categoría de Servicios
categorias_servicios = [
    {'nombre': 'Cortes', 'descripcion': 'Cortes de cabello unisex modernos'},
    {'nombre': 'Coloración', 'descripcion': 'Servicios de tintura y técnicas de coloración'},
    {'nombre': 'Peinados', 'descripcion': 'Estilos para eventos y ocasiones especiales'},
    {'nombre': 'Tratamientos', 'descripcion': 'Tratamientos capilares restaurativos'}
]

# Crear Categorías de Servicios
for categoria in categorias_servicios:
    CategoriaServicio.objects.get_or_create(**categoria)

# Datos para Servicios
servicios = [
    {
        'categoria_nombre': 'Cortes',  # Agregada la categoría correspondiente
        'nombre': 'Corte Clásico',
        'descripcion': 'Un corte clásico y atemporal',
        'precio': 200.00,
        'duracion': timezone.timedelta(minutes=30)
    },
    {
        'categoria_nombre': 'Cortes',  # Agregada la categoría correspondiente
        'nombre': 'Corte Moderno',
        'descripcion': 'Un corte moderno a la última moda',
        'precio': 250.00,
        'duracion': timezone.timedelta(minutes=45)
    },
    {
        'categoria_nombre': 'Coloración',  # Agregada la categoría correspondiente
        'nombre': 'Balayage',
        'descripcion': 'Técnica de coloración Balayage',
        'precio': 800.00,
        'duracion': timezone.timedelta(hours=2)
    },
    {
        'categoria_nombre': 'Tratamientos',  # Agregada la categoría correspondiente
        'nombre': 'Hidratación Profunda',
        'descripcion': 'Tratamiento para cabello seco y dañado',
        'precio': 500.00,
        'duracion': timezone.timedelta(hours=1, minutes=30)
    }
]

# Crear Servicios
for servicio_data in servicios:
    categoria_nombre = servicio_data.pop('categoria_nombre')
    categoria = CategoriaServicio.objects.get(nombre=categoria_nombre)
    duracion = servicio_data.pop('duracion')
    Servicio.objects.get_or_create(categoria=categoria, duracion=duracion, **servicio_data)

# Datos para Productos
productos = [
    {'nombre': 'Shampoo Hidratante', 'descripcion': 'Shampoo para cabello seco y maltratado', 'precio': 150.00, 'stock': 15},
    {'nombre': 'Aceite de Argán', 'descripcion': 'Aceite nutritivo para puntas abiertas', 'precio': 200.00, 'stock': 10},
    {'nombre': 'Gel Fijador', 'descripcion': 'Gel de alta fijación para estilos duraderos', 'precio': 120.00, 'stock': 20},
    {'nombre': 'Spray de Volumen', 'descripcion': 'Spray para dar volumen desde la raíz', 'precio': 180.00, 'stock': 5}
]

# Crear Productos
for producto in productos:
    Producto.objects.get_or_create(**producto)

print("La base de datos ha sido poblada con datos de ejemplo.")
