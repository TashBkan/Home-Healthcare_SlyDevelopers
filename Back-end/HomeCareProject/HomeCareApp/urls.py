from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('paciente/new', views.newPaciente, name='newPaciente'),
    path('paciente/read', views.getAllPacientes, name='getAllPacientes'),
    path('paciente/read/<int:id>', views.getOnePaciente, name='getOnePaciente'),
    path('paciente/update/<int:id>', views.updatePaciente, name='updatePaciente'),
    path('paciente/delete/<int:id>', views.deletePaciente, name='deletePaciente'),
    path('medico/new', views.newMedico, name='newMedico'),
    path('medico/read', views.getAllMedicos, name='getAllMedicos'),
    path('medico/read/<int:id>', views.getOneMedico, name='getOneMedico'),
    path('medico/update/<int:id>', views.updateMedico, name='updateMedico'),
    path('medico/delete/<int:id>', views.deleteMedico, name='deleteMedico'),
]