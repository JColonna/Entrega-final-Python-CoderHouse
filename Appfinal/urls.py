
from django.urls import path
from Appfinal import views
from Appfinal.views import  Zapatilla, Zapatillas, ZapatillasDeportivas, Pantalones, Remeras, Botines,Accesorios, tiendaVirtual
from  Appfinal.views import register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index', views.index, name='Index'),
    path('contacto', views.formularioContacto, name='Contacto'),
    path('confirmacion', views.confirmacionContacto, name='Confirmacion'),
    path('tiendavirtual', views.tiendaVirtual, name="Tienda"),
    path('zapatillas/list', views.Zapatillas.as_view(), name="ListZapas"),
    path('botines/list', views.Botin.as_view(), name="ListBot"),
    path('remeras/list', views.Remera.as_view(), name="ListRem"),
    path('pantalones/list', views.Pantalon.as_view(), name="ListPan"),
    path('accesorios/list', views.Accesorio.as_view(), name="ListAcc"),
    path(r'^(?P<pk>\d+)$', views.Zapatilla.as_view(), name='Zapatillas'),
    path(r'^(?P<pk>\d+)$', views.Pantalones.as_view(), name='Pantalones'),
    path(r'^(?P<pk>\d+)$', views.Remeras.as_view(), name='Remeras'),
    path(r'^(?P<pk>\d+)$', views.Botines.as_view(), name='Botines'),
    path(r'^(?P<pk>\d+)$', views.Accesorios.as_view(), name='Accesorios'),
    path('register', views.register, name='Register' ),
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name="Appfinal/logout.html"), name="Logout"),
    

]