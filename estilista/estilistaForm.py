from django import forms
from .models import Estilista


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
        fields = ['user', 'dni', 'telefono']
       
        
        
# from django import forms
# from .models import Usuarios, Rol

# class UsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuarios
#         fields = ['user', 'dni', 'telefono', 'roles']
#         widgets = {
#             'roles': forms.CheckboxSelectMultiple()
#         }
