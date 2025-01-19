from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import Permission 
from django.contrib.contenttypes.models import ContentType



class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=10, unique=True, primary_key=True)
    telefono = models.CharField(max_length=20, unique=True)
    rol = models.CharField(max_length=30, default='cliente')  # Nota el uso de 'related_name'
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ["-fecha_creacion"]
        # permissions = (
        #     ('puede_citar', 'Puede crear citas'), # Definimos un permiso personalizado
        # )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


