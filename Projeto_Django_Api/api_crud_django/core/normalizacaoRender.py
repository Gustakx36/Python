from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from .entidades_acesso import Cliente, Logins, ApiKey, Enderecos
import re

def listaNormalizada(lista, itemActive=0):
    objetos = []
    i = 0
    for linhas in lista:
        objTemp = {
            'colunas' : [],
            'linhas' : [],
            'active' : "",
            'count' : i,
            'table' : linhas.tableName()
        }
        for item in linhas.selectColunas():
            objTemp['colunas'].append(item['COLUMN_NAME'])
        for linha in linhas.selectSimples():
            objTemp['linhas'].append(list(linha.values()))
        objetos.append(objTemp)
        i += 1
    objetos[itemActive]['active'] = 'active'
    return objetos

def renderListar(request, int=0):
    try:
        if not 'ApiKey' in request.GET.dict():
            return JsonResponse({
                'api_key_error': 'E necessario o atributo ApiKey'
            })
        if ApiKey.verificaAcessoApiKey(request.GET.dict()['ApiKey']):
            listaItensColunas = listaNormalizada([Logins, Cliente, Enderecos, ApiKey], int)
            itens = {
                'objetos' : listaItensColunas,
                'API_KEY' : request.GET.dict()['ApiKey'],
                'BASE_URL' : 'http://127.0.0.1:8000/'
            }
            return render(request, 'html/listar.html', itens)
        return renderLogin(request)
    except KeyError:
        return JsonResponse({
            'api_error': 'Error'
        })

def renderLogin(request):
    itens = {
        'BASE_URL' : 'http://127.0.0.1:8000/'
    }
    return render(request, 'html/login.html', itens)

def renderRegistrar(request):
    itens = {
        'BASE_URL' : 'http://127.0.0.1:8000/'
    }
    return render(request, 'html/register.html', itens)

def renderRegisterLogin(request):
    metodo = {
        'GET' : request.GET,
        'POST' : request.POST
    }[request.method]
    return JsonResponse(Logins.insertSimples(metodo.dict()))

def colunasString(lista):
    listaColuna = []
    for item in lista:
            listaColuna['colunas'].append(item['COLUMN_NAME'])
    return ','.join(listaColuna)

def renderIndexJson(request):
    try:
        metodo = {
            'GET' : request.GET,
            'POST' : request.POST
        }[request.method]
        dictObjeto = {
            'login' : Logins,
            'cliente' : Cliente,
            'endereco' : Enderecos,
            'key' : ApiKey
        }[request.META['PATH_INFO'].replace('/', '')]
        if not 'ApiKey' in metodo.dict():
            return JsonResponse({
                'api_key_error': 'E necessario o atributo ApiKey'
            })

        if ApiKey.verificaAcessoApiKey(metodo.dict()['ApiKey']):
            if request.method == 'GET':
                return JsonResponse({
                    request.META['PATH_INFO'].replace('/', '') + 's' : dictObjeto.selectSimples()
                })
            
            if request.method == 'POST':
                return JsonResponse(dictObjeto.insertSimples(metodo.dict()))
            
            return HttpResponseNotFound("Not found")
        
        return JsonResponse({
            'api_key_error': True
        })
    except KeyError:
        return JsonResponse({
            'api_error': 'Sao necessarios todos os parametros : ' + colunasString(dictObjeto.selectColunas())
        })

def renderIndexIntJson(request, int):
    if re.sub('[/0-9]', '', int).isalpha():
        return JsonResponse({
            'api_error': 'E necessario que o segundo parametro da requisicao seja um inteiro'
        })
    try:
        metodo = {
            'GET' : request.GET,
            'POST' : request.POST,
            'DELETE' : request.GET
        }[request.method]
        dictObjeto = {
            'login' : Logins,
            'cliente' : Cliente,
            'endereco' : Enderecos
        }[re.sub('[/0-9]', '', request.META['PATH_INFO'])]

        if not 'ApiKey' in metodo.dict():
            return JsonResponse({
                'api_key_error': 'E necessario o atributo ApiKey'
            })

        if ApiKey.verificaAcessoApiKey(metodo.dict()['ApiKey']): 
            if request.method == 'POST':
                return JsonResponse({
                    'update' : dictObjeto.updateSimples(metodo.dict(), int)
                })
            
            if request.method == 'GET':
                return JsonResponse({
                    re.sub('[/0-9]', '', request.META['PATH_INFO']) : dictObjeto.selectSimplesPorId(int)
                })
            
            if request.method == 'DELETE':
                return JsonResponse({
                    'delete' : dictObjeto.deleteSimples(int)
                })
            
            return HttpResponseNotFound("Not found")
        return JsonResponse({
            'api_key_error': True
        })
    except KeyError:
        return JsonResponse({
            'api_error': 'Sao necessarios todos os parametros : ' + colunasString(dictObjeto.selectColunas())
        })

def renderLoginVerify(request):
    return JsonResponse({
        'existe' : Logins.verificaLoginSenha(request.GET.dict()) > 0,
        'ApiKey' : Logins.apiKeyLogin(request.GET.dict())
    })