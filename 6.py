numero_1 = int(input("Qual o primeiro valor? "))
listanumeros = []
soma = 0
multiplicacao = 1

for x in range(9):
    numero = int(input("Qual o outro valor? "))
    listanumeros.append(numero)

print(f"Os valores digitados foram : {listanumeros}")

for x in listanumeros:
    soma = soma + x

print(f"A soma dos valores e igual a : {soma}")

for x in listanumeros:
    multiplicacao = multiplicacao * x

print(f"a multiplicacao dos valores e igual a : {multiplicacao}")

print(f"O maior numero digitado foi : {listanumeros[(len(listanumeros) - 1)]}")
print(f"O menos numero digitado foi : {listanumeros[0]}")
