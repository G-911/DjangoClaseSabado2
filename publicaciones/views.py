from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post
# Create your views here.

class PaginaDeInicio(TemplateView):
    template_name = "inicio.html"
    
    
class PaginaDePublicaciones(ListView):
    template_name = "publicaciones.html"
    model = Post
    
    
class PaginaDeDetalleDeLaPublicacion(DetailView):
    template_name = "detalle.html"
    model = Post