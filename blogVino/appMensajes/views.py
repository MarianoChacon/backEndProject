from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import FormResp
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


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
        
#------------------READ--------------

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'appMensajes/mensaje_list.html'

    

class MensajeVer(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'appMensajes/mensaje_ver.html'


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