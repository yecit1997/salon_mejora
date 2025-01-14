from django import forms
from django.contrib.auth.models import User
from .models import Cliente

class CombinedUserClienteForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=10)
    telefono = forms.CharField(max_length=20)

    class Meta:
        model = Cliente
        fields = ['dni', 'telefono']
