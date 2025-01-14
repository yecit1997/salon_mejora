from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Nombre de usuario'
        })
    )
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Contraseña'
        })
    )
    
    labels = {
            'username': '',
            'password': '',
            
        }



