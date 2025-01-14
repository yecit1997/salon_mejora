from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from .estilistaForm import EstilistaForm
from .models import Estilista
from django.db import models



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
                telefono=form.cleaned_data['telefono']
            )
            login(request, user)
            return redirect('lista-estilistas')
    else:
        estilista_form = EstilistaForm()
    
    context = {
        'estilista_form': estilista_form
    }
    return render(request, 'estilistas/create_estilista.html', context)



# Listar estilistas
def lista_estilistas(request):
    estilistas = Estilista.objects.all()
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
    estilista: str = get_object_or_404(Estilista, dni=dni)
    if request.method == 'GET':
        estilista_form = EstilistaForm(instance=estilista)
    else:
        estilista_form = EstilistaForm(request.POST, instance=estilista)
        if estilista_form.is_valid():
            estilista_form.save()
        return redirect('lista-estilistas')
    
    context = {
        'estilista_form':estilista_form
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
def eliminar_estilista(request, dni):
    estilista = get_object_or_404(Estilista, dni=dni)
    estilista.delete()
    return redirect('lista-estilistas')












