from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Prueba

class PruebaView(TemplateView):
    template_name = "home/prueba.html"
    
    
class PruebaListView(ListView):

        template_name = 'home/list.html'
        context_object_name = 'listanumeros'
        queryset = ['0','10','20','30']
    
class ListaPrueba(ListView):
      template_name = "home/lista_prueba.html"
      model = Prueba
      context_object_name = "lista"
