from datetime import datetime, timedelta
from django import forms
from .models import Cita

class citaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = 'estilista, fecha, hora'.split(', ')
        widgets = {
            # 'cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cliente'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'fecha', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'hora', 'type': 'time'}),
        }
        labels = {
        
            'estilista': 'Estilista',
            'fecha': 'Fecha servicio',
            'hora': 'Hora servicio',
        }

    def clean(self):
        cleaned_data = super().clean()
        estilista = cleaned_data.get('estilista')
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')

        if estilista and fecha and hora:
            # Convertir la fecha y hora seleccionadas en un objeto datetime
            fecha_hora = datetime.combine(fecha, hora)
            rango_inicio = fecha_hora - timedelta(hours=1)
            rango_fin = fecha_hora + timedelta(hours=1)
            citas_conflictivas = Cita.objects.filter(
                estilista=estilista,
                fecha=fecha,
                hora__range=(rango_inicio, rango_fin)
            )

            if citas_conflictivas.exists():
                raise forms.ValidationError("Este estilista ya tiene una cita en un rango de una hora para la hora seleccionada.")

        return cleaned_data



    
