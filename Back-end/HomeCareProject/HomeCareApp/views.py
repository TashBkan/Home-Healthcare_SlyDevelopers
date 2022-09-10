import email
import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError

from .models import Paciente, Medico

def home(request):
    return HttpResponse("Tu cuidado nuestro compromiso")

# ---------------------------------------------------------------
# Paciente
# ---------------------------------------------------------------

def newPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paciente = Paciente(
                id = data["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                fechaNacimiento = data["fechaNacimiento"],
                genero = data["genero"],
                direccion = data["direccion"],
                longitud = data["longitud"],
                latitud = data["latitud"],
                telefono = data["telefono"],
                ciudad = data["ciudad"],
                email = data["email"]
            )        
            paciente.save()
            return HttpResponse("Paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getAllPacientes(request):
    if request.method == 'GET':
        try:
            pacientes = Paciente.objects.all()
            if (not pacientes):
                return HttpResponseBadRequest("No existen pacientes registrados")
            allPaciData = []
            for paci in pacientes:
                data = {
                    "id": paci.id,
                    "nombres": paci.nombres,
                    "Apellidos": paci.apellidos,
                    "fecha de nacimiento": paci.fechaNacimiento,
                    "genero": paci.genero,
                    "direccion": paci.direccion,
                    "longitud": paci.longitud,
                    "latitud": paci.latitud,
                    "telefono": paci.telefono,
                    "ciudad": paci.ciudad,
                    "Email": paci.email
                }
                allPaciData.append(data)
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(allPaciData)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getOnePaciente(request, id):
    if request.method == 'GET':
        try:
            paci = Paciente.objects.filter(id = id).first()
            if (not paci):
                return HttpResponseBadRequest("No existe un paciente con ese documento")

            data = {
                "id": paci.id,
                    "nombres": paci.nombres,
                    "Apellidos": paci.apellidos,
                    "fecha de nacimiento": paci.fechaNacimiento,
                    "genero": paci.genero,
                    "direccion": paci.direccion,
                    "longitud": paci.longitud,
                    "latitud": paci.latitud,
                    "telefono": paci.telefono,
                    "ciudad": paci.ciudad,
                    "Email": paci.email
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
        
def updatePaciente(request, id):
    if request.method == 'PUT':
        try:
            paci = Paciente.objects.filter(id = id).first()
            if (not paci):
                return HttpResponseBadRequest("No existe un paciente con ese documento")
            data = json.loads(request.body)
            paci.nombres = data["nombres"],
            paci.apellidos = data["apellidos"],
            paci.fechaNacimiento = data["fechaNacimiento"],
            paci.genero = data["genero"],
            paci.direccion = data["direccion"],
            paci.longitud = data["longitud"],
            paci.latitud = data["latitud"],
            paci.telefono = data["telefono"],
            paci.ciudad = data["ciudad"],
            paci.email = data["email"]
            paci.save()
            return HttpResponse("Paciente actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def deletePaciente(request, id):
    if request.method == 'DELETE':
        try:
            paci = Paciente.objects.filter(id = id).first()
            if (not paci):
                return HttpResponseBadRequest("No existe un paciente con ese documento")
            paci.delete()
            return HttpResponse("Paciente eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

# ---------------------------------------------------------------
# Medico
# ---------------------------------------------------------------

def newMedico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            medico = Medico(
                id = data["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                genero = data["genero"],
                telefono = data["telefono"],
                registroMedico = data["registroMedico"],
                especialidad = data["especialidad"],
                pacienteId = data["pacienteId"]
            )        
            medico.save()
            return HttpResponse("Medico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getAllMedicos(request):
    if request.method == 'GET':
        try:
            medicos = Medico.objects.all()
            if (not medicos):
                return HttpResponseBadRequest("No existen medicos registrados")
            allMediData = []
            for medi in medicos:
                data = {
                    "id": medi.id,
                    "nombres": medi.nombres,
                    "Apellidos": medi.apellidos,
                    "genero": medi.genero,
                    "telefono": medi.telefono,
                    "resgistroMedico": medi.resgistroMedico,
                    "especialidad": medi.especialidad,
                    "pacienteId": medi.pacienteId
                }
                allMediData.append(data)
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(allMediData)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getOneMedico(request, id):
    if request.method == 'GET':
        try:
            medi = Medico.objects.filter(id = id).first()
            if (not medi):
                return HttpResponseBadRequest("No existe un medico con ese id")

            data = {
                "id": medi.id,
                    "nombres": medi.nombres,
                    "Apellidos": medi.apellidos,
                    "genero": medi.genero,
                    "telefono": medi.telefono,
                    "resgistroMedico": medi.resgistroMedico,
                    "especialidad": medi.especialidad,
                    "pacienteId": medi.pacienteId
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
        
def updateMedico(request, id):
    if request.method == 'PUT':
        try:
            medi = Medico.objects.filter(id = id).first()
            if (not medi):
                return HttpResponseBadRequest("No existe un medico con ese documento")
            data = json.loads(request.body)
            medi.nombres = data["nombres"],
            medi.apellidos = data["apellidos"],
            medi.genero = data["genero"],
            medi.telefono = data["telefono"],
            medi.registroMedico = data["registroMedico"],
            medi.especialidad = data["especialidad"],
            medi.pacienteId = data["pacienteId"]
            medi.save()
            return HttpResponse("Medico actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def deleteMedico(request, id):
    if request.method == 'DELETE':
        try:
            medi = Medico.objects.filter(id = id).first()
            if (not medi):
                return HttpResponseBadRequest("No existe un medico con ese documento")
            medi.delete()
            return HttpResponse("Medico eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")