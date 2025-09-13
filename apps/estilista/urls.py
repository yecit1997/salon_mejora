from django.urls import path
from apps.estilista import views

app_name = 'estilista'

urlpatterns = [
    path('crear-estilista/', views.crear_estilista, name='crear-estilista'),
    path('lista-estilistas/', views.lista_estilistas, name='lista-estilistas'),
    path('editar-estilista/<str:dni>/', views.editar_estilista, name='editar-estilista'),
    path('ver-estilista/<str:dni>/', views.ver_estilista, name='ver-estilista'),
    path('eliminar-estilista/<str:dni>/', views.eliminar_estilista, name='eliminar-estilista'),
    path('cambiar-estado-estilista/<str:dni>/', views.cambiar_estado_estilista, name='cambiar-estado-estilista'),
    path('ver-mis-citas/', views.ver_mis_citas, name='ver-mis-citas'),
]