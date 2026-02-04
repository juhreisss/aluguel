from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from rest_framework.decorators import api_view
from .serializers import (UsuarioSerializer, ImovelSerializer,  ContratoSerializer, PagamentoSerializer
)


# class UsuarioListCreateAPIView(APIView):
#     def get(self, request):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)

####GET E POST ####
#USUARIO#

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


####GET E POST ####
@api_view(['GET', 'POST'])
def listar_usuarios(request):
    if request.method == 'GET':
        queryset= Usuario.objects.all()
        serializers = UsuarioSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = UsuarioSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#### UPDATE E DELETE ####

class UsuarioUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#####################################################################################
#IMOVEL#
####GET E POST ####
class ImovelListCreateAPIView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer


####GET E POST ####
@api_view(['GET', 'POST'])
def listar_imoveis(request):
    if request.method == 'GET':
        queryset= Imovel.objects.all()
        serializers = ImovelSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ImovelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#### UPDATE E DELETE ####

class ImovelUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

#####################################################################################
#CONTRATO#
####GET E POST ####
class ContratoListCreateAPIView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


####GET E POST ####
@api_view(['GET', 'POST'])
def listar_contratos(request):
    if request.method == 'GET':
        queryset= Contrato.objects.all()
        serializers = ContratoSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ContratoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#### UPDATE E DELETE ####

class ContratoUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


#####################################################################################
#PAGAMENTO#
####GET E POST ####
class PagamentoListCreateAPIView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

####GET E POST ####
@api_view(['GET', 'POST'])
def listar_pagamentos(request):
    if request.method == 'GET':
        queryset= Pagamento.objects.all()
        serializers = PagamentoSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = PagamentoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#### UPDATE E DELETE ####

class PagamentoUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer