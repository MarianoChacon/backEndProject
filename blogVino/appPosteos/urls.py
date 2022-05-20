
from django.urls import path
from appPosteos.views import *

urlpatterns = [

    path('', PosteoList.as_view(), name='List'),
    

]