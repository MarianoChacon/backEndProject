from django.urls import path
from .views import *


urlpatterns = [

    path('mensajes/inicio/', MensajeCrear.as_view() , name='inicioMensajes'),
    path('mensajes/list/', MensajeList.as_view() , name='mensajesList'),
]