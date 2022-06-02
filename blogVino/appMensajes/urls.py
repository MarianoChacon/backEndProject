from django.urls import path
from .views import *


urlpatterns = [

    path('mensajes/inicio/', MensajeCrear.as_view(), name='inicioMensajes'),
    path('mensajes/list/', MensajeList.as_view() , name='mensajeList'),
    path('mensaje/ver/<pk>', MensajeVer.as_view(), name='mensaje_ver'),
    path('mensaje/resp/', respForm, name='respForm'),

]