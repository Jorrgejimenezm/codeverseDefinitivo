from django.contrib import admin
from .models import Grupo, Publicacion,Comentario

# Register your models here.

class GrupoAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','administrador']
admin.site.register(Grupo,GrupoAdmin)

class PublicacionAdmin(admin.ModelAdmin):
    list_display=['usuario','contenido']
admin.site.register(Publicacion,PublicacionAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display=['autor','publicacion','contenido']
admin.site.register(Comentario,ComentarioAdmin)