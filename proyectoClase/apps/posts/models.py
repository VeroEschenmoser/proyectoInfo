from django.db import models
from django.urls import timezone

# Create your models here.



#categorias

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Posts(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.CharField(null=False)
    activo = models.models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default="sin categoria")
    imagen = models.ImageField(upload_to='media', null=True, blank=True, default='static/post_default.png')
    publicado = models.DateTimeRangeField(default=timezone.now)

class meta:

    ordering = ['-publicado']    

def __str__(self):
    return self.titulo


def delete(self, using=None, keep_parents=False):
    self.imagen.storage.delete(self.imagen.name)
    super().delete()