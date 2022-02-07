
from rest_framework import serializers

from loadImage.models import ImagenModelo
from loadImage.models import ImagenSave

class ImagenTablaSerializer(serializers.ModelSerializer):
    class Meta :
        model = ImagenModelo
        fields = ('__all__')

class ImagenSerializer(serializers.ModelSerializer):
    class Meta :
        model = ImagenSave
        fields = ('__all__')