from django import forms
from .models import Servicio


class servicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'descripcion'}),
            # 'precio': forms.DecimalField(),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': '',
            'descripcion': '',
            'precio': 'Precio',
            'imagen': '',
        }

        


