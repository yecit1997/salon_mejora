from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio
from .serviciosForm import servicioForm

from django.contrib.auth.decorators import login_required, permission_required


# Crear servicios
@permission_required('auth.is_superuser', raise_exception=False)
def crear_servicios(request):
    if request.method == 'POST':
        form = servicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-servicios')
    else:
        form = servicioForm()
    
    context = {
        'form': form
    }
    return render(request, 'servicios/crear_servicio.html', context=context)


# Listar servicios
def listar_servicios(request):
    servicios = Servicio.objects.all()
    
    context = {
        'servicios': servicios
    }
    return render(request, 'servicios/listar_servicios.html', context=context)




