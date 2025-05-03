from django.db import models
from estilista.models import Estilista
from cliente.models import Cliente
from servicios.models import Servicio

class Cita(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    estilista = models.ForeignKey(Estilista, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "cita"
        verbose_name_plural = "citas"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f'{self.servicio.nombre} - {self.estilista.user.first_name} - {self.fecha} - {self.hora} - {self.cliente.user.first_name} {self.cliente.user.last_name}'
    
    
    
    
    
    
