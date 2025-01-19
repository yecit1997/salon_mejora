from .models import Cliente


def rol_cliente(request):
    rol = None
    if request.user.is_authenticated:
        try:
            estilista = Cliente.objects.get(user=request.user)
            rol = estilista.rol
        except Cliente.DoesNotExist:
            rol = 'estilista'  # Suponiendo que los clientes no tienen un rol asignado en el modelo Estilista
    return {'rol': rol}
