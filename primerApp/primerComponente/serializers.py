from rest_framework import serializers

#importacion de modelos
from primerComponente.models import PrimerModelo
#importacion de serializador
class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta : 
        model = PrimerModelo
        fields = ('__all__')
