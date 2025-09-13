from django.urls import path
from apps.servicios import views

app_name = 'servicios'

urlpatterns = [
    path('', views.listar_servicios, name='lista-servicios'),
    path('crear-servicios', views.crear_servicios, name='crear-servicios'),
    path('detalle-servicios/<int:pk>', views.detelle_servicio, name='detalle-servicios'),
    path('editar-servicios/<int:pk>', views.editar_servicio, name='editar-servicios'),
    path('eliminar-servicios/<int:pk>', views.eliminar_servicio, name='eliminar-servicios'),
]