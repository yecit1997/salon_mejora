from django.apps import AppConfig


class ServiciosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.servicios'

    def ready(self):
        import apps.servicios.signals