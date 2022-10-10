velocidade = int(input("Qual foi era a velocidade do carro em km/h? "))

if velocidade > 80:
    print("Velocidade ultrapassada")
    multa = (velocidade - 80) * 50
    print(f"Sera necessario pagar uma multa no valor de : R${multa}")
else:
    print("Dentro da velocidade permitida")


