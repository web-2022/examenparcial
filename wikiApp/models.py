from django.db import models

# Create your models here.
class temaWiki(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=512)

    def __str__(self):
        return self.nombre

class articuloWiki(models.Model):
    titulo = models.CharField(max_length=128)
    contenido = models.CharField(max_length=1024)
    temaRelacionado = models.ForeignKey(temaWiki, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
