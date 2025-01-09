from django import forms
from .models import Estilista

class EstilistaForm(forms.ModelForm):
    class Meta:
        model = Estilista
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Telefono',
            'email': 'Email',
            'direccion': 'Direccion',
            'imagen': 'Imagen',
        }
        help_texts = {
            'nombre': 'Ingrese su nombre',
            'apellido': 'Ingrese su apellido',
            'telefono': 'Ingrese su telefono',
            'email': 'Ingrese su email',
            'direccion': 'Ingrese su direccion',
            'imagen': 'Ingrese su imagen',
        }
        error_messages = {
            'nombre': {
                'required': 'Este campo es requerido',
            },
            'apellido': {
                'required': 'Este campo es requerido',
            },
            'telefono': {
                'required': 'Este campo es requerido',
            },
            'email': {
                'required': 'Este campo es requerido',
            },
            'direccion': {
                'required': 'Este campo es requerido',
            },
            'imagen': {
                'required': 'Este campo es requerido',
            },
        }




