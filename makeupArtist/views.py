from django.shortcuts import render
from .models import Servicio, Producto, CategoriaServicio

def home(request):
    categorias = CategoriaServicio.objects.all()
    productos = Producto.objects.all()
    context = {
        'categorias': categorias,
        'productos': productos,
    }
    return render(request, 'makeupArtist/home.html', context)

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .forms import ClienteForm

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'makeupArtist/registro.html', {'form': form})

def servicios(request):
    # Aquí tendrías la lógica para obtener los servicios que quieres mostrar
    lista_servicios = [
        {'nombre': 'Corte de pelo unisex', 'descripcion': 'Estilos modernos y clásicos para todos.'},
        # ... otros servicios ...
    ]
    return render(request, 'makeupArtist/servicios.html', {'lista_servicios': lista_servicios})

def some_view(request):
    # Obtener todos los servicios
    servicios = Servicio.objects.all()
    # Obtener todos los productos
    productos = Producto.objects.all()
    # Y luego pasarlos al contexto de una plantilla
    return render(request, 'some_template.html', {'servicios': servicios, 'productos': productos})

def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguna_url_despues_registro')  # Redirige a donde necesites después del registro
    else:
        form = ClienteForm()

    return render(request, 'makeupArtist/registro_cliente.html', {'form': form})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})
