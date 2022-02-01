from ast import Delete
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#importacion de modelos
from primerComponente.models import PrimerModelo

#importacion de serializador
from primerComponente.serializers import PrimerTablaSerializer

class responseA(APIView):
    def response_custom(message="", payload="", statusn=""):
        return{
            "message": message,
            "payload": payload,
            "status": statusn
        }

class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer=PrimerTablaSerializer(querySet,many=True ,context={'request':request})
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = PrimerTablaSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            s=serializer.data
            mensok="success"
            
            return Response(responseA.response_custom(mensok,s,status.HTTP_201_CREATED))
        else:
            menserr="error"
            se=serializer.errors
            return Response(responseA.response_custom(menserr,se,status.HTTP_400_BAD_REQUEST))


class PrimerViewDetail(APIView):

    def get_object(self, pk):
        try:
            return PrimerModelo.objects.get(pk=pk)
        except PrimerModelo.DoesNotExist:
                return 404

    def get(self,request,pk,format=None):
        ##serializer = PrimerTablaSerializer(data=request.data, context={'request':request})
        idResponse = self.get_object(pk)
        if idResponse != 404:
             serializer = PrimerTablaSerializer(idResponse, context={'request':request})
             s=serializer.data
             mensok="success"
             return Response(responseA.response_custom(mensok,s,status.HTTP_200_OK))
        else:
            menserr="id no encontrado"
            se=idResponse
            return Response(responseA.response_custom(menserr,se,status.HTTP_404_NOT_FOUND))

    def put(self,request,pk,format=None):

        idResponse = self.get_object(pk)
        if idResponse != 404:
               serializer = PrimerTablaSerializer(idResponse, data=request.data, context={'request':request})
               if serializer.is_valid():
                   serializer.save()
                   s=serializer.data
                   mensok="success"
                   return Response(responseA.response_custom(mensok,s,status.HTTP_200_OK))
               else:
                   menserr="error"
                   se=serializer.errors
                   return Response(responseA.response_custom(menserr,se,status.HTTP_400_BAD_REQUEST))
        else:
            menserr="id no encontrado"
            se=idResponse
            return Response(responseA.response_custom(menserr,se,status.HTTP_404_NOT_FOUND))

    def delete(self,request,pk,format=None):
        idResponse = get_object_or_404(PrimerModelo, pk=pk)
        if idResponse != 404:
             idResponse.delete()
             mensok="success"
             return Response(responseA.response_custom(mensok,"",status.HTTP_200_OK))
        else:
            menserr="id no encontrado"
            se=idResponse
            return Response(responseA.response_custom(menserr,se,status.HTTP_404_NOT_FOUND))
        
            


