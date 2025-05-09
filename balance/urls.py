from django.urls import path
from balance import views

app_name = 'balance'

urlpatterns = [
    path('citas-mes/', views.citas_por_mes, name='citas-mes'),
    path('balance-home/', views.balance_home, name='balance-home'),
]