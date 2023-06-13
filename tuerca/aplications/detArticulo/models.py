from django.db import models
from aplications.home.models import Articulo
# Create your models here.

class DetArticulo(models.Model):
    Numero = models.CharField(max_length=100)
    Articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    Fecha = models.DateTimeField()
    Observacion = models.CharField(max_length=100)
    Cantidad = models.IntegerField() 
    def __str__(self):
        return self.Numero
    