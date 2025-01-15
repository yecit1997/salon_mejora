from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Cliente
from .clienteForm import CombinedUserClienteForm


# Crear  liente
# def registro_cliente(request):
#     if request.method == 'POST':
#         form = CombinedUserClienteForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#                 email=form.cleaned_data['email'],
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name']
#             )
#             cliente = Cliente.objects.create(
#                 user=user,
#                 dni=form.cleaned_data['dni'],
#                 telefono=form.cleaned_data['telefono']
#             )
#             login(request, user)
#             return redirect('lista-estilistas')
#     else:
#         form = CombinedUserClienteForm()
    
#     context = {
#         'form': form
#     }
#     return render(request, 'clientes/registro.html', context)



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
            return redirect('lista-estilistas')
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





