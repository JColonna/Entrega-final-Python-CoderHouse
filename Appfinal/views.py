from django.forms.forms import Form
from django.shortcuts import render
from Appfinal import forms
from Appfinal.models import Avatar, FormularioContacto, Accesorios, ZapatillasDeportivas,Pantalones,Botines,Remeras
from Appfinal.forms import FormularioContact, AvatarFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from Appfinal.forms import UserRegisterForm
from django. contrib.auth.decorators import login_required
from Appfinal.models import Indumentaria
from Appfinal.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.models import User

# Create your views here.
def nosotros(request):
    return render(request,'Appfinal/nosotros.html')
def index(request):
       
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
    
    
        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url

    #return HttpResponse("Esto es una prueba del inicio")
  

    return render(request, 'Appfinal/padre.html', diccionario)

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
class ZapatillasList(ListView):
    model = ZapatillasDeportivas
    template_name = 'Appfinal/zapatillas_list.html'
class PantalonesList(ListView):
    model = Pantalones
    template_name = 'Appfinal/pantalones_list.html'
class RemerasList(ListView):
    model = Remeras
    template_name = 'Appfinal/remeras_list.html'
class AccesoriosList(ListView):
    model = Accesorios
    template_name = 'Appfinal/accesorios_list.html'
class BotinesList(ListView):
    model = Botines
    template_name = 'Appfinal/botines_list.html'

#detail
class ZapatillasDetalle(DetailView):
    model = ZapatillasDeportivas
    template_name = 'Appfinal/zapatillas_detail.html'
class BotinesDetalle(DetailView):
    model = Botines
    template_name = 'Appfinal/botines_detail.html'

class RemerasDetalle(DetailView):
    model = Remeras
    template_name = 'Appfinal/remeras_detail.html'

class PantalonesDetalle(DetailView):
    model = Pantalones
    template_name = 'Appfinal/pantalones_detail.html'

class AccesoriosDetalle(DetailView):
    model = Accesorios
    template_name = 'Appfinal/accesorios_detail.html'

#Crear 
class AccesorioCreate(CreateView):

    model = Accesorios
    success_url = "../Appfinal/accesorios/list"
    fields = ['tipo','talle', 'stock', 'precio']

class RemeraCreate(CreateView):

    model = Remeras
    success_url = "../Appfinal/remeras/list"
    fields = ['tipo','talle', 'stock', 'precio'] 
class PantalonCreate(CreateView):

    model = Pantalones
    success_url = "../Appfinal/pantalones/list"
    fields = ['tipo','talle', 'stock', 'precio'] 
class BotinCreate(CreateView):

    model = Botines
    success_url = "../Appfinal/botines/list"
    fields = ['tipo','talle', 'stock', 'precio'] 
class ZapatillaCreate(CreateView):

    model = ZapatillasDeportivas
    success_url = "../Appfinal/zapatillas/list"
    fields = ['tipo','talle', 'stock', 'precio']  

#Editar
class AccesoriosUpdate(UpdateView):

      model = Accesorios
      success_url = "../accesorios/list"
      fields = ['tipo','talle', 'stock', 'precio'] 
class ZapatillasUpdate(UpdateView):

      model = ZapatillasDeportivas
      success_url = "../zapatillas/list"
      fields = ['tipo','talle', 'stock', 'precio'] 
class BotinesUpdate(UpdateView):

      model = Botines
      success_url = "../botines/list"
      fields = ['tipo','talle', 'stock', 'precio'] 
class PantalonesUpdate(UpdateView):

      model = Pantalones
      success_url = "../pantalones/list"
      fields = ['tipo','talle', 'stock', 'precio'] 
class RemerasUpdate(UpdateView):

      model = Remeras
      success_url = "../remeras/list"
      fields = ['tipo','talle', 'stock', 'precio'] 

#Eliminar

class AccesoriosDelete(DeleteView):

      model = Accesorios
      success_url = "../accesorios/list"
class ZapatillasDelete(DeleteView):

      model = ZapatillasDeportivas
      success_url = "../zapatillas/list"
class RemerasDelete(DeleteView):

      model = Remeras
      success_url = "../remeras/list"
class BotinesDelete(DeleteView):

      model = Botines
      success_url = "../botines/list"
class PantalonesDelete(DeleteView):

      model = Pantalones
      success_url = "../pantalones/list"

#Login edit y register 
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
@login_required
def editarPerfil(request):

   usuario= request.user

   if request.method == "POST":

      miFormulario= UserEditForm(request.POST)  

      if miFormulario.is_valid():

         informacion= miFormulario.cleaned_data

         usuario.email= informacion["email"] 
         usuario.password1= informacion["password1"]
         usuario.password2= informacion["password2"]
         usuario.last_name= informacion["last_name"]
         usuario.first_name= informacion["first_name"]

         usuario.save()

         return render(request, "Appfinal/inicio.html")

   else:
      miFormulario= UserEditForm(initial={"email":usuario.email})  

   return render (request, "Appfinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario}) 

@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) 

            if miFormulario.is_valid():   


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "Appfinal/padre.html") 

      else: 

            miFormulario= AvatarFormulario() 

      return render(request, "Appfinal/agregarAvatar.html", {"miFormulario":miFormulario})
