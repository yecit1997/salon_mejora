from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Servicio

@receiver(post_delete, sender=Servicio)
def borrar_imagen_servicio(sender, instance, **kwargs):
    """
    Borra el archivo de la imagen cuando el objeto Servicio es eliminado.
    """
    # Verifica si hay una imagen asociada al objeto
    if instance.imagen:
        instance.imagen.delete(save=False)