from django.forms.forms import Form
from django.shortcuts import render
from Appfinal import forms
from Appfinal.models import FormularioContacto, Accesorios, ZapatillasDeportivas,Pantalones,Botines,Remeras
from Appfinal.forms import FormularioContact
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from Appfinal.forms import UserRegisterForm
from django. contrib.auth.decorators import login_required
from Appfinal.models import Indumentaria
from Appfinal.forms import UserRegisterForm

# Create your views here.

def index(request):

    return render(request, 'Appfinal/padre.html')

def formularioContacto(request):
    if request.method == "POST":
      miFormulario = FormularioContact(request.POST)
      if miFormulario.is_valid():
          informacion = miFormulario.cleaned_data
          cliente = FormularioContacto(

              nombre = informacion["nombre"],
              apellido = informacion["apellido"],
              email = informacion["email"],
              telefono = informacion["telefono"],
              consulta = informacion["consulta"])

          
          cliente.save()
          return render(request, 'Appfinal/padre.html')
    else: 
        miFormulario = FormularioContacto()
    
    return render(request, 'Appfinal/formularioContacto.html')

def confirmacionContacto(request):

    return render(request, 'Appfinal/confirmacionContacto.html')


def tiendaVirtual(request):
    return render(request, 'Appfinal/tiendaVirtual.html')
#List
class Zapatillas(ListView):
    model = ZapatillasDeportivas
    template_name = 'Appfinal/zapatillas_list.html'
class Pantalon(ListView):
    model = Pantalones
    template_name = 'Appfinal/pantalones_list.html'
class Remera(ListView):
    model = Remeras
    template_name = 'Appfinal/remeras_list.html'
class Accesorio(ListView):
    model = Accesorios
    template_name = 'Appfinal/accesorios_list.html'
class Botin(ListView):
    model = Botines
    template_name = 'Appfinal/botines_list.html'

#detail
class Zapatilla(DetailView):
    model = ZapatillasDeportivas
    template_name = 'Appfinal/zapatillas_detail.html'
class Botines(DetailView):
    model = Botines
    template_name = 'Appfinal/botines_detail.html'

class Remeras(DetailView):
    model = Remeras
    template_name = 'Appfinal/remeras_detail.html'

class Pantalones(DetailView):
    model = Pantalones
    template_name = 'Appfinal/pantalones_detail.html'

class Accesorios(DetailView):
    model = Accesorios
    template_name = 'Appfinal/accesorios_detail.html'


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'Appfinal/confirmacionRegistro.html', {"mesanje": f'Felicitaciones, su usuario: {username} ha sido creado exitosamente, toque el boton para iniciar sesion.' })
    else:
        form = UserRegisterForm()

    return render(request, 'Appfinal/register.html', {"form":form})

def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password = contra)

            if user is not None:
                login(request, user)
                return render(request,'Appfinal/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render (request, 'Appfinal/inicio.html', {'mensaje': 'Los datos ingresados no son validos'})


        else:
            return render(request, 'Appfinal/inicio.html', {'mensaje':'Formulario erroneo'})

    form = AuthenticationForm() #Formulario vacio para hacer el login
    return render(request, "Appfinal/login.html", {"form":form})



