from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length = 30)
    descripcion = models.TextField()
    # imagen = 
    autor = models.ForeignKey("auth.User", on_delete = models.CASCADE)