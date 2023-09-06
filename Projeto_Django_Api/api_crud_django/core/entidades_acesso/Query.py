from core.connection import connectionDB

def selectSimples(table):
    sql = "SELECT * FROM " + table
    result = connectionDB.read_query(sql)
    return result

def selectSimplesPorId(table, id):
    sql = "SELECT * FROM " + table + " WHERE id = %s"
    result = connectionDB.read_query_bind(sql, [id])
    return result

def selectUltimo(table):
    sql = "SELECT * FROM " + table + " ORDER BY id DESC LIMIT 1"
    result = connectionDB.read_query(sql)
    return result

def insertSimples(table, params, new):
    if 'ApiKey' in new:
        new.pop('ApiKey')
    x = '%s ' * len(params.split(','))
    paramsValues = ', '.join(x.strip().split())
    sql = "INSERT INTO " + table + "(" + params + ") VALUES (" + paramsValues + ")"
    result = connectionDB.execute_query(sql, list(new.values()))
    return result

def updateSimples(table, params, new, id):
    if 'ApiKey' in new:
        new.pop('ApiKey')
    lista = list(new.values())
    lista.append(id)
    sql = "UPDATE " + table + " SET " + params + " WHERE id = %s"
    result = connectionDB.execute_query(sql, lista)
    return result

def deleteSimples(table, id):
    sql = "DELETE FROM " + table + " WHERE id = %s"
    result = connectionDB.execute_query(sql, [id])
    return result

def selectColunas(table):
    sql = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'django_api_banco' AND TABLE_NAME = '" + table + "';"
    result = connectionDB.read_query(sql)
    return result

def verificaLoginSenha(Login):
    sql = "SELECT id FROM core_logins WHERE login = %s AND senha = %s;"
    result = connectionDB.read_query_bind(sql, list(Login.values()))
    return result['id'] if result != None else False