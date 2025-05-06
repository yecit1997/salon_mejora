from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from cita.models import Cita

def citas_por_mes(request):
    todas_las_citas = Cita.objects.all()
    citas_por_mes = {}
    
    for cita in todas_las_citas:
        fecha = cita.fecha
        mes = fecha.strftime('%B')  # Obtener el nombre del mes en español
        anio = fecha.year
        print(mes, anio)
        if mes not in citas_por_mes:
            citas_por_mes[mes] = {}
    return render(request, 'balance/citas_por_mes.html')