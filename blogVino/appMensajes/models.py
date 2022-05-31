from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):
    emisor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor')
    receptor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    mensaje=models.TextField()
    leido=models.BooleanField()
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesanje de {self.emisor} para {self.receptor} enviado {self.fecha}"