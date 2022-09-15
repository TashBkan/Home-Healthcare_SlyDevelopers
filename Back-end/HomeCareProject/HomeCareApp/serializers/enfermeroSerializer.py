from rest_framework import serializers
from HomeCareApp.models.enfermeroModels import Enfermero


class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['id', 'rol', 'username', 'password', 'nombres', 'apellidos', 'genero', 'telefono', 'pacienteId']

    def create(self, validated_data):
        enfermeroInstance = Enfermero.objects.create(**validated_data)
        return enfermeroInstance
    
    def to_representation(self, obj):
        enfe = Enfermero.objects.get(id = obj.id)
        return {
                    "id": enfe.id,
                    "username": enfe.username,
                    "nombres": enfe.nombres,
                    "apellidos": enfe.apellidos,
                    "genero": enfe.genero,
                    "telefono": enfe.telefono,
                    "pacienteId": enfe.pacienteId
        }