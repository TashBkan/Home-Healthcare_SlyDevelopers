from rest_framework import serializers
from HomeCareApp.models.medicoModels import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'rol', 'username', 'password', 'nombres', 'apellidos', 'genero', 'telefono', 'registroMedico', 'especialidad', 'pacienteId']

    def create(self, validated_data):
        medicoInstance = Medico.objects.create(**validated_data)
        return medicoInstance
    
    def to_representation(self, obj):
        medi = Medico.objects.get(id = obj.id)
        return {
                    "id": medi.id,
                    "username": medi.username,
                    "nombres": medi.nombres,
                    "apellidos": medi.apellidos,
                    "genero": medi.genero,
                    "telefono": medi.telefono,
                    "resgistroMedico": medi.resgistroMedico,
                    "especialidad": medi.especialidad,
                    "pacienteId": medi.pacienteId
        }