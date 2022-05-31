from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(label='Ingrese su nombre de usuario')
    email=forms.EmailField(label="Ingrese e-mail")
    password1= forms.CharField(label='Ingrese su contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Ingrese su nombre')
    last_name=forms.CharField(label='Ingrese su apellido')
    
    class Meta:
        model= User
        fields= ['username','email','password1','password2','first_name','last_name']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    username=forms.CharField(label='Ingrese su nombre de usuario')
    email=forms.EmailField(label="Ingrese nuevo e-mail")
    password1= forms.CharField(label='Ingrese nueva contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita su nueva contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Ingrese su nombre')
    last_name=forms.CharField(label='Ingrese su apellido')

    class Meta:
        model= User
        fields=['username','email','password1','password2','first_name','last_name']
        help_texts = {k:"" for k in fields}


    
