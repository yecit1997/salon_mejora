from django.urls import path
from usuarios import views


urlpatterns = [
    path('inicio-seccion', views.inicio_seccion, name='inicio-seccion'),
    path('cerrar-seccion', views.cerrar_seccion, name='cerrar-seccion'),
]