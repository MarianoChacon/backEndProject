from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import FormMensaje
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.


def inicioMensajes(request):
    return render(request, 'appMensajes/inicio.html')

#@login_required
#def formMensaje(request):
 #   mensaje=request.user

  #  if request.method=="POST":
   #     formulario=FormMensaje(request.POST)

    #    if formulario.is_valid():
     #       informacion=formulario.cleaned_data

      #      mensaje.emisor=request.user
       #     mensaje.receptor=informacion['receptor']
        #    mensaje.mensaje=informacion['mensaje']

         #   mensaje.save()
          #  return render(request, "appMensajes/inicio.html", {'mensaje':mensaje})
    #else:
       # formulario=FormMensaje()

    #return render (request, "appMensajes/inicio.html", {'formulario':formulario})


#------------------CREATE--------------

class MensajeCrear(LoginRequiredMixin,CreateView):
    model = Mensaje
    success_url = reverse_lazy('inicioMensajes')
    fields=['emisor','receptor', 'mensaje']

#------------------READ--------------

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'appMensajes/mensaje_list.html'


class MensajeVer(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'appMensajes/mensaje_ver.html'