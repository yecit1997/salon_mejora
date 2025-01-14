from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from .citaForm import citaForm



# Pedir una cita
def crear_cita(request):
    if request.method == 'POST':
        form = citaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-citas')
    else:
        form = citaForm()
        
    context = {
        'form': form
        }
        
    return render(request, 'citas/pedir_cita.html', context=context)




# Listamos las citas que tenemos en el sistema
def listar_citas(request):
    citas = Cita.objects.all()
    
    context = {
        'citas': citas
    }
    
    return render(request, 'citas/listar_cita.html', context=context)


