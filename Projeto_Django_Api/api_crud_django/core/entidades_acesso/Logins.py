from core.entidades_acesso import Query, ApiKey

def selectSimples():
    logins = Query.selectSimples('core_logins')
    return logins

def selectSimplesPorId(id):
    logins = Query.selectSimplesPorId('core_logins', id)
    return logins

def selectUltimo():
    logins = Query.selectUltimo('core_logins')
    return logins

def insertSimples(loginNew):
    logins = Query.insertSimples('core_logins', 'login,senha', loginNew)
    apiKeyGerada = ApiKey.insertSimples({'id_login' : verificaLoginSenha(loginNew)})
    return {
        'insert' : logins,
        'apiKeyGerada' : apiKeyGerada['Api_Key'],
        'existeFk' : True
    }

def updateSimples(loginNew, id):
    logins = Query.updateSimples('core_logins', 'login = %s, senha = %s', loginNew, id)
    return logins

def deleteSimples(id):
    logins = Query.deleteSimples('core_logins', id)
    return logins

def selectColunas():
    logins = Query.selectColunas('core_logins')
    return logins

def verificaLoginSenha(Login):
    logins = Query.verificaLoginSenha(Login)
    return logins

def apiKeyLogin(Login):
    logins = verificaLoginSenha(Login)
    return ApiKey.apiKeyPorLogin(logins)

def tableName():
    return 'Login'