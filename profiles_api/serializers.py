from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    "Serializer for HelloApiView."
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializa objeto del perfil de User"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email','name', 'password') #Campos que se quieren mostrar
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'} # con estos mostramos son asteriscos y protejemos la clave
            }
        }

        def create(self, validated_data):
            """Crear y retornar nuevo user"""
            user = models.UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password']
            )

            return user
        
        def update(self, instance, validated_data):
            """Actualiza cuenta de user"""
            if 'password' in validated_data:
                password = validated_data.pop('password')
                instance.set_password(password)
            
            return super().update(instance, validated_data)