from rest_framework import serializers
from HomeCareApp.models.userModels import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'rol', 'username', 'password', 'nombres', 'apellidos', 'genero', 'telefono']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id = obj.id)
        return {
                    "id": user.id,
                    "rol": user.rol,
                    "username": user.username,
                    "nombres": user.nombres,
                    "apellidos": user.apellidos,
                    "genero": user.genero,
                    "telefono": user.telefono
        }