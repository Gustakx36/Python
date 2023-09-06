from core.connection import connectionDB
from core.entidades_acesso import Query
import random

def selectSimples():
    Query.selectSimples('core_api_key')
    acesso = Query.selectSimples('core_api_key')
    return acesso

def selectColunas():
    acesso = Query.selectColunas('core_api_key')
    return acesso

def verificaAcessoApiKey(key):
    sql = """
        SELECT api_key FROM 
            core_api_key
        WHERE 
            api_key = %s
    """
    acesso = connectionDB.read_query_bind(sql, [key])
    return acesso

def apiKeyPorLogin(id_login):
    sql = """
        SELECT api_key FROM 
            core_api_key
        WHERE 
            id_login = %s
    """
    acesso = connectionDB.read_query_bind(sql, [id_login])
    return acesso['api_key'] if acesso != None else None

def adicionarKeyAoBanco(key, keyNew):
    sql = """
        INSERT INTO 
            core_api_key(api_key, id_login) 
        VALUES 
            (%s, %s)
    """
    acesso = connectionDB.execute_query(sql, [key, keyNew['id_login']])
    return acesso

def insertSimples(keyNew):
    escolhas_possiveis = 'ABCDEFG123456789'
    resultado = ''
    for i in range(40):
        resultado += random.choice(escolhas_possiveis)
    return {
        'insert' : adicionarKeyAoBanco(resultado, keyNew),
        'Api_Key' : resultado,
        'existeFk' : True
    }

def tableName():
    return 'ApiKey'

def selectColunas():
    clientes = Query.selectColunas('core_api_key')
    return clientes
