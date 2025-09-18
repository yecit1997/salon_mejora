from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import  permission_required
from django.contrib import messages
from core.paginador import paginador
from apps.cliente.models import Cliente
from apps.servicios.models import Servicio
from .models import Cita
from .citaForm import citaForm
from apps.cita.correo_creacion_cita import enviar_correo


# Pedir una cita
# @permission_required(['cliente.puede_citar_cliente', 'auth.is_superuser'],login_url='inicio-seccion', raise_exception=True)
def crear_cita(request, id):
    try:
        servicio = get_object_or_404(Servicio, id=id)
        if request.method == 'POST':
            form = citaForm(request.POST, user=request.user) # Pasa el usuario al formulario
            if form.is_valid():
                cita = form.save(commit=False)
                cita.servicio = servicio

                # Lógica para determinar el cliente
                if request.user.is_superuser:
                    # Si es administrador, usa el cliente seleccionado del formulario
                    cita.cliente = form.cleaned_data['cliente']
                else:
                    # Si es un cliente normal, usa el cliente logueado
                    cita.cliente = get_object_or_404(Cliente, user=request.user)
                cita.creado_por = request.user

                cita.save()
                enviar_correo(cita.cliente, cita)
                messages.success(request, 'Cita creada con éxito 😊')
                return redirect('servicios:lista-servicios')
        else:
            form = citaForm(user=request.user)

        context = {
            'form': form,
            'servicio': servicio,
            'cliente': None # El cliente es dinámico, por lo que puede ser None
        }
        return render(request, 'citas/pedir_cita.html', context=context)
    except Exception as e:
        messages.error(request, f'Ocurrió un error: {e}')
        return render(request, 'core/sin_permisos.html')
    

# Listamos las citas que tenemos en el sistema
@permission_required(['cita.view_cita', 'Estilista.puede_ver_listas', 'auth.is_superuser'], login_url='inicio-seccion', raise_exception=True)
def listar_citas(request):
    try:
        citas = Cita.objects.all()
        citas = paginador(citas,request)
        context = {
            'citas': citas,
            # 'creado_por': creado_por,
        }
        
        return render(request, 'citas/listar_cita.html', context=context)
    except:
        return render(request, 'core/sin_permisos.html')


# Editar una cita // Solo para el administrador y clientes
@permission_required(['cliente.puede_citar_cliente', 'Estilista.puede_ver_listas', 'auth.is_superuser'],login_url='inicio-seccion', raise_exception=True)
def editar_cita(request, id):
    try:
        # Verificamos si el usuario tiene permisos para editar la cita
        if not request.user.has_perm('cita.change_cita') and not request.user.has_perm('cliente.puede_citar_cliente'):
            return render(request, 'core/sin_permisos.html')
        cita = get_object_or_404(Cita, id=id)
        servicio = get_object_or_404(Servicio, id=id) # Obtenemos el servicio que se ha seleccionado

        if request.method == 'POST':
            form = citaForm(request.POST, instance=cita)
            if form.is_valid():
                form.save()
                messages.success(request, 'La cita fue modificada con exito 😊')
                return redirect('cita:listar-citas')
        else:
            form = citaForm(instance=cita)
            
        context = {
            'form': form,
            'servicio':servicio
        }
        
        return render(request, 'citas/editar_cita.html', context=context, status=200)
    except Exception as e:
        return render(request, 'core/sin_permisos.html', context={'Error': e}, status=403)


# Eliminar Citas // Solo para el administrador y clientes
@permission_required(['cliente.puede_citar_cliente', 'auth.is_superuser'],login_url='inicio-seccion', raise_exception=False)
def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    messages.warning(request, 'La cita fue eliminada con exito ❌')
    return redirect('cita:listar-citas')




