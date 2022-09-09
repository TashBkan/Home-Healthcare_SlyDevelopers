import re
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from homeCareApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):

    def post(self, request, *args, **kwars):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exeption=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exeption=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

