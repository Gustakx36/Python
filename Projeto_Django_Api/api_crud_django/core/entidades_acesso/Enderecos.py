from core.entidades_acesso import Query, Cliente

def selectSimples():
    enderecos = Query.selectSimples('core_endereco')
    return enderecos

def selectSimplesPorId(id):
    enderecos = Query.selectSimplesPorId('core_endereco', id)
    return enderecos

def selectUltimo():
    enderecos = Query.selectUltimo('core_endereco')
    return enderecos

def insertSimples(enderecoNew):
    enderecos = Query.insertSimples('core_endereco', 'cep,rua,numero,id_cliente', enderecoNew)
    return {
        'insert' : enderecos,
        'existeFk' : Cliente.selectSimplesPorId(enderecoNew['id_cliente'])
    }

def updateSimples(enderecoNew, id):
    enderecos = Query.updateSimples('core_endereco', 'cep = %s, rua = %s, numero = %s, id_cliente = %s', enderecoNew, id)
    return enderecos

def deleteSimples(id):
    enderecos = Query.deleteSimples('core_endereco', id)
    return enderecos

def selectColunas():
    enderecos = Query.selectColunas('core_endereco')
    return enderecos

def tableName():
    return 'Endereco'