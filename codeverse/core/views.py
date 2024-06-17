from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Publicacion, Grupo, Comentario
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView
from.forms import PublicacionForm

class HomeView(ListView):
    model = Publicacion
    template_name = 'core/home.html'
    context_object_name = 'publicaciones'


@method_decorator(login_required, name='dispatch')
class CrearGruposView(CreateView):
    model = Grupo
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.administrador = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CrearPublicacionView(CreateView):
    model = Publicacion
    fields = ['contenido', 'video', 'imagen', 'grupo']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch') 
class borrarGrupo(DeleteView):
    model = Grupo
    success_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        grupo = self.get_object() #me devuleve el articulo que se quiere modificar
        if grupo.administrador != request.user: #comprobar si el autor el el mismo que el user logrado
            raise PermissionDenied #lanzar un error de permisos

        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(login_required, name='dispatch')
class modificarGrupo(UpdateView):
    model = Grupo
    fields = ['nombre', 'descripcion', 'fecha_creacion']
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        grupo = self.get_object()  # me devuelve el artículo que se quiere modificar
        if grupo.administrador != request.user:  # comprobar si el autor es el mismo que el usuario logrado
            raise PermissionDenied  # lanzar una excepción de permisos específica de Django

        return super().dispatch(request, *args, **kwargs)
    


@method_decorator(login_required, name='dispatch') 
class borrarPublicacion(DeleteView):
    model = Publicacion
    success_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        publicaccion = self.get_object() #me devuleve el articulo que se quiere modificar
        if publicaccion.usuario != request.user: #comprobar si el autor el el mismo que el user logrado
            raise PermissionDenied #lanzar un error de permisos

        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(login_required, name='dispatch')
class modificarPublicacion(UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'core/publicacion_form.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        publicacion = self.get_object()  # me devuelve el artículo que se quiere modificar
        if publicacion.usuario != request.user:  # comprobar si el autor es el mismo que el usuario logrado
            raise PermissionDenied  # lanzar una excepción de permisos específica de Django

        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(login_required, name='dispatch')    
class misPubliciones(ListView):
    model = Publicacion
    template_name = 'core/mis_publicaciones.html'
    context_object_name = 'publicaciones'

    def get_queryset(self):
        # Filter the queryset to include only posts by the logged-in user
        user = self.request.user
        return Publicacion.objects.filter(usuario=user)
   
class PublicacionDetailView(DetailView):
    model = Publicacion  # Specify the model to use
    template_name = 'core/publicacion_detail.html'  # Define the template name for the detail view
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(publicacion=self.object)
        return context
    

from django.shortcuts import render
from .models import Publicacion

def buscar_publicaciones(request):
    usuario = request.GET.get('usuario', '')
    if usuario:
        publicaciones = Publicacion.objects.filter(usuario__username__icontains=usuario)
    else:
        publicaciones = Publicacion.objects.all()
    
    context = {
        'publicaciones': publicaciones
    }
    return render(request, 'core/home.html', context)

@method_decorator(login_required, name='dispatch')
class CrearGruposView(CreateView):
    model = Grupo
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        if request.user.userprofile.user_level == 'experimentado':
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("<h1>No tienes permiso para crear Grupos.</h1>")
    def form_valid(self, form):
        form.instance.administrador = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CrearPublicacionView(CreateView):
    model = Publicacion
    fields = ['contenido', 'video', 'imagen', 'grupo']
    success_url = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        if request.user.userprofile.user_level == 'experimentado':
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("<h1>No tienes permiso para crear publicaciones.</h1>")
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
