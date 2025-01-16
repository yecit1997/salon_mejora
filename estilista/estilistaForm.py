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

    # def save(self, commit=True):
    #     user = super(EstilistaForm, self).save(commit=False)
    #     user.username = self.cleaned_data['username']
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     if self.cleaned_data['password']:
    #         user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #     return user