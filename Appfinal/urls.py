
from django.urls import path
from Appfinal import views
from Appfinal.views import TiendaVirtual, ZapatillasDeportivas, Pantalones, Remeras, Botines,Accesorios
from  Appfinal.views import register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index', views.index, name='Index'),
    path('contacto', views.formularioContacto, name='Contacto'),
    path('confirmacion', views.confirmacionContacto, name='Confirmacion'),
    path('tiendavirtual/list', views.TiendaVirtual.as_view(), name="List"),
    path(r'^(?P<pk>\d+)$', views.ZapatillasDeportivas.as_view(), name='Zapatillas'),
    path(r'^(?P<pk>\d+)$', views.Pantalones.as_view(), name='Pantalones'),
    path(r'^(?P<pk>\d+)$', views.Remeras.as_view(), name='Remeras'),
    path(r'^(?P<pk>\d+)$', views.Botines.as_view(), name='Botines'),
    path(r'^(?P<pk>\d+)$', views.Accesorios.as_view(), name='Accesorios'),
    path('register', views.register, name='Register' ),
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name="Appfinal/logout.html"), name="Logout"),
    

]