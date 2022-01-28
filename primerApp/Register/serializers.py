from rest_framework import serializers

from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email',)
        Write_only_fields = ('password',)
        read_only_fields = ('id',)

    def crear(self, validated_data):
        user=User()
        user.objects.create( username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validar_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError('Nombre de usuario ya existente')
        else: 
            return data

     