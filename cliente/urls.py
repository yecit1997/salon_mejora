from django.urls import path
from cliente import views



urlpatterns = [
    path('registro-cliente/', views.registro_cliente, name='registro-cliente'),
    path('listar-cliente/', views.listar_clientes, name='listar-cliente'),
    
]