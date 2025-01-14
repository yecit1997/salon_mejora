from django import forms
from .models import Estilista

# class EstilistaForm(forms.ModelForm):
#     class Meta:
#         model = Estilista
#         fields = '__all__'
        # widgets = {
        #     'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI'}),
        #     'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        #     'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
        #     'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
        #     'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        # }
        # labels = {
        #     'dni': '',
        #     'nombre': '',
        #     'apellido': '',
        #     'telefono': '',
        #     'email': '',
        #     'direccion': '',
        #     'imagen': '',
        # }


class EstilistaForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=10)
    telefono = forms.CharField(max_length=20)

    class Meta:
        model = Estilista
        fields = ['dni', 'telefono']