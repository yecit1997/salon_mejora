from django.urls import path
from apps.usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('inicio-seccion', views.inicio_seccion, name='inicio-seccion'),
    path('cerrar-seccion', views.cerrar_seccion, name='cerrar-seccion'),
]