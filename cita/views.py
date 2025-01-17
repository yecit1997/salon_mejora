from django.shortcuts import render, redirect, get_object_or_404

from cliente.models import Cliente
from servicios.models import Servicio
from .models import Cita
from .citaForm import citaForm



# Pedir una cita
def crear_cita(request, id):
    servicio = get_object_or_404(Servicio, id=id) # Obtenemos el servicio que se ha seleccionado
    cliente = get_object_or_404(Cliente, user=request.user) # Obtenemos el cliente que está logueado
    if request.method == 'POST':
        form = citaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False) # Guardamos el formulario sin enviarlo a la base de datos
            cita.servicio = servicio
            cita.cliente = cliente
            cita.save() # Guardamos la cita en la base de datos
            return redirect('listar-citas')
    else:
        form = citaForm()
        
    context = {
        'form': form,
        'servicio':servicio
        # 'cliente':cliente
        }
    
    return render(request, 'citas/pedir_cita.html', context=context)
    


# Listamos las citas que tenemos en el sistema
def listar_citas(request):
    citas = Cita.objects.all()
    
    context = {
        'citas': citas
        
    }
    
    return render(request, 'citas/listar_cita.html', context=context)


# Editar una cita
def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        form = citaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listar-citas')
    else:
        form = citaForm(instance=cita)
        
    context = {
        'form': form
    }
    
    return render(request, 'citas/editar_cita.html', context=context)


