from django.urls import path
from cliente import views



urlpatterns = [
    path('registro-cliente/', views.registro_cliente, name='registro-cliente'),
    path('listar-cliente/', views.listar_clientes, name='listar-cliente'),
    path('editar-cliente/<str:dni>', views.editar_cliente, name='editar-cliente'),
    path('eliminar-cliente/<str:dni>', views.eliminar_cliente, name='eliminar-cliente'),
    path('ver-cliente/<str:dni>', views.ver_cliente, name='ver-cliente'),
    
]