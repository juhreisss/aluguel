from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios', UsuarioListCreateAPIView.as_view()),
    path('usuario/<int:pk>', UsuarioUpdateDestroyAPIView.as_view()),
    path('listar_usuarios', listar_usuarios),
 
    path('imoveis', ImovelListCreateAPIView.as_view()),
    path('imovel/<int:pk>', ImovelUpdateDestroyAPIView.as_view()),
    path('listar_imoveis', listar_imoveis),
 
    path('contratos', ContratoListCreateAPIView.as_view()),
    path('contrato/<int:pk>', ContratoUpdateDestroyAPIView.as_view()),
    path('listar_contratos', listar_contratos),
 
    path('pagamentos', PagamentoListCreateAPIView.as_view()),
    path('pagamento/<int:pk>', PagamentoUpdateDestroyAPIView.as_view()),
    path('listar_pagamentos', listar_pagamentos),
]