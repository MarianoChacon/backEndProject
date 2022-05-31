from django.shortcuts import render

# Create your views here.


def inicioMensajes(request):
    return render(request, 'appMensajes/inicio.html')