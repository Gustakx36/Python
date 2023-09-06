from core.entidades_acesso import Query, Logins

def selectSimples():
    clientes = Query.selectSimples('core_cliente')
    return clientes

def selectSimplesPorId(id):
    clientes = Query.selectSimplesPorId('core_cliente', id)
    return clientes

def selectUltimo():
    clientes = Query.selectUltimo('core_cliente')
    return clientes

def insertSimples(clienteNew):
    clientes = Query.insertSimples('core_cliente', 'nome,idade,id_login', clienteNew)
    return {
        'insert' : clientes,
        'existeFk' : Logins.selectSimplesPorId(clienteNew['id_login'])
    }

def updateSimples(clienteNew, id):
    clientes = Query.updateSimples('core_cliente', 'nome = %s, idade = %s, id_login = %s', clienteNew, id)
    return clientes

def deleteSimples(id):
    clientes = Query.deleteSimples('core_cliente', id)
    return clientes

def selectColunas():
    clientes = Query.selectColunas('core_cliente')
    return clientes

def tableName():
    return 'Cliente'