from django.conf import settings
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from homeCareApp.models.enfermeroModels import Enfermero
from homeCareApp.serializers.enfermeroSerializer import EnfermeroSerializer
from homeCareApp.serializers.userSerializer import UserSerializer

class CreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = EnfermeroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializerUser = UserSerializer(data=request.data)
        serializerUser.is_valid(raise_exception=True)
        serializerUser.save()

        tokenData = {"username":request.data["username"], "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

class GetView(generics.RetrieveAPIView):
    queryset = Enfermero.objects.all()
    serializer_class = EnfermeroSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        return super().get(request, *args, **kwargs)

