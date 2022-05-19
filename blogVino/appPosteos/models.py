from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from django.forms import CharField

# Create your models here.

class posteo(models.Model):
    titulo=models.CharField(max_length=80, unique=TRUE)
    subtitulo=models.CharField(max_length=80)
    cuerpo=models.TextField()
    autor=models.CharField(max_length=30)
    fecha=models.DateField()
    resumen=models.TextField()
    imagen=models.ImageField(upload_to='posteos', null=True, blank=True)