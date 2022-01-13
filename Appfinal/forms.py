from django import forms
from Appfinal import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Contacto(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    consulta = forms.CharField()

class UserRegisterForm(UserCreationForm):
    username= forms.CharField() 
    email= forms.CharField() 
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput) 
    password2= forms.CharField(label="Repetir la contraseña", widget= forms.PasswordInput)

    last_name= forms.CharField()  
    first_name= forms.CharField() 
    
    class Meta:
        model= User
        fields= ["username", "email", "password1", "password2", "last_name", "first_name"]
class UserEditForm(UserCreationForm):
    
    email= forms.CharField(label="Ingrese su Email") 
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput) 
    password2= forms.CharField(label="Repetir la contraseña", widget= forms.PasswordInput)

    last_name= forms.CharField()  
    first_name= forms.CharField() 
    
    class Meta:
        model= User
        fields= ["username", "email", "password1", "password2", "last_name", "first_name"]

class AvatarFormulario(forms.Form):
    
    imagen = forms.ImageField(required=True)  
