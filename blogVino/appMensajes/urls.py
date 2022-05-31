from django.urls import path
from .views import *


urlpatterns = [

    path('mensajes/inicio/', inicioMensajes , name='inicioMensajes'),

]