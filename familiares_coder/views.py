from re import template
from wsgiref.util import request_uri
from django.shortcuts import render
from django.template import loader
from .models import Familiar
from .models import Mascota
from .models import PeliculaFavorita
from .models import Avatar
from .models import Mensaje
from django.http import HttpResponse
from familiares_coder.forms import FamiliarFormulario
from familiares_coder.forms import MascotaFormulario
from familiares_coder.forms import PeliculaFormulario
from familiares_coder.forms import MessageForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#def listado_familiares(request):
    
#    template = loader.get_template('listado_familiares.html')
#    familiares = Familiar.objects.all()
#    print(familiares)
#    context = {
#        'familiares': familiares,
#    }
#    return HttpResponse(template.render(context,request))

@login_required(login_url='Inicio2')
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request,"familiares_coder/inicio.html",{"url":avatares[0].imagen.url})

def inicio2(request):
    return render(request, "familiares_coder/inicio2.html")

def familiar(request):
    return render(request,"familiares_coder/familiar.html")

def mascota(request):
    return render(request,"familiares_coder/mascota.html")

def pelicula(request):
    return render(request,"familiares_coder/pelicula.html")

def mascotas(request):
    
    if request.method == 'POST':
        
        miFormulario = MascotaFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
        
            mascota = Mascota (nombre=informacion['nombre'], edad=informacion['edad'], animal=informacion['animal'])
        
            mascota.save()
        
            return render(request, "familiares_coder/inicio.html")
    
    else:
                
        miFormulario= MascotaFormulario()
        
    return render(request,"familiares_coder/mascotas.html",{"miFormulario":miFormulario})



def familiares(request):
    
    if request.method == 'POST':
        
        miFormulario = FamiliarFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
        
            familiar = Familiar (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])
        
            familiar.save()
        
            return render(request, "familiares_coder/inicio.html")
    
    else:
                
        miFormulario= FamiliarFormulario()
        
    return render(request,"familiares_coder/familiares.html",{"miFormulario":miFormulario})





def peliculas(request):
    
    if request.method == 'POST':
        
        miFormulario = PeliculaFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
        
            pelicula = PeliculaFavorita (nombre=informacion['nombre'], genero=informacion['genero'], estreno=informacion['estreno'])
        
            pelicula.save()
        
            return render(request, "familiares_coder/inicio.html")
    
    else:
                
        miFormulario= PeliculaFormulario()
        
    return render(request,"familiares_coder/peliculas.html",{"miFormulario":miFormulario})





def mensajes(request):
    
    if request.method == 'POST':
        
        miFormulario = MessageForm(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
        
            mensaje = Mensaje(first_name=informacion['first_name'], last_name=informacion['last_name'], email_address=informacion['email_address'], message=informacion['message'])
        
            mensaje.save()
        
            return render(request, "familiares_coder/inicio2.html")
    
    else:
                
        miFormulario= MessageForm()
        
    return render(request,"familiares_coder/mensajes.html",{"miFormulario":miFormulario})




def busquedaFamiliar(request):
    return render(request, "familiares_coder/busquedaFamiliar.html")

def buscarFamiliar(request):
    
    if request.GET['nombre']:
        
        nombreFamiliar = request.GET['nombre']
        nombreFamiliares = Familiar.objects.filter(nombre__icontains=nombreFamiliar)
        
        return render(request, "familiares_coder/resultadosBusquedaFamiliar.html", {"nombreFamiliares": nombreFamiliares, "nombre": nombreFamiliar})
    
    else:
        
        respuesta= "No enviaste datos"
        
    return HttpResponse(respuesta)




def busquedaAnimal(request):
    return render(request, "familiares_coder/busquedaAnimal.html")

def buscarAnimal(request):
    
    if request.GET['animal']:
        
        animal = request.GET['animal']
        animales = Mascota.objects.filter(animal__icontains=animal)
        
        return render(request, "familiares_coder/resultadosBusquedaAnimal.html", {"animales": animales, "animal": animal})
    
    else:
        
        respuesta= "No enviaste datos"
        
    return HttpResponse(respuesta)
    



def busquedaPelicula(request):
    return render(request, "familiares_coder/busquedaPelicula.html")

def buscarPelicula(request):
    
    if request.GET['nombre']:
        
        nombrePelicula = request.GET['nombre']
        nombrePeliculas = PeliculaFavorita.objects.filter(nombre__icontains=nombrePelicula)
        
        return render(request, "familiares_coder/resultadosBusquedaPelicula.html", {"nombrePeliculas": nombrePeliculas, "nombre": nombrePelicula})
    
    else:
        
        respuesta= "No enviaste datos"
        
    return HttpResponse(respuesta)



def leerFamiliares(request):
    
    familiares = Familiar.objects.all()
    contexto = {"familiares": familiares}
    
    return render(request,"familiares_coder/leerFamiliares.html",contexto)


def leerMascotas(request):
    
    mascotas = Mascota.objects.all()
    contexto = {"mascotas": mascotas}
    
    return render(request,"familiares_coder/leerMascotas.html",contexto)


def leerPeliculas(request):
    
    peliculas = PeliculaFavorita.objects.all()
    contexto = {"peliculas": peliculas}
    
    return render(request,"familiares_coder/leerPeliculas.html",contexto)


def eliminarFamiliar(request,familiar_nombre):
    
    familiar = Familiar.objects.get(nombre=familiar_nombre)
    familiar.delete()
    
    familiares = Familiar.objects.all()
    contexto = {"familiares": familiares}
    
    return render(request,"familiares_coder/leerFamiliares.html",contexto)



def eliminarMascota(request,mascota_nombre):
    
    mascota = Mascota.objects.get(nombre=mascota_nombre)
    mascota.delete()
    
    mascotas = Mascota.objects.all()
    contexto = {"mascotas": mascotas}
    
    return render(request,"familiares_coder/leerMascotas.html",contexto)



def eliminarPelicula(request,pelicula_nombre):
    
    pelicula = PeliculaFavorita.objects.get(nombre=pelicula_nombre)
    pelicula.delete()
    
    peliculas = PeliculaFavorita.objects.all()
    contexto = {"peliculas": peliculas}
    
    return render(request,"familiares_coder/leerPeliculas.html",contexto)




def editarFamiliar(request, familiar_nombre):
    
    familiar = Familiar.objects.get(nombre=familiar_nombre)
    
    if request.method == 'POST':
        
        miFormulario = FamiliarFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            familiar.nombre = informacion['nombre']
            familiar.apellido = informacion['apellido']
            familiar.edad = informacion['edad']
            
            familiar.save()
            
            return render(request, "familiares_coder/inicio.html")
        
    else:
            
        miFormulario = FamiliarFormulario(initial={'nombre': familiar.nombre, 'apellido' : familiar.apellido, 'edad': familiar.edad})
            
    return render(request, "familiares_coder/familiares.html",{"miFormulario":miFormulario,"familiar_nombre":familiar_nombre})
    






def editarMascota(request, mascota_nombre):
    
    mascota = Mascota.objects.get(nombre=mascota_nombre)
    
    if request.method == 'POST':
        
        miFormulario = MascotaFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            mascota.nombre = informacion['nombre']
            mascota.edad = informacion['edad']
            mascota.animal = informacion['animal']
            
            mascota.save()
            
            return render(request, "familiares_coder/inicio.html")
        
    else:
            
        miFormulario = MascotaFormulario(initial={'nombre': mascota.nombre, 'edad' : mascota.edad, 'animal': mascota.animal})
            
    return render(request, "familiares_coder/mascotas.html",{"miFormulario":miFormulario,"mascota_nombre":mascota_nombre})
    


def editarPelicula(request, pelicula_nombre):
    
    pelicula = PeliculaFavorita.objects.get(nombre=pelicula_nombre)
    
    if request.method == 'POST':
        
        miFormulario = PeliculaFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            pelicula.nombre = informacion['nombre']
            pelicula.genero = informacion['genero']
            pelicula.estreno = informacion['estreno']
            
            pelicula.save()
            
            return render(request, "familiares_coder/inicio.html")
        
    else:
            
        miFormulario = PeliculaFormulario(initial={'nombre': pelicula.nombre, 'genero' : pelicula.genero, 'estreno': pelicula.estreno})
            
    return render(request, "familiares_coder/peliculas.html",{"miFormulario":miFormulario,"pelicula_nombre":pelicula_nombre})




class FamiliarList(ListView):
    
    model = Familiar
    template_name = "familiares_coder/familiares_list.html"
    
class FamiliarDetalle(DetailView):
    
    model = Familiar
    template_name = "familiares_coder/familiar_detalle.html"
    
class FamiliarCreacion(CreateView):
    
    model = Familiar
    success_url = "/familiares_coder/familiar/list"
    fields = ['nombre','apellido','edad']
    
class FamiliarUpdate(UpdateView):
    model = Familiar
    success_url = "/familiares_coder/familiar/list"
    fields = ['nombre','apellido','edad']
    
class FamiliarDelete(DeleteView):
    model = Familiar
    success_url = "/familiares_coder/familiar/list"






class MascotaList(ListView):
    
    model = Mascota
    template_name = "familiares_coder/mascotas_list.html"
    
class MascotaDetalle(DetailView):
    
    model = Mascota
    template_name = "familiares_coder/mascota_detalle.html"
    
class MascotaCreacion(CreateView):
    
    model = Mascota
    success_url = "/familiares_coder/mascota/list"
    fields = ['nombre','edad','animal']
    
class MascotaUpdate(UpdateView):
    model = Mascota
    success_url = "/familiares_coder/mascota/list"
    fields = ['nombre','edad','animal']
    
class MascotaDelete(DeleteView):
    model = Mascota
    success_url = "/familiares_coder/mascota/list"




class PeliculaList(ListView):
    
    model = PeliculaFavorita
    template_name = "familiares_coder/peliculas_list.html"
    
class PeliculaDetalle(DetailView):
    
    model = PeliculaFavorita
    template_name = "familiares_coder/pelicula_detalle.html"
    
class PeliculaCreacion(CreateView):
    
    model = PeliculaFavorita
    success_url = "/familiares_coder/pelicula/list"
    fields = ['nombre','genero','estreno']
    
class PeliculaUpdate(UpdateView):
    model = PeliculaFavorita
    success_url = "/familiares_coder/pelicula/list"
    fields = ['nombre','genero','estreno']
    
class PeliculaDelete(DeleteView):
    model = PeliculaFavorita
    success_url = "/familiares_coder/pelicula/list"






def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                
                return render(request, "familiares_coder/inicio.html", {"mensaje":f"Bienvenidx {usuario}"})
            else:
                return render(request, "familiares_coder/inicio.html", {"mensaje":"Error, datos incorrectos"})
            
        else:
            
                return render(request, "familiares_coder/inicio.html", {"mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()

    return render(request, "familiares_coder/login.html", {'form':form})






def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "familiares_coder/inicio.html", {"mensaje":"Usuario creado :)"})
            
           
            
    else:
            form = UserRegisterForm()
            
    return render(request, "familiares_coder/registro.html", {"form":form})
    

@login_required
def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return render(request, "familiares_coder/inicio.html")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
    return render(request, "familiares_coder/editarPerfil.html",{"miFormulario":miFormulario,"usuario":usuario})


def nopagesyet(request):
    return render(request, "familiares_coder/nopagesyet.html")