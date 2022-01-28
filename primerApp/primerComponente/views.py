from ast import Delete
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#importacion de modelos
from primerComponente.models import PrimerModelo

#importacion de serializador
from primerComponente.serializers import PrimerTablaSerializer

class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer=PrimerTablaSerializer(querySet,many=True ,context={'request':request})
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = PrimerTablaSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PrimerViewDetail(APIView):

    def get_object(self, pk):
        try:
            return PrimerModelo.objects.get(pk=pk)
        except PrimerModelo.DoesNotExist:
                return 404

    def get(self,request,pk,format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
             serializer = PrimerTablaSerializer(idResponse, context={'request':request})
             return Response(serializer.data, status = status.HTTP_200_OK)
        else:
             return Response('no encontrado', status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
               serializer = PrimerTablaSerializer(idResponse, data=request.data, context={'request':request})
               if serializer.is_valid():
                   serializer.save()
                   return Response(serializer.data, status = status.HTTP_200_OK)
               else:
                    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response('id no encontrado', status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        idResponse = get_object_or_404(PrimerModelo, pk=pk)
        if idResponse != 404:
             idResponse.delete()
             return Response('borrado con exito', status=status.HTTP_200_OK)
        else:
             return Response('id no encontrado', status = status.HTTP_400_BAD_REQUEST)
        
            


