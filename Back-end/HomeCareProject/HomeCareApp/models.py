from django.db import models

class Paciente(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    genero = models.CharField(max_length=30, null=True)
    direccion = models.CharField(max_length=50, null=True)
    longitud = models.CharField(max_length=50, null=True)
    latitud = models.CharField(max_length=50, null=True)
    telefono = models.BigIntegerField(null=True)
    ciudad = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    
    
class Medico(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=30,null=True)
    telefono = models.BigIntegerField(null=True)
    registroMedico = models.CharField (max_length=50)
    especialidad = models.CharField (max_length=50)
    pacienteId = models.ForeignKey(Paciente, related_name='medico', on_delete=models.CASCADE)

class Enfermero(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=30,null=True)
    telefono = models.BigIntegerField(null=True)
    pacienteId = models.ForeignKey(Paciente, related_name='enfermero', on_delete=models.CASCADE)
    
class Auxiliar(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=30,null=True)
    telefono = models.BigIntegerField(null=True)
    pacienteId = models.ForeignKey(Paciente, related_name='auxiliar', on_delete=models.CASCADE)
    
class Acompañante(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=30,null=True)
    telefono = models.BigIntegerField(null=True)
    email = models.EmailField(max_length=100, unique=True)
    pacienteId = models.ForeignKey(Paciente, related_name='acompañante', on_delete=models.CASCADE)
    
class Historia_clinica(models.Model):
    id = models.AutoField(primary_key=True)
    diagnosticos = models.CharField(max_length=30)
    signos = models.CharField(max_length=30)
    oximetria = models.CharField(max_length=30)
    FrecRespiratoria = models.CharField(max_length=30)
    FrecCardiaca = models.CharField(max_length=30)
    Temperatura = models.CharField(max_length=30)
    presionArterial = models.CharField(max_length=30)
    glicemias = models.CharField(max_length=30)
    sugerencias_cuidado = models.CharField(max_length=300)
    pacienteId = models.ForeignKey(Paciente, related_name='historia_clinica', on_delete=models.CASCADE)
