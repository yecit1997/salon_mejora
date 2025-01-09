from django.db import models

# Create your models here.
class Estilista(models.Model):
    dni = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "estilista"
        verbose_name_plural = "estilistas"
        ordering = ["-fecha_creacion"]
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"