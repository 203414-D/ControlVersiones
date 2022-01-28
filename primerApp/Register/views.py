from rest_framework.response import Response
from Register.serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status


class RegisterUser(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_401_UNAUTHORIZED)
