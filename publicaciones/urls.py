from django.urls import path
from .views import *

urlpatterns = [
    path ("", PaginaDeInicio.as_view(), name = "inicio"),
    path ("publicaciones", PaginaDePublicaciones.as_view(), name = "publicaciones"),
    
]