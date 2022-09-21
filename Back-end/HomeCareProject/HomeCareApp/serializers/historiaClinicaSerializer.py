from rest_framework import serializers
from homeCareApp.models.historiClinicaModels import HistoriaClinica

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['id', 'diagnosticos', 'signos', 'oximetria', 'frecRespiratoria', 'frecCardiaca', 'temperatura', 'presionArterial', 'glicemias', 'sugerencias_cuidado', 'pacienteId']

    def create(self, validated_data):
        historiaClinicaInstance = HistoriaClinica.objects.create(**validated_data)
        return historiaClinicaInstance
    
    def to_representation(self, obj):
        hist = HistoriaClinica.objects.get(id = obj.id)
        return {
                    "id": hist.id,
                    "diagnosticos": hist.diagnosticos,
                    "signos": hist.signos,
                    "oximetria": hist.oximetria,
                    "frecRespiratoria": hist.frecRespiratoria,
                    "frecCardiaca": hist.frecCardiaca,
                    "temperatura": hist.temperatura,
                    "presionArterial": hist.presionArterial,
                    "glicemias": hist.glicemias,
                    "sugerencias_cuidado": hist.sugerencias_cuidado,
                    "pacienteId": hist.ciudad,
        }

