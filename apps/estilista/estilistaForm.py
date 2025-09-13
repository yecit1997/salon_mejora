from django import forms
from .models import Estilista

class EstilistaForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, required=False)  # Password opcional
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=10)
    telefono = forms.CharField(max_length=20)

    class Meta:
        model = Estilista
        fields = ['dni', 'telefono']

    def __init__(self, *args, **kwargs):
        super(EstilistaForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields.pop('password')
