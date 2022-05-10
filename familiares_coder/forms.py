from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    
class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    animal = forms.CharField(max_length=40)
    
class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    estreno = forms.DateField()
    

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','last_name','first_name']
        help_texts = {k:"" for k in fields}    
        

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
        
        
class MessageForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)