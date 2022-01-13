
from django.urls import path
from Appfinal import views
from Appfinal.views import *

from  Appfinal.views import register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index', views.index, name='Index'),
    path('nosotros', views.nosotros, name='Nosotros'),
    path('contacto', views.formularioContacto, name='Contacto'),
    path('confirmacion', views.confirmacionContacto, name='Confirmacion'),
    path('tiendavirtual', views.tiendaVirtual, name="Tienda"),
    path('zapatillas/list', views.ZapatillasList.as_view(), name="ListZapas"),
    path('botines/list', views.BotinesList.as_view(), name="ListBot"),
    path('remeras/list', views.RemerasList.as_view(), name="ListRem"),
    path('pantalones/list', views.PantalonesList.as_view(), name="ListPan"),
    path('accesorios/list', views.AccesoriosList.as_view(), name="ListAcc"),
    path(r'^(?P<pk>\d+)$', views.ZapatillasDetalle.as_view(), name='Zapatillas'),
    path(r'^(?P<pk>\d1+)$', views.PantalonesDetalle.as_view(), name='Pantalones'),
    path(r'^(?P<pk>\d2+)$', views.RemerasDetalle.as_view(), name='Remeras'),
    path(r'^(?P<pk>\d3+)$', views.BotinesDetalle.as_view(), name='Botines'),
    path(r'^(?P<pk>\d4+)$', views.AccesoriosDetalle.as_view(), name='Accesorios'),
    path(r'^nuevo$', views.AccesorioCreate.as_view(), name= "NewAcces"),
    path(r'^nuevo1$', views.RemeraCreate.as_view(), name= "NewRem"),
    path(r'^nuevo2$', views.ZapatillaCreate.as_view(), name= "NewZapas"),
    path(r'^nuevo3$', views.BotinCreate.as_view(), name= "NewBotin"),
    path(r'^nuevo4$', views.PantalonCreate.as_view(), name= "NewPan"),
    path(r'^editar/(?P<pk>\d1+)$', views.AccesoriosUpdate.as_view(), name= "EditAcces"), 
    path(r'^editar/(?P<pk>\d2+)$', views.ZapatillasUpdate.as_view(), name= "EditZapas"), 
    path(r'^editar/(?P<pk>\d3+)$', views.BotinesUpdate.as_view(), name= "EditBot"), 
    path(r'^editar/(?P<pk>\d4+)$', views.RemerasUpdate.as_view(), name= "EditRem"),
    path(r'^editar/(?P<pk>\d5+)$', views.PantalonesUpdate.as_view(), name= "EditPant"),    
    path(r'^borrar/(?P<pk>\d+)$', views.AccesoriosDelete.as_view(), name= "DeleteAcces"),
    path(r'^borrar/(?P<pk>\d1+)$', views.PantalonesDelete.as_view(), name= "DeletePant"), 
    path(r'^borrar/(?P<pk>\d2+)$', views.BotinesDelete.as_view(), name= "DeleteBot"), 
    path(r'^borrar/(?P<pk>\d3+)$', views.RemerasDelete.as_view(), name= "DeleteRem"), 
    path(r'^borrar/(?P<pk>\d4+)$', views.ZapatillasDelete.as_view(), name= "DeleteZap"),  
    path('register', views.register, name='Register' ),
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name="Appfinal/logout.html"), name="Logout"),
    path('editarperfil', views.editarPerfil, name='EditarPerfil'),
    path('agregaravatar', views.agregarAvatar, name="AgregarAvatar")

    

]