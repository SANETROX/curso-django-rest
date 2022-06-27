from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models, permissions


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

class HelloViewSet(viewsets.ViewSet):
    """
    Test API VIEW SET, trae ciertos metodos para crear logica mas simple,
     crud y operaciones basicas con DB
     Corrers funciones list(), retrieve, entre otras
    """
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Retorna una lista de objetos"""
        a_viewset = [
            "Usa acciones (list, create, retrieve, update, partial_update)",
            "Automaticamente mapea a los URLS usando Routers",
            "Provee mas funcionalidad con menos codigo"
        ]

        return Response({"message":"Hello from viewset", "a_viewset":a_viewset})
    
    def create(self, request):
        """Crear nuevo objeto"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hola {name} desde create viewset"
            return Response({"message":message})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Obtiene un objeto y su ID"""
        return Response({"message":"Retrieve object successfully", "http_method":"GET"})
    
    def update(self, request, pk=None):
        """actualiza un objeto"""
        return Response({"message":"Update object successfully", "http_method":"PUT"})
    
    def partial_update(self, request, pk=None):
        """actualiza parcialmente un objeto"""
        return Response({"message":"Update object successfully", "http_method":"PATCH"})
    
    def destroy(self, request, pk=None):
        """Destruye un objeto"""
        return Response({"message":"Destroy object successfully", "http_method":"DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """
        Crear y actualizar perfiles, ModelViewset esta disenado para manejar por api los Modelos
        que definamos
    """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)