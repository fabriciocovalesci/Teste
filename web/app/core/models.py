from django.db import models

class Foto(models.Model): 
    name = models.CharField(max_length=50) 
    foto_carregada = models.ImageField(upload_to='media') 