from django.db import models

# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 30)
    cuerpo = models.CharField(max_length = 1000)
    autor = models.CharField(max_length = 30)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to = 'blogs', null = True, blank = True)

    def __str__(self) -> str:
        return f'Titulo: {self.titulo} - Autor: {self.autor}'
