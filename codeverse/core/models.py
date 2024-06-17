from django.db import models
from django.contrib.auth.models import User

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre del grupo")
    descripcion = models.TextField(max_length=100, verbose_name="Descripcion")
    administrador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(max_length=250, verbose_name="Contenido")
    video = models.FileField(verbose_name="video", blank=True)
    imagen = models.ImageField(verbose_name="Foto", blank=True)
    fecha_publicacion = models.DateTimeField(verbose_name="Fecha de publicacion", auto_now_add=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, blank=True)
    numero_comentarios = models.IntegerField(default=0)
    def __str__(self):
        return self.contenido
    
class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE) 
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE) 
    contenido = models.TextField(max_length=500)  
    fecha_creacion = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
         return self.contenido