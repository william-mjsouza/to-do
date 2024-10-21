#from django.shortcuts import render, redirect
#from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

@api_view(['GET'])  # Define que a função get_users está preparada apenas para lidar com requisições do tipo GET
def get_users(request):
    if request.method == 'GET':
        # Busca todos os usuários registrados no banco de dados (equivalente a um SELECT * FROM user; no SQL)
        users = User.objects.all()
        # Pega todos os objetos User e os converte em JSON
        serializer = UserSerializer(users, many=True)
        # Retorna os dados serializados para o cliente
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST) # Caso o método da requisição não seja GET, é retornado uma mensagem de requisição inválida

@api_view(['GET'])
# 'request' (informações sobre a requisição HTTP) e 'nick' (o nickname do usuário que está sendo procurado)
def get_by_nick(request, nick):
    # Tenta buscar um objeto 'User' no banco de dados onde a chave primária (pk) é igual ao 'nick' fornecido
    # Se encontrar, atribui o objeto 'User' à variável 'user'
    try:
        user = User.objects.get(pk=nick)  # pk é à chave primária
    except:
        # Se o Django não encontrar o 'User' com o 'nick' fornecido, ele gera uma exceção (erro)
        # Nesse caso, a exceção é tratada e retorna uma resposta HTTP com o status 404 (não encontrado)
        return Response(status=status.HTTP_404_NOT_FOUND)  
        
    if request.method == 'GET':
        # Usa o serializer 'UserSerializer' para converter o objeto 'User' (ou seja, os dados do usuário) em um formato JSON
        serializer = UserSerializer(user)  
         # Retorna uma resposta HTTP com os dados serializados (em formato JSON), que serão enviados ao cliente
        return Response(serializer.data)  
