from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from cliente.models import Cliente
from servicios.models import Servicio
from .models import Cita
from .citaForm import citaForm



# Pedir una cita
@permission_required(['cliente.puede_citar_cliente'],login_url='inicio-seccion', raise_exception=True)
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
            
            # Enviar correo al cliete con los datos de la cita
            destinatarios = [cliente.user.email, cita.estilista.user.email]
            asunto = "Nueva Cita Programada" 
            mensaje = f"""Se ha generado una nueva cita. 
            Servicio: {cita.servicio.nombre} 
            Cliente: {cliente.user.get_full_name()} 
            Estilista: {cita.estilista.user.get_full_name()} 
            Fecha: {cita.fecha} Hora: {cita.hora} """ 
            send_mail(asunto, mensaje, 'tusitioweb@correo.com', destinatarios)
            return redirect('lista-servicios')
    else:
        form = citaForm()
        
    context = {
        'form': form,
        'servicio':servicio,
        'cliente':cliente
        }
    
    return render(request, 'citas/pedir_cita.html', context=context)
    

# Listamos las citas que tenemos en el sistema
@permission_required('Estilista.puede_ver_listas', login_url='inicio-seccion', raise_exception=True)
def listar_citas(request):
    citas = Cita.objects.all()
    
    context = {
        'citas': citas
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
    return redirect('listar-citas')