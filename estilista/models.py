from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Estilista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=10, unique=True, primary_key=True)
    telefono = models.CharField(max_length=20, unique=True)
    rol = models.CharField(max_length=30, default='estilista')  # Nota el uso de 'related_name'
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "estilista"
        verbose_name_plural = "estilistas"
        ordering = ["-fecha_creacion"]
        
        
    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"
