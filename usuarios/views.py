# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from usuarios.loginForm import LoginForm

# def inicio_seccion(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data['username']
#             clave = form.cleaned_data['password']
#             rol = form.cleaned_data['rol']
#             print(f'Rol: {rol}')
#             user = authenticate(username=usuario, password=clave, rol=rol)
#             if user is not None:
#                 login(request, user)
#                 return redirect('lista-estilistas')
#             else:
#                 return redirect('lista-estilistas')
    
#     context = {
#         'form': LoginForm()
#     }
#     return render(request, 'usuarios/inicio_seccion.html', context=context)

