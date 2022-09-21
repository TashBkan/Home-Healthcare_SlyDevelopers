from rest_framework import serializers
from homeCareApp.models.auxiliarModels import Auxiliar

class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = ['id', 'rol', 'username', 'password', 'nombres', 'apellidos', 'genero', 'telefono', 'pacienteId']

    def create(self, validated_data):
        medicoInstance = Auxiliar.objects.create(**validated_data)
        return medicoInstance
    
    def to_representation(self, obj):
        aux = Auxiliar.objects.get(id = obj.id)
        return {
                    "id": aux.id,
                    "username": aux.username,
                    "nombres": aux.nombres,
                    "apellidos": aux.apellidos,
                    "genero": aux.genero,
                    "telefono": aux.telefono,
                    "pacienteId": aux.pacienteId
        }