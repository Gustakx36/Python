from django.contrib import admin
from django.urls import path, include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('cliente', views.index, name='cliente'),
    path('login', views.index, name='login'),
    path('endereco', views.index, name='endereco'),
    path('key', views.index, name='key'),
    path('cliente/<int>', views.indexInt, name='clienteId'),
    path('login/<int>', views.indexInt, name='clienteId'),
    path('endereco/<int>', views.indexInt, name='enderecoId'),
    path('iniciar', views.iniciarTables, name='iniciarTables'),
    path('home/listar', views.HomeListar, name='listarItens'),
    path('home', views.login, name='login'),
    path('home/registrar', views.registrar, name='login'),
    path('home/registrar/login', views.registerLogin, name='login'),
    path('home/listar/<integer>', views.HomeListarInt, name='listarItensInt'),
    path('home/verify', views.loginVerify, name='verificarLogin')
]
