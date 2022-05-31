from asyncio.windows_events import NULL
from django import forms
from django.contrib.auth.models import User


class formMensaje(forms.Form):
    emisor=forms.CharField(max_length=30, NULL=False)
    receptor=forms.CharField(max_length=30, NULL=False)
    mensaje=forms.Textarea()
    
    
