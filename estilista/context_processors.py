from .models import Estilista


def rol_estilista(request):
    rol = None
    if request.user.is_authenticated:
        try:
            estilista = Estilista.objects.get(user=request.user)
            rol = estilista.rol
        except Estilista.DoesNotExist:
            rol = 'cliente'  # Suponiendo que los clientes no tienen un rol asignado en el modelo Estilista
    return {'rol': rol}
