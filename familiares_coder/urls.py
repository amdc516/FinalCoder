"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
#from .views import listado_familiares
from familiares_coder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('inicio2', views.inicio2, name="Inicio2"),
    path('nopagesyet', views.nopagesyet, name="NoPagesYet"),
    path('familiar', views.familiar, name="Familiar"),
    path('mascota', views.mascota, name="Mascota"),
    path('pelicula', views.pelicula, name="Pelicula"),
    path('mascotas', views.mascotas, name="Mascotas"),
    path('familiares', views.familiares, name="Familiares"),
    path('mensajes', views.mensajes, name="Mensajes"),
    path('peliculas', views.peliculas, name="Peliculas"),
    path('busquedaAnimal', views.busquedaAnimal, name="BusquedaAnimal"),
    path('buscarAnimal/', views.buscarAnimal),
    path('busquedaFamiliar', views.busquedaFamiliar, name="BusquedaFamiliar"),
    path('buscarFamiliar/', views.buscarFamiliar),
    path('busquedaPelicula', views.busquedaPelicula, name="BusquedaPelicula"),
    path('buscarPelicula/', views.buscarPelicula),
    path('leerFamiliares', views.leerFamiliares, name="LeerFamiliares"),
    path('leerMascotas', views.leerMascotas, name="LeerMascotas"),
    path('leerPeliculas', views.leerPeliculas, name="LeerPeliculas"),
    path('eliminarFamiliar/<familiar_nombre>/', views.eliminarFamiliar, name="EliminarFamiliar"),
    path('eliminarMascota/<mascota_nombre>/', views.eliminarMascota, name="EliminarMascota"),
    path('eliminarPelicula/<pelicula_nombre>/', views.eliminarPelicula, name="EliminarPelicula"),
    path('editarFamiliar/<familiar_nombre>/', views.editarFamiliar, name="EditarFamiliar"),
    path('editarMascota/<mascota_nombre>/', views.editarMascota, name="EditarMascota"),
    path('editarPelicula/<pelicula_nombre>/',views.editarPelicula,name="EditarPelicula"),
    
    path('familiar/list',views.FamiliarList.as_view(),name='List1'),
    path(r'^(?P<pk>\d+)1$', views.FamiliarDetalle.as_view(), name='Detail1'),
    path(r'^nuevo1$', views.FamiliarCreacion.as_view(), name='New1'),
    path(r'^editar/(?P<pk>\d+)1$',views.FamiliarUpdate.as_view(),name = 'Edit1'),
    path(r'^borrar/(?P<pk>\d+)1$',views.FamiliarDelete.as_view(),name = 'Delete1'),
    
    path('mascota/list',views.MascotaList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.MascotaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.MascotaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.MascotaUpdate.as_view(),name = 'Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.MascotaDelete.as_view(),name = 'Delete'),
    path('pelicula/list',views.PeliculaList.as_view(),name='List2'),
    path(r'^(?P<pk>\d+)2$', views.PeliculaDetalle.as_view(), name='Detail2'),
    path(r'^nuevo2$', views.PeliculaCreacion.as_view(), name='New2'),
    path(r'^editar/(?P<pk>\d+)2$',views.PeliculaUpdate.as_view(),name = 'Edit2'),
    path(r'^borrar/(?P<pk>\d+)2$',views.PeliculaDelete.as_view(),name = 'Delete2'),
    path('login',views.login_request, name = 'Login'),
    path('register',views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='familiares_coder/logout.html'), name='Logout'),
    path('editarPerfil',views.editarPerfil, name="EditarPerfil"),
    
]

