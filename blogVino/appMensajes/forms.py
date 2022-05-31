from asyncio.windows_events import NULL
from django import forms
from django.contrib.auth.models import User


class FormMensaje(forms.Form):
    
    receptor=forms.CharField(max_length=30)
    mensaje=forms.CharField(max_length=500)

    
    
