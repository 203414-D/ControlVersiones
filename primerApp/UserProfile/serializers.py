from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from UserProfile.models import ProfileTabla

class ProfileTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileTabla
        fields = ('user_id', 'url_img')