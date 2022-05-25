from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from appPosteos.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView


# Create your views here.


def prueba(request):
    return render(request, 'AppPosteos/prueba.html')

#------------------CREATE--------------

class PosteoCrear(CreateView):
    model = Posteo
    success_url = reverse_lazy('list')
    fields=['titulo', 'subtitulo', 'cuerpo','autor','resumen','imagen']

#------------------READ--------------

class PosteoList(ListView):
    model = Posteo
    template_name = 'appPosteos/posteo_list.html'
    imagenposteo=Posteo.objects.all()
    extra_context={'imagenesurl': imagenposteo[0].imagen.url}

class PosteoDetalle(DetailView):
    model = Posteo
    template_name = 'appPosteos/posteo_detalle.html'


#-----------------UPDATE---------------------

class PosteoEditar(UpdateView):
    model = Posteo
    success_url = reverse_lazy('list')
    fields=['titulo', 'subtitulo', 'cuerpo','autor','resumen','imagen']

#-----------------DELETE---------------------

class PosteoEliminar(DeleteView):
    model = Posteo
    success_url = reverse_lazy('list')