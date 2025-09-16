from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="servicios", null=False, blank=False, default='servicios/default.jpg')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-fecha_creacion"]
        

    def __str__(self):
        return f'{self.nombre} - {self.precio}'







