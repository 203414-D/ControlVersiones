from lib2to3.pgen2.parse import ParseError
from multiprocessing import context
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions



from UserProfile.models import ProfileTabla
from UserProfile.serializers import ProfileTablaSerializer

class ProfileList(APIView):
    def get(self, request, format=None):
        queryset= ProfileTabla.objects.all()
        serializer = ProfileTablaSerializer(queryset, many= True, context= {'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "No se ha seleccionado ningun archivo")
        serializer = ProfileTablaSerializer(data=request.data)
        if serializer.is_valid():
            validated_data=serializer.validated_data
            img = ProfileTabla(**validated_data)
            img.save()
            serializer_response= ProfileTablaSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileTablaDetail(APIView):
    def get_object(self,pk):
        try:
            return ProfileTabla.objects.get(user_id=pk)
        except ProfileTabla.DoesNotExist:
            resp = "no existe"
            return resp
    
    def get(self, request, pk, fromat=None):
        idResponse = self.get_object(pk)
        val = "no existe"
        if idResponse != val:
            idResponse = ProfileTablaSerializer(idResponse)
            return Response(idResponse.data, status=status.HTTP_200_OK)
        return Response("no hay datos",  status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, fromat=None):
        idResponse= self.get_object(pk)
        serializer = ProfileTablaSerializer(idResponse, data= request.data)
        if serializer.is_valid():
            serializer.save()
            datos=serializer.data
            return Response(datos, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk,format=None):
        img= self.get_object(pk)
        vali = "no exite"
        if img != vali:
            img.url_img.delete(save=True)
            img.delete()
            return Response("archivo eliminado", status=status.HTTP_200_OK)
        return Response("Archivo no encontrado", status=status.HTTP_404_NOT_FOUND)
            
            


        

