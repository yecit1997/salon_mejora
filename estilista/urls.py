from django.urls import path
from estilista import views

urlpatterns = [
    path('crear-estilista', views.crear_estilista, name='crear-estilista'),
    path('lista-estilistas', views.lista_estilistas, name='lista-estilistas'),
    path('editar-estilista/<str:dni>', views.editar_estilista, name='editar-estilista'),
    path('ver-estilista/<str:dni>', views.ver_estilista, name='ver-estilista'),
    path('eliminar-estilista/<str:dni>', views.eliminar_estilista, name='eliminar-estilista'),
]
