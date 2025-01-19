from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cliente
from django.contrib.auth.models import User

@receiver(post_migrate)
def create_permissions(sender, **kwargs):
    if sender.name == 'auth' and kwargs.get('app'):
        content_type = ContentType.objects.get_for_model(Cliente)
        puede_citar_perm = Permission.objects.create(
            codename='puede_citar_cliente',
            name='Puede crear citas',
            content_type=content_type,
        )

@receiver(post_save, sender=User)
def asignar_permisos_cliente(sender, instance, created, **kwargs):
    if created and instance.groups.filter(name='cliente').exists():
        content_type = ContentType.objects.get_for_model(Cliente)
        puede_citar_perm = Permission.objects.get(codename='puede_citar_cliente', content_type=content_type)
        instance.user_permissions.add(puede_citar_perm)




