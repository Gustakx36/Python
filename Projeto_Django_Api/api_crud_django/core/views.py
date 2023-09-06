from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .entidades_acesso import ApiKey
from core.connection import connectionDB
from core import normalizacaoRender
import re

def HomeListar(request):
    return normalizacaoRender.renderListar(request)

def HomeListarInt(request, integer):
    integer = int(integer)
    return normalizacaoRender.renderListar(request, integer)

def login(request):
    return normalizacaoRender.renderLogin(request)

def registrar(request):
    return normalizacaoRender.renderRegistrar(request)

def registerLogin(request):
    return normalizacaoRender.renderRegisterLogin(request)

@csrf_exempt
def loginVerify(request):
    return normalizacaoRender.renderLoginVerify(request)

@csrf_exempt
def index(request):
    return normalizacaoRender.renderIndexJson(request)

@csrf_exempt
def indexInt(request, int):
    return normalizacaoRender.renderIndexIntJson(request, int)

def iniciarTables(request):
    connectionDB.iniciarTable()
    return JsonResponse({'key_gerada' : 'iniciado'})
