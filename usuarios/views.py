from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from usuarios.loginForm import LoginForm

def inicio_seccion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            clave = form.cleaned_data['password']
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect('lista-servicios')
            else:
                return redirect('lista-servicios')
    
    context = {
        'form': LoginForm()
    }
    return render(request, 'usuarios/inicio_seccion.html', context=context)



def cerrar_seccion(request):
    '''
    Definimos el cierre de la seccion y direccionamos al usuario nuevamente a la pagina de inicio de seccion
    '''
    logout(request)
    return redirect('inicio-seccion')
