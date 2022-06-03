from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from appPosteos.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from appPosteos.forms import *

# Create your views here.



def aboutUs(request):
    return render(request, 'appPosteos/aboutUs.html')
#------------------CREATE--------------

class PosteoCrear(LoginRequiredMixin,CreateView):
    model = Posteo
    success_url = reverse_lazy('list')
    fields=['titulo', 'subtitulo', 'cuerpo','autor','resumen','imagen','user']

#------------------READ--------------

class PosteoList(ListView):
    model = Posteo
    template_name = 'appPosteos/posteo_list.html'
    

class PosteoDetalle(LoginRequiredMixin, DetailView):
    model = Posteo
    template_name = 'appPosteos/posteo_detalle.html'


#-----------------UPDATE---------------------

class PosteoEditar(LoginRequiredMixin,UpdateView):
    model = Posteo
    success_url = reverse_lazy('list')
    fields=['titulo', 'subtitulo', 'cuerpo','autor','resumen','imagen']

#-----------------DELETE---------------------

class PosteoEliminar(LoginRequiredMixin,DeleteView):
    model = Posteo
    success_url = reverse_lazy('list')


#-----------------VER UN POSTEO---------------------



class PosteoVer(LoginRequiredMixin, DetailView):
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
                return render(request, "appPosteos/loginConfirma.html", {'mensaje': f"Bienvenidx {usuario}"})
            else:
                return render(request, "appPosteos/login.html", {'form':form, 'mensaje': "Error, formulario erróneo"})
        else:
                return render(request, "appPosteos/login.html", {'form':form, 'mensaje': "Error, datos incorrectos"})

    form=AuthenticationForm()

    return render(request, "appPosteos/login.html", {'form':form})

#-----------------Register---------------------

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)

        if form.is_valid():
            
            username=form.cleaned_data['username']
            form.save()
            return render(request, "appPosteos/registerConfirma.html", {'mensaje': "Usuario creado correctamente"})

        else:
            return render(request, "appPosteos/registerConfirma.html", {'mensaje': "Ocurrió un error, inténtelo nuevamente"})

    else:
        form=UserRegistrationForm()

    return render(request, "appPosteos/register.html", {'form':form} )

#-----------------Buscar--------------------- 

def buscarAutor(request):
    if request.GET["autor"]:
        autor=request.GET['autor']
        posteos=Posteo.objects.filter(autor__icontains=autor)
        return render(request, 'appPosteos/resBusqAutor.html', {'posteos':posteos, 'autor':autor})
    else:
        respuesta="No ingresó datos"

    return render(request, 'appPosteos/resBusqAutor.html', {"respuesta":respuesta})

#-----------------Editar perfil---------------------

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=='POST':
        miFormulario=UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():

            informacion= miFormulario.cleaned_data

            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.first_name=informacion['first_name']
            usuario.last_name=informacion['last_name']
            usuario.save()

            return render(request, "appPosteos/editarPerfilConfrima.html", {'usuario':usuario, 'mensaje1':"Perfil editado correctamente"})
    else:
        miFormulario=UserEditForm(instance=usuario)
    return render(request, 'appPosteos/editarPerfil.html', {'formulario':miFormulario, 'usuario':usuario.username})