from django.db import models
from .pacienteModels import Paciente

class HistoriaClinica(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, serialize=True)
    diagnosticos = models.CharField(max_length=30)
    signos = models.CharField(max_length=30)
    oximetria = models.CharField(max_length=30)
    frecRespiratoria = models.CharField(max_length=30)
    frecCardiaca = models.CharField(max_length=30)
    temperatura = models.CharField(max_length=30)
    presionArterial = models.CharField(max_length=30)
    glicemias = models.CharField(max_length=30)
    sugerencias_cuidado = models.CharField(max_length=300)
    pacienteId = models.ForeignKey(Paciente, related_name='historiaClinica', on_delete=models.CASCADE)
