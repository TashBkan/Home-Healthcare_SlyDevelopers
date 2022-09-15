from django.db import models
from .pacienteModels import Paciente

class Medico(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, serialize=True)
    rol = models.TextField('Rol', max_length=20, default='medico')
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=30,null=True)
    telefono = models.BigIntegerField()
    registroMedico = models.CharField (max_length=50)
    especialidad = models.CharField (max_length=50)
    pacienteId = models.ForeignKey(Paciente, related_name='medico', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.rol},{self.username},{self.password},{self.nombres},{self.apellidos},{self.telefono},{self.genero}'