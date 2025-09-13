from django.urls import path
from apps.balance import views

app_name = 'balance'

urlpatterns = [
    path('citas-mes/', views.citas_por_mes, name='citas-mes'),
    path('citas-dia/', views.citas_por_dia, name='citas-dia'),
    path('balance-home/', views.balance_home, name='balance-home'),
]