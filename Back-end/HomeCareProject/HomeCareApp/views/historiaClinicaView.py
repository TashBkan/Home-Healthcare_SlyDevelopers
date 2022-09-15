from django.conf import settings
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from HomeCareApp.models.historiClinicaModels import HistoriaClinica
from HomeCareApp.serializers.historiaClinicaSerializer import HistoriaClinicaSerializer

class CreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = HistoriaClinicaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class GetView(generics.RetrieveAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
  
        return super().get(request, *args, **kwargs)
"""
class DeleteView(generics.RetrieveAPIView):
    
    def delete(self, request, *args, **kwargs):
    
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
"""