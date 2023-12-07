from django.urls import path
from . import views
from .views import lista_productos

urlpatterns = [
    path('', views.home, name='home'),  # La vista de inicio para la ruta de acceso vacía
    path('registro/', views.registro, name='registro'),
    path('makeupArtist/', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),  # Asegúrate de que esta línea esté aquí
    path('productos/', lista_productos, name='productos'),
    #path('registro-cliente/', views.registro_cliente, name='registro_cliente'),
    #path('makeupArtist/', views.registro, name='registro'),
    #path('registro/', registro_cliente, name='registro'),
]
