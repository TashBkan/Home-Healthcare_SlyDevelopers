from django.contrib import admin
from .models.userModels import User
from .models.pacienteModels import Paciente
from .models.medicoModels import Medico

admin.site.register(User)
admin.site.register(Paciente)
admin.site.register(Medico)

# Register your models here.
