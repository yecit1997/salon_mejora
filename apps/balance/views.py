from django.shortcuts import render
from collections import Counter

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

from apps.cita.models import Cita

def balance_home(request):
    return render(request, 'balance/balance_home.html')

def citas_por_mes(request):
    todas_las_citas = Cita.objects.all()
    nombres_meses = [cita.fecha.strftime('%b') for cita in todas_las_citas]
    nombres_dias = [cita.fecha.strftime('%d') for cita in todas_las_citas]

    conteo_meses = dict(Counter(nombres_meses))
    conteo_dias = dict(Counter(nombres_dias))
    
    total_citas = len(todas_las_citas)
    porcentaje_por_mes = {} # Inicializar el diccionario para almacenar los porcentajes
        
    # Calcular el porcentaje de citas por mes
    for mes, cantidad in conteo_meses.items():
        porcentaje_por_mes[mes] = round((cantidad / total_citas) * 100, 2)

    meses = list(porcentaje_por_mes.keys()) # Obtener los meses en el orden correcto
    porcentajes_meses = list(porcentaje_por_mes.values()) # Obtener los porcentajes en el orden correcto
    try:
        # Crear el gráfico de barras con matplotlib
        plt.figure(figsize=(8, 5))
        plt.bar(meses, porcentajes_meses, color='skyblue', width=0.5)
        plt.xlabel('Mes')
        plt.ylabel('Porcentaje (%)')
        plt.title('Porcentaje de Citas por Mes')
        plt.ylim(0, 100)  # Asegurar que el eje Y vaya de 0 a 100
        
        # plt.pie(porcentajes, labels=meses, autopct='%1.1f%%', startangle=140)
        
        # Guardar el gráfico en un buffer de memoria
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        grafico_porcentaje_meses = base64.b64encode(buffer.read()).decode('utf-8')
        plt.close()
    except:
      print('Ocurrió un error al crear el gráfico.')
      
      
    
    
    context = {
        'conteo_meses': conteo_meses,
        'conteo_dias': conteo_dias,
        'total_citas': total_citas,
        'porcentaje_por_mes': porcentaje_por_mes,
        'grafico_porcentaje_meses': f'data:image/png;base64,{grafico_porcentaje_meses}',
    }
    return render(request, 'balance/citas_por_mes.html', context)


def citas_por_dia(request):
  todas_las_citas = Cita.objects.all()
  nombres_meses = [cita.fecha.strftime('%b') for cita in todas_las_citas]
  nombres_dias = [cita.fecha.strftime('%d') for cita in todas_las_citas]

  conteo_meses = dict(Counter(nombres_meses))
  conteo_dias = dict(Counter(nombres_dias))
  total_citas = len(todas_las_citas)
  
  porcentaje_por_dia = {} # Inicializar el diccionario para almacenar los porcentajes
    
  # Calcular el porcentaje de citas por día
  for dia, cantidad in conteo_dias.items():
    porcentaje_por_dia[dia] = round((cantidad / total_citas) * 100, 2)
        
    dia = list(porcentaje_por_dia.keys()) # Obtener los días en el orden correcto
    porcentajes_dia = list(porcentaje_por_dia.values()) # Obtener los porcentajes en el orden correcto
    try:
      # Crear el gráfico de barras con matplotlib
        plt.figure(figsize=(8, 5))
        plt.bar(dia, porcentajes_dia, color='skyblue', width=0.5)
        plt.xlabel('dia')
        plt.ylabel('Porcentaje (%)')
        plt.title('Porcentaje de Citas por día')
        plt.ylim(0, 100)  # Asegurar que el eje Y vaya de 0 a 100
        
        # plt.pie(porcentajes, labels=meses, autopct='%1.1f%%', startangle=140)
        
        # Guardar el gráfico en un buffer de memoria
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        grafico_porcentaje_dias = base64.b64encode(buffer.read()).decode('utf-8')
        plt.close()
    except:
      print('Ocurrió un error al crear el gráfico.')
    
  context = {
        'conteo_meses': conteo_meses,
        'conteo_dias': conteo_dias,
        'total_citas': total_citas,
        'porcentaje_por_dia': porcentaje_por_dia,
        'grafico_porcentaje_dias': f'data:image/png;base64,{grafico_porcentaje_dias}',
    }
  return render(request, 'balance/citas_por_dia.html', context)



