from django import forms
from .models import Cita

class citaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
            # 'cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cliente'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'fecha', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'hora', 'type': 'time'}),
        }
        labels = {
            'servicio': 'Servicio',
            'estilista': 'Estilista',
            'cliente': 'Cliente',
            'fecha': 'Fecha servicio',
            'hora': 'Hora servicio',
        }
