from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
   email = serializers.EmailField(
           required=True,
           validators=[UniqueValidator(queryset=User.objects.all())]
           )
 
   password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
   password2 = serializers.CharField(write_only=True, required=False)
 
   class Meta:
       model = User
       fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
       extra_kwargs = {
           'first_name': {'required': True},
           'last_name': {'required': True}
       }
 
   ##def validate(self, attrs):
  ##     if attrs['password'] != attrs['password2']:
   ##        raise serializers.ValidationError({"password": "Password error"})
 
   ##    return attrs
 
   def create(self, validated_data):
       user = User.objects.create(
           username=validated_data['username'],
           email=validated_data['email'],
           first_name=validated_data['first_name'],
           last_name=validated_data['last_name']
       )
 
      
       user.set_password(validated_data['password'])
       user.save()
 
       return user


class RegisterSerializernew(serializers.ModelSerializer):
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

     


     