from django.db import models

# Create your models here.
    
class Articulo(models.Model):

    Articulo_CHOICES = (
        ('0', 'pizzaron'),
        ('1', 'mesa'),
        ('2', 'silla'),
        ('3', 'banco'),
    )
   
    Nombre =models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre

