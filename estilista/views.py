from django.shortcuts import render, redirect
from .estilistaForm import EstilistaForm
from .models import Estilista

# Create your views here.

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


def lista_estilistas(request):
    estilistas = Estilista.objects.all()
    context = {
        'estilistas':estilistas
    }
    return render(request, 'estilistas/lista_estilista.html', context=context)







