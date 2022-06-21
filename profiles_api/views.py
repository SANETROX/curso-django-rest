from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApi(APIView):
    """
    Helol APIView de prueba
    """
    def get(self, request, format=None):
        an_apiview = [
            "Usamos como metodos http como funciones (get, post, put, patch, delete)",
            "Es similar a una vista en Django",
            "Nos da el mayor control sobrer la logica de nustra aplicacion",
            "Esta mapeado manualmente a los URLs"
        ]

        return Response({"message":"Hello fom django Rest", "api_response":an_apiview})
