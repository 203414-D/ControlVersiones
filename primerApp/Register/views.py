from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from Register.serializers import RegisterSerializernew
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from Register.serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class RegisterUser(APIView):
    def post(self, request):
        serializer = RegisterSerializernew(data = request.data)
        if serializer.is_valid():
            print(serializer.get_fields())
            a=request.data.__getitem__('username')
            c=request.data.__getitem__('email')
            d=request.data.__getitem__('password')
            la = User.objects.create_user(a,c,d, is_staff=True,is_active=True,is_superuser=True)
            Token.objects.get_or_create(user=la)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_401_UNAUTHORIZED)

class RegisterUserNew(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class RegisterN(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
                return 404

    def put(self,request,pk,format=None):

        idResponse = self.get_object(pk)
        if idResponse != 404:
               serializer = RegisterSerializer(idResponse, data=request.data, context={'request':request})
               if serializer.is_valid():
                   serializer.save()
                   s=serializer.data
                   return Response(s,status.HTTP_200_OK)
               else:
                   se=serializer.errors
                   return Response(se,status.HTTP_400_BAD_REQUEST)
        else:
            se="id not found"
            return Response(se,status.HTTP_404_NOT_FOUND)
