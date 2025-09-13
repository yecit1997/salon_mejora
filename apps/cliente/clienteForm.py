from django import forms
from .models import Cliente


class CombinedUserClienteForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre de usuario'})
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        required=True
    )  # Password opcional
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'})
    )
    first_name = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'})
    )
    last_name = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Tu apellido'})
    )
    dni = forms.CharField(
        max_length=11,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Número de DNI'})
    )
    telefono = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Número de teléfono'})
    )
    # is_active = forms.BooleanField(required=False)


    class Meta:
        model = Cliente
        fields = ['dni', 'first_name', 'last_name', 'username', 'password', 'email', 'telefono']

    def __init__(self, *args, **kwargs):
        super(CombinedUserClienteForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields.pop('password')