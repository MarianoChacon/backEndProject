from asyncio.windows_events import NULL
from datetime import datetime
from email.policy import default
from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class FormResp(forms.Form):
    
    receptor=forms.ModelChoiceField(queryset=User.objects.all())
    mensaje=forms.CharField(max_length=500)
    emisor=forms.HiddenInput()

    class Meta:
        model = Mensaje
        exclude = ['emisor']

    
    
