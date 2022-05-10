from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"nombre: {self.nombre} - apellido : {self.apellido} - edad : {self.edad}"

    
class Mascota(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    animal = models.CharField(max_length=40)

    def __str__(self):
        return f"nombre: {self.nombre} - edad : {self.edad} - animal : {self.animal}"

class PeliculaFavorita(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    estreno = models.DateField()
    
    def __str__(self):
        return f"nombre: {self.nombre} - genero : {self.genero} - estreno : {self.estreno}"
    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    
class Mensaje(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email_address = models.EmailField(max_length = 150)
	message = models.CharField(max_length = 2000)
    