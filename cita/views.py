from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import  permission_required
from django.contrib import messages
from core.paginador import paginador
from cliente.models import Cliente
from servicios.models import Servicio
from .models import Cita
from .citaForm import citaForm
from cita.correo_creacion_cita import enviar_correo




# Pedir una cita
@permission_required(['cliente.puede_citar_cliente'],login_url='inicio-seccion', raise_exception=True)
def crear_cita(request, id):
    try:
        servicio = get_object_or_404(Servicio, id=id) # Obtenemos el servicio que se ha seleccionado
        cliente = get_object_or_404(Cliente, user=request.user) # Obtenemos el cliente que está logueado
        if request.method == 'POST':
            form = citaForm(request.POST)
            if form.is_valid():
                cita = form.save(commit=False) # Guardamos el formulario sin enviarlo a la base de datos
                cita.servicio = servicio
                cita.cliente = cliente
                cita.save() # Guardamos la cita en la base de datos
                
                # Enviar correo al cliete con los datos de la cita
                enviar_correo(cliente, cita)
                messages.success(request,'Cita creada con exito 😊')
                
                return redirect('lista-servicios')
        else:
            form = citaForm()
            
        context = {
            'form': form,
            'servicio':servicio,
            'cliente':cliente
            }
        
        return render(request, 'citas/pedir_cita.html', context=context)
    except:
      return render(request, 'core/pedir_sin_permisos.html')
    

# Listamos las citas que tenemos en el sistema
@permission_required('cita.view_cita', login_url='inicio-seccion', raise_exception=True)
def listar_citas(request):
    citas = Cita.objects.all()
    citas = paginador(citas,request)
    context = {
        'citas': citas,
    }
    
    return render(request, 'citas/listar_cita.html', context=context)


# Editar una cita // Solo para el administrador y clientes
@permission_required(['cliente.puede_citar_cliente', 'Estilista.puede_ver_listas', 'auth.is_superuser'],login_url='inicio-seccion', raise_exception=True)
def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    servicio = get_object_or_404(Servicio, id=id) # Obtenemos el servicio que se ha seleccionado

    if request.method == 'POST':
        form = citaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cita fue modificada con exito 😊')
            return redirect('listar-citas')
    else:
        form = citaForm(instance=cita)
        
    context = {
        'form': form,
        'servicio':servicio
    }
    
    return render(request, 'citas/editar_cita.html', context=context)


# Eliminar Citas // Solo para el administrador y clientes
@permission_required(['cliente.puede_citar_cliente', 'auth.is_superuser'],login_url='inicio-seccion', raise_exception=True)
def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    messages.warning(request, 'La cita fue eliminada con exito ❌')
    return redirect('listar-citas')