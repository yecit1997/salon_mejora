from django.shortcuts import render, redirect, get_object_or_404
from .estilistaForm import EstilistaForm
from .models import Estilista
from django.db import models


# Crear estilista
def crear_estilista(request):
    if request.method == 'POST':
        estilista_form = EstilistaForm(request.POST)
        if estilista_form.is_valid():
            estilista_form.save()
            return redirect('lista-estilistas')
    else:
        estilista_form = EstilistaForm()
        
    context = {
        'estilista_form':estilista_form
    }
    return render(request, 'estilistas/create_estilista.html', context=context) 

# Listar estilistas
def lista_estilistas(request):
    estilistas = Estilista.objects.all()
    status = request.GET.get('status', 'all')
    if status == 'active':
        estilistas = estilistas.filter(deshabilitado=False)
    elif status == 'disabled':
        estilistas = estilistas.filter(deshabilitado=True)
    query = request.GET.get('q')
    if query:
        estilistas = Estilista.objects.filter(
            models.Q(dni__icontains=query) |
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(telefono__icontains=query) |
            models.Q(email__icontains=query)
        )

    # estilistas = Estilista.objects.filter(deshabilitado=False)
    context = {
        'estilistas':estilistas,
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












