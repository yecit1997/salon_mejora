from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cliente'
    verbose_name = _('clientes')
    
    def ready(self):
        import cliente.signals


