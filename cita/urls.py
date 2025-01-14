from django.urls import path
from cita import views



urlpatterns = [
    path('crear-cita/', views.crear_cita, name='crear-cita'),
    path('listar-citas/', views.listar_citas, name='listar-citas'),
    
]