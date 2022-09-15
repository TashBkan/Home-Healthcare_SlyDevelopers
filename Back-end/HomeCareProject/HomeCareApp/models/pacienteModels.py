from django.db import models

class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, serialize=True)
    rol = models.TextField('Rol', max_length=20, default='paciente')
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fechaNacimiento = models.CharField(max_length=30, null=True)
    genero = models.CharField(max_length=30, null=True)
    direccion = models.CharField(max_length=50, null=True)
    longitud = models.CharField(max_length=50, null=True)
    latitud = models.CharField(max_length=50, null=True)
    telefono = models.BigIntegerField()
    ciudad = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.rol},{self.username},{self.password},{self.nombres},{self.apellidos},{self.telefono},{self.genero}'