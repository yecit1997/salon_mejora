from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Cliente
from .clienteForm import CombinedUserClienteForm

# Registrar clientes
def registro_cliente(request):
    if request.method == 'POST':
        form = CombinedUserClienteForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user = User.objects.create_user(
                username=user_data['username'],
                password=user_data['password'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            cliente = Cliente.objects.create(
                user=user,
                dni=user_data['dni'],
                telefono=user_data['telefono']
            )
            return redirect('inicio-seccion')
    else:
        form = CombinedUserClienteForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'clientes/registro.html', context=context)


# Listar cliente
def listar_clientes(request):
    clientes = Cliente.objects.all()
    
    context = {
        'clientes': clientes
    }
    
    return render (request, 'clientes/listar_clientes.html', context=context)


# Ver cliente
def ver_cliente(request, dni):
    cliente = get_object_or_404(Cliente, dni=dni)
    
    context = {
        'cliente': cliente
    }
    return render(request, 'clientes/ver_cliente.html', context=context)

# Editar cliente
def editar_cliente(request, dni):
    estilista = get_object_or_404(Cliente, dni=dni)
    if request.method == 'GET':
        form = CombinedUserClienteForm(instance=estilista, initial={
            'username': estilista.user.username,
            'email': estilista.user.email,
            'first_name': estilista.user.first_name,
            'last_name': estilista.user.last_name,
        })
    else:
        form = CombinedUserClienteForm(request.POST, instance=estilista)
        if form.is_valid():
            # Actualizar el usuario asociado
            user = estilista.user
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            # Guardar el estilista
            form.save()

            return redirect('listar-cliente')
    
    context = {
        'form': form
    }
    return render(request, 'clientes/editar_cliente.html', context=context)


# Eliminar cliente
def eliminar_cliente(request, dni):
    cliente = get_object_or_404(Cliente, dni=dni)
    cliente.delete()
    return redirect('listar-cliente')




