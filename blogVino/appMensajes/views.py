import re
from xmlrpc.client import DateTime
from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Mensaje, NuevoMens
from .forms import FormResp
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.

@login_required
def inicioMensajes(request):
    return render(request, 'appMensajes/inicio.html')



#------------------CREATE--------------

class MensajeCrear(LoginRequiredMixin,CreateView):
    model = Mensaje
    success_url = reverse_lazy('inicioMensajes')
    fields=['receptor', 'mensaje']

    def form_valid(self, form):
        form.instance.emisor = self.request.user
        return super().form_valid(form)
        


#---------------------Form para responder mensaje------------

@login_required
def respForm(request):
  
    if request.method =='POST':
        form=FormResp(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            mensaje=Mensaje(emisor=User.objects.get(username=request.user), receptor=informacion['receptor'], mensaje=informacion['mensaje'])
            mensaje.save()

            return render(request, 'appMensajes/mensaje_responder.html')

    else:
        form=FormResp()
        

        return render (request,'appMensajes/mensaje_responder.html', {'form':form})

#------------------READ de mensajes + formulario de respuesta--------------

@login_required
def listaMensajes(request):
    listaUsuarios=User.objects.all()
    mensajes=Mensaje.objects.all()

    for mensaje in mensajes:
        if (mensaje.receptor == request.user):
        
            mensaje.leido= True
            mensaje.save()

    
    mens=Mensaje.objects.all()

    if request.method =='POST':
        form=FormResp(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            mensaje=Mensaje(emisor=User.objects.get(username=request.user), receptor=informacion['receptor'], mensaje=informacion['mensaje'])
            mensaje.save()

            

    else:
        form=FormResp()

    return render(request, 'appMensajes/mensaje_list.html', {'mens':mens, 'listaUsuarios':listaUsuarios,'form':form})


@login_required
def nuevoMensRecib(request):
    
    #tiempoDesdeUltimoMensActual=datetime.datetime.now()-Mensaje.objects.filter(receptor=request.user).order_by('-fecha').values_list('fecha')[0]
    #tiempoDesdeUltimoMensGuardado=datetime.datetime.now()-NuevoMens.objects.filter(user=request.user).values_list('ultimoMensFecha')[0]
    #if tiempoDesdeUltimoMensActual<tiempoDesdeUltimoMensGuardado:

        #tieneMensajeNuevo="Usted tiene un mensaje nuevo"
    
    
        #return render(request, 'appMensajes/prueba.html', {'expresion':tieneMensajeNuevo})
    
    #else:
        #noTieneMensajeNuevo="Ustes no tiene un mensaje nuevo"
        #return render(request, 'appMensajes/prueba.html', {'expresion':noTieneMensajeNuevo})

        a=datetime.now()
        c=str(Mensaje.objects.filter(receptor=request.user).order_by('-fecha').values_list('fecha')[0])
        d=c[19:48]
        b=datetime.strptime(d, '%Y, %m, %d, %H, %M, %S, %f')

        e=a-b
        return render(request, 'appMensajes/prueba.html', {'a':a, 'b':b, 'e':e})