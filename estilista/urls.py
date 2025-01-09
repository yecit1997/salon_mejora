from django.urls import path
from estilista import views

urlpatterns = [
    path('crear-estilista', views.crear_estilista, name='crear-estilista'),
    path('lista-estilistas', views.lista_estilistas, name='lista-estilistas'),
]
