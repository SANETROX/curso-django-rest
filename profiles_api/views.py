from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

from profiles_api import serializers


class HelloApi(APIView):
    """
    Helol APIView de prueba
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            "Usamos como metodos http como funciones (get, post, put, patch, delete)",
            "Es similar a una vista en Django",
            "Nos da el mayor control sobrer la logica de nustra aplicacion",
            "Esta mapeado manualmente a los URLs"
        ]

        return Response({"message":"Hello fom django Rest", "api_response":an_apiview})

    def post(self, request):
        """Crea un mensaje de nuestro nombre utlizando serializers"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Maneja actualizar el objeto"""
        return Response({"message":"Update Successfully"})
    
    def patch(self, request, pk=None):
        """Maneja actualizacion parcial del objeto"""
        return Response({"message":"Patch object Successfully"})
    
    def delete(self, request, pk=None):
        return Response({"message":"Delete object successfully"})