from django.urls import path
from servicios import views



urlpatterns = [
    path('crear-servicios', views.crear_servicios, name='crear-servicios'),
    path('lista-servicios', views.listar_servicios, name='lista-servicios'),
]