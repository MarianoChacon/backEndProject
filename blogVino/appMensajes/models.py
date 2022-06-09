from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):
    emisor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor')
    receptor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    mensaje=models.TextField()
    leido=models.BooleanField(null=TRUE)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesanje de {self.emisor} para {self.receptor} enviado {self.fecha}"

class NuevoMens(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    ultimoMensFecha=models.DateTimeField()

    def __str__(self):
        return f"Usuario {self.usuario}. Fecha: {self.ultimoMensFecha}"
    