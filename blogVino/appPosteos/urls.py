
from django.urls import path
from appPosteos.views import *

urlpatterns = [

    path('posteo/list/', PosteoList.as_view(), name='list'),
    path('posteo/<pk>', PosteoDetalle.as_view(), name='posteo_detalle'),
    path('posteo/nuevo/', PosteoCrear.as_view(), name='posteoCrear'),
    path('posteo/editar/<pk>', PosteoEditar.as_view(), name='posteoEditar'),
    path('posteo/eliminat/<pk>', PosteoEliminar.as_view(), name='posteoEliminar'),
    
    

]