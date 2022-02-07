

import json
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from PIL import Image
import os



#importacion de serializador
from loadImage.serializers import ImagenTablaSerializer

#importacion de modelo
from loadImage.models import ImagenModelo

#importacion response custom
from primerComponente.views import responseA


class ImagenView(APIView):
    def get(self, request, format=None):
        querySet = ImagenModelo.objects.all()
        serializer = ImagenTablaSerializer(querySet,many = True, context={'request':request})
        s=serializer.data
        mensok="success"
        return Response(responseA.response_custom(mensok,s,status.HTTP_200_OK))

    def post(self,request, format=None):
        image_path = settings.MEDIA_ROOT
        a=request.data.__getitem__('image')
        c=request.data.__getitem__('format')
        d=request.data.__getitem__('title')
        im = Image.open(a)
        im.save(f"{image_path}/"+d+c)
        request2 ={
            "name_img": d,
            "url_img": "http://localhost:8000/assets/img/"+d+c,
            "format_img": c,
        }
        res = json.dumps(request2)
        res2 = json.loads(res)
        serializer = ImagenTablaSerializer(data= res2)
        if serializer.is_valid():
            serializer.save()
            s=serializer.data
            mensok="success"
            return Response(responseA.response_custom(mensok,s,status.HTTP_201_CREATED))
        else:
            menserr="error"
            se=serializer.errors
            return Response(responseA.response_custom(menserr,se,status.HTTP_400_BAD_REQUEST))

class ImagenViewDetail(APIView):

    def get_objetc(self, pk):
         try:
            return ImagenModelo.objects.get(pk=pk)
         except ImagenModelo.DoesNotExist:
                return 404

    def get(self, request, pk, format=None):

        idresponse = self.get_objetc(pk)
        if idresponse !=404:
            serializer = ImagenTablaSerializer(idresponse, context={'request':request})
            s=serializer.data
            mensok="success"
            return Response(responseA.response_custom(mensok,s,status.HTTP_200_OK))
        else:
            menserr="Error"
            se="id not found"
            return Response(responseA.response_custom(menserr,se,status.HTTP_404_NOT_FOUND))

    def put(self,request,pk,format=None):

        idResponse = self.get_objetc(pk)
        if idResponse != 404:
            serializer = ImagenTablaSerializer(idResponse, data = request.data, context={'request':request})
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
             menserr="error"
             se="id not found"
             return Response(responseA.response_custom(menserr,se,status.HTTP_404_NOT_FOUND))
    
    def delete(self,request,pk,format=None):
        idresponse = get_object_or_404(ImagenModelo, pk=pk)
        if idresponse !=404:
            idresponse.delete()
            mensok="success"
            return Response(responseA.response_custom(mensok,"",status.HTTP_200_OK))
        else:
            menserr="error"
            se="id not found"
            return Response(responseA.response_custom(menserr,se,status.HTTP_404_NOT_FOUND))



