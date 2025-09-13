from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Servicio
from .serviciosForm import servicioForm
from core.paginador import paginador

# Crear servicios
@permission_required('auth.is_superuser', raise_exception=True)
def crear_servicios(request):
    if request.method == 'POST':
        form = servicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios:lista-servicios')
    else:
        form = servicioForm()
    
    context = {
        'form': form
    }
    return render(request, 'servicios/crear_servicio.html', context=context)


# Listar servicios
def listar_servicios(request):
    servicios = Servicio.objects.all()
    
    servicios = paginador(servicios,request )
    context = {
        'servicios': servicios,
    }
    return render(request, 'servicios/listar_servicios.html', context=context)


# Editar servicios
@permission_required('auth.is_superuser', raise_exception=True)
def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = servicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios:lista-servicios')
    else:
        form = servicioForm(instance=servicio)
            
    context = {
        'form': form
        }
    return render(request, 'servicios/editar_servicio.html', context=context)    


# Ver detalle
def detelle_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    
    context = {
        'servicio': servicio
    }
    return render(request, 'servicios/detalle_servicio.html', context=context)


# Eliminar servidios
@permission_required('auth.is_superuser', raise_exception=True)
def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.delete()
    
    return redirect('servicios:lista-servicios')



