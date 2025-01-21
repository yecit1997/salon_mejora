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


# Editar servicios
def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    
    if request.method == 'POST':
        form = servicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('lista-servicios')
        else:
            form = servicioForm(instance=servicio)
            

# Ver detalle
def detelle_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    
    context = {
        'servicio': servicio
    }
    return render(request, 'servicios/detalle_servicio.html', context=context)


# Eliminar servidios
def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.delete()
    
    return redirect('lista-servicios')



