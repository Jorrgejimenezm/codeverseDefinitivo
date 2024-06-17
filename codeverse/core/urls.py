from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('crearGrupo', views.CrearGruposView.as_view(), name='crearGrupos'),
    path('crearPublicaciones', views.CrearPublicacionView.as_view(), name='crearPublicaciones'),
    path('borrarGrupo', views.borrarGrupo.as_view(), name='borrarGrupo'),
    path('modificarGrupo', views.modificarGrupo.as_view(), name='modificarGrupo'),
    path('borrarPublicacion', views.borrarPublicacion.as_view(), name='borrarPublicacion'),
    path('modificarPublicacion', views.modificarPublicacion.as_view(), name='modificarPublicacion'),
    path('misPublicaciones/', views.misPubliciones.as_view(), name='misPublicaciones'),
    path('publicacion/<int:pk>', views.PublicacionDetailView.as_view(), name='publicacion_detail'),
    path('publicacion/<int:pk>/editar/', views.modificarPublicacion.as_view(), name='publicacion_update'),
    path('publicacion/<int:pk>/eliminar/', views.borrarPublicacion.as_view(), name='publicacion_delete'),
    path('buscar-publicaciones/', views.buscar_publicaciones, name='buscar_publicaciones'),  # Asegúrate de que la URL esté definida correctamente aquí
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
