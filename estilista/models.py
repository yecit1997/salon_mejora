from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group



# Create your models here.
class Estilista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=10, unique=True, primary_key=True)
    telefono = models.CharField(max_length=20, unique=True)
    rol = models.CharField(max_length=30, default='estilistas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "estilista"
        verbose_name_plural = "estilistas"
        ordering = ["-fecha_creacion"]
        
        
    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.user and self.rol == "estilistas":
            grupo_estilista = Group.objects.get(name="estilistas")
            grupo_estilista.user_set.add(self.user)