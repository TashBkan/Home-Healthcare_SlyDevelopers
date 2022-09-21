from rest_framework import serializers
from homeCareApp.models.acompañanteModels import Acompañante

class AcompañanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acompañante
        fields = ['id', 'rol', 'username', 'password', 'nombres', 'apellidos', 'genero', 'telefono', 'email', 'pacienteId']

    def create(self, validated_data):
        acompañanteInstance = Acompañante.objects.create(**validated_data)
        return acompañanteInstance
    
    def to_representation(self, obj):
        acom = Acompañante.objects.get(id = obj.id)
        return {
                    "id": acom.id,
                    "username": acom.username,
                    "nombres": acom.nombres,
                    "apellidos": acom.apellidos,
                    "genero": acom.genero,
                    "telefono": acom.telefono,
                    "email": acom.email,
                    "pacienteId": acom.pacienteId
        }