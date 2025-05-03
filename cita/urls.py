from django.urls import path
from cita import views

app_name = 'cita'

urlpatterns = [
    path('listar-citas/', views.listar_citas, name='listar-citas'),
    path('crear-cita/<int:id>', views.crear_cita, name='crear-cita'),
    path('editar-cita/<int:id>', views.editar_cita, name='editar-cita'),
    path('eliminar-cita/<int:id>', views.eliminar_cita, name='eliminar-cita'),
    
]