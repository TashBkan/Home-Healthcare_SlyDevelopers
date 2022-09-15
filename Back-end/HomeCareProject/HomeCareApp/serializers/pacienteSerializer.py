from rest_framework import serializers
from HomeCareApp.models.pacienteModels import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'rol', 'username', 'password', 'nombres', 'apellidos', 'fechaNacimiento', 'genero', 'direccion', 'longitud', 'latitud', 'telefono', 'ciudad', 'email']

    def create(self, validated_data):
        pacienteInstance = Paciente.objects.create(**validated_data)
        return pacienteInstance
    
    def to_representation(self, obj):
        paci = Paciente.objects.get(id = obj.id)
        return {
                    "id": paci.id,
                    "username": paci.username,
                    "nombres": paci.nombres,
                    "apellidos": paci.apellidos,
                    "fechaNacimiento": paci.fechaNacimiento,
                    "genero": paci.genero,
                    "direccion": paci.direccion,
                    "longitud": paci.longitud,
                    "latitud": paci.latitud,
                    "telefono": paci.telefono,
                    "ciudad": paci.ciudad,
                    "email": paci.email
        }

