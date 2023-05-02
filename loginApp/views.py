from __future__ import print_function
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Usuario
from .serializers import UsuarioSerializer


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)

class UsuariosDetails(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        token = request.data.get('token', '')
        if(token != 'f82779ddfbf8ccd5f1d48cc4986fd2d9'):
            return Response(email, status=status.HTTP_401_NOT_FOUND)
        
        usuario = Usuario.objects.filter(mail=email, contrasena=password).first()
        serializer = UsuarioSerializer(usuario)
            
        if usuario:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(email, status=status.HTTP_404_NOT_FOUND)