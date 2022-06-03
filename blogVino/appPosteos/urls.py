
from django.urls import path
from appPosteos.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('posteo/list/', PosteoList.as_view(), name='list'),
    path('posteo/<pk>', PosteoDetalle.as_view(), name='posteo_detalle'),
    path('posteo/nuevo/', PosteoCrear.as_view(), name='posteoCrear'),
    path('posteo/editar/<pk>', PosteoEditar.as_view(), name='posteoEditar'),
    path('posteo/eliminat/<pk>', PosteoEliminar.as_view(), name='posteoEliminar'),
    path('posteo/ver/<pk>', PosteoVer.as_view(), name='posteo_ver'),
    path('login', login_request,name='login'),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name='appPosteos/logout.html'), name='logout'),
    path('buscarAutor/', buscarAutor, name='buscarAutor'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
     path('aboutUs/', aboutUs, name='aboutUs'),

]