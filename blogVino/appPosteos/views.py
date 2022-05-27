from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from appPosteos.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


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


#-----------------VER UN POSTEO---------------------



class PosteoVer(DetailView):
    model = Posteo
    template_name = 'appPosteos/posteo_ver.html'


#-----------------login---------------------

def login_request(request):

    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contra)


            if user is not None:
                login(request, user)
                return render(request, "appPosteos/posteo_list.html", {'mensaje': f"Bienvenido {usuario}"})
            else:
                return render(request, "appPosteos/posteo_list.html", {'mensaje': "Error, datos incorrectos"})
        else:
                return render(request, "appPosteos/posteo_list.html", {'mensaje': "Error, formulario erróneo"})

    form=AuthenticationForm()

    return render(request, "appPosteos/login.html", {'form':form})