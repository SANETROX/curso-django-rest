from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    "Serializer for HelloApiView."
    name = serializers.CharField(max_length=10)