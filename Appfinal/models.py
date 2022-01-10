from django.db import models


# Create your models here.

class FormularioContacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    consulta = models.CharField(max_length=200)
    def __str__(self):
        return (f'Nombre: {self.nombre},Apellido: {self.apellido}, Email: {self.email}, Telefono: {self.telefono}, Consulta: {self.consulta}')
    
class Indumentaria(models.Model):
    tipo = models.CharField(max_length=40)
    def __str__(self):
        return(f'{self.tipo}')

class Pantalones(models.Model):
    tipo = models.CharField(max_length=40)
    talle = models.IntegerField()
    stock = models.BooleanField()
    precio = models.IntegerField()
    def __str__(self):
        return(f'{self.tipo}, {self.talle}, {self.stock}, {self.precio}')
class Remeras(models.Model):
    tipo = models.CharField(max_length=40)
    talle = models.IntegerField()
    stock = models.BooleanField()
    precio = models.IntegerField()
    def __str__(self):
        return(f'{self.tipo}, {self.talle}, {self.stock}, {self.precio}')

class ZapatillasDeportivas(models.Model):
    tipo = models.CharField(max_length=40)
    talle = models.IntegerField()
    stock = models.BooleanField()
    precio = models.IntegerField()
    def __str__(self):
        return(f'{self.tipo}, {self.talle}, {self.stock}, {self.precio}')
class Botines(models.Model):
    tipo = models.CharField(max_length=40)
    talle = models.IntegerField()
    stock = models.BooleanField()
    precio = models.IntegerField()
    def __str__(self):
        return(f'{self.tipo}, {self.talle}, {self.stock}, {self.precio}')
class Accesorios(models.Model):
    tipo = models.CharField(max_length=40)
    talle = models.IntegerField()
    stock = models.BooleanField()
    precio = models.IntegerField()
    def __str__(self):
        return(f'{self.tipo}, {self.talle}, {self.stock}, {self.precio}')
 


