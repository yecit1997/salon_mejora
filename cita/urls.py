from django.urls import path
from cita import views



urlpatterns = [
    path('crear-cita/<int:id>', views.crear_cita, name='crear-cita'),
    path('editar-cita/<int:id>', views.editar_cita, name='editar-cita'),
    path('listar-citas/', views.listar_citas, name='listar-citas'),
    
]