from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .estilistaForm import EstilistaForm
from core.paginador import paginador
from .models import Estilista
from apps.cita.models import Cita
from django.db import models


# Crear estilista
def crear_estilista(request):
    if request.method == 'POST':
        form = EstilistaForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            estilista = Estilista.objects.create(
                user=user,
                dni=form.cleaned_data['dni'],
                telefono=form.cleaned_data['telefono'],
                rol='estilista'
            )
            # login(request, user)
            return redirect('estilista:lista-estilistas')
    else:
        estilista_form = EstilistaForm()
    
    context = {
        'estilista_form': estilista_form
    }
    return render(request, 'estilistas/create_estilista.html', context)


# Listar estilistas
@permission_required('auth.is_superuser', raise_exception=True)
def lista_estilistas(request):
    estilistas = Estilista.objects.all()
    # Paginación
    estilistas = paginador(estilistas, request)
    status = request.GET.get('status', 'all')
    
    if status == 'active':
        estilistas = estilistas.filter(user__is_active=True)
    elif status == 'disabled':
        estilistas = estilistas.filter(user__is_active=False)
    
    query = request.GET.get('q')
    if query:
        estilistas = estilistas.filter(
            models.Q(dni__icontains=query) |
            models.Q(user__first_name__icontains=query) |
            models.Q(user__last_name__icontains=query) |
            models.Q(telefono__icontains=query) |
            models.Q(user__email__icontains=query)
        )

    context = {
        'estilistas': estilistas,
        'status': status
    }
    return render(request, 'estilistas/lista_estilista.html', context=context)


# Editar estilista
def editar_estilista(request, dni):
    
    estilista = get_object_or_404(Estilista, dni=dni)
    if request.method == 'GET':
        estilista_form = EstilistaForm(instance=estilista, initial={
            'username': estilista.user.username,
            'email': estilista.user.email,
            'first_name': estilista.user.first_name,
            'last_name': estilista.user.last_name,
        })
    else:
        estilista_form = EstilistaForm(request.POST, instance=estilista)
        if estilista_form.is_valid():
            # Actualizar el usuario asociado
            user = estilista.user
            user.username = estilista_form.cleaned_data['username']
            user.email = estilista_form.cleaned_data['email']
            user.first_name = estilista_form.cleaned_data['first_name']
            user.last_name = estilista_form.cleaned_data['last_name']
            user.save()

            # Guardar el estilista
            estilista_form.save()

            return redirect('estilista:lista-estilistas')
    
    context = {
        'estilista_form': estilista_form
    }
    return render(request, 'estilistas/editar_estilista.html', context=context)


# Visaulizar estilista
def ver_estilista(request, dni):
    estilista = get_object_or_404(Estilista, dni=dni)
    context = {
        'estilista':estilista
    }
    return render(request, 'estilistas/ver_estilista.html', context=context)


# Eliminar estilista
@permission_required('auth.is_superuser', raise_exception=True)
def eliminar_estilista(request, dni):
    estilista = get_object_or_404(Estilista, dni=dni)
    estilista.delete()
    return redirect('estilista:lista-estilistas')


# Cambiar estado estilista
@permission_required('auth.is_superuser', raise_exception=True)
def cambiar_estado_estilista(request, dni):
    estilista = get_object_or_404(Estilista, dni=dni)
    if request.method == 'POST':
        if estilista.user.is_active:
            estilista.user.is_active = False
        else:
            estilista.user.is_active = True
        estilista.user.save()
        return redirect('estilista:lista-estilistas')
    
    context = {
        'estilista': estilista
    }
    return render(request, 'estilistas/cambiar_estado_estilista.html', context=context)


def ver_mis_citas(request):
    estilista = get_object_or_404(Estilista, user=request.user)
    cita = Cita.objects.filter(estilista=estilista)
    print(cita)
    context = {
        'estilista': estilista,
        'cita': cita,
    }
    return render(request, 'estilistas/ver_mis_citas.html', context=context)





