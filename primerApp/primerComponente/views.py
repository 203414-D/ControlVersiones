from rest_framework.views import APIView
from rest_framework.response import Response

#importacion de modelos
from primerComponente.models import PrimerModelo

#importacion de serializador
from primerComponente.serializers import PrimerTablaSerializer

class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer=PrimerTablaSerializer(querySet,many=True ,context={'request':request})
        return Response(serializer.data)