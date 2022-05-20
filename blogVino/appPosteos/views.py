from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from appPosteos.models import *
# Create your views here.



#------------------READ--------------

class PosteoList(ListView):
    Model = Posteo
    template_name = 'appPosteos/posteos.html'