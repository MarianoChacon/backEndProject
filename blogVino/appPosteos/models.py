from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Posteo(models.Model):
    titulo=models.CharField(max_length=80, unique=True)
    subtitulo=models.CharField(max_length=80)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cuerpo=RichTextField()
    autor=models.CharField(max_length=30)
    fecha=models.DateTimeField(auto_now_add=True)
    resumen=models.TextField()
    imagen=models.ImageField(upload_to='posteos', null=True, blank=True)

    def __str__(self):
        return f"Posteo de {self.autor} realizado el {self.fecha}"
