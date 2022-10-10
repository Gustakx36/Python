print("Me informe o tamanho dos lados do triângulo e irei defini-lo")

Lado_A = float(input("Qual tamanho do lado A : "))

Lado_B = float(input("Qual tamanho do lado B : "))

Lado_C = float(input("Qual tamanho do lado C : "))

while True:

    if Lado_A <= 0 or Lado_B <= 0 or Lado_C <= 0:

        print("Valores Invalidos")

        exit("")

        break

    else:

        print("Valores Validos")

        break

while True:

    if Lado_A + Lado_B <= Lado_C:

        print("Valores Invalidos")

        exit("")

        break

    elif Lado_A + Lado_C <= Lado_B:

        print("Valores Invalidos")

        exit("")

        break

    elif Lado_B + Lado_C <= Lado_A:

        print("Valores Invalidos")

        exit("")

        break

    else:

        print('Valores Validos')

        break

while True:

    if Lado_A >= Lado_B or Lado_A >= Lado_C:

        A: float = Lado_A
        B: float = Lado_B
        C: float = Lado_C

        break

    elif Lado_B >= Lado_A or Lado_B >= Lado_C:

        A: float = Lado_B
        B: float = Lado_A
        C: float = Lado_C

        break

    elif Lado_C >= Lado_A or Lado_C >= Lado_B:

        A: float = Lado_C
        B: float = Lado_A
        C: float = Lado_B

        break

print("_____________________________________________________________________________________")

while True:

    if Lado_A == Lado_B == Lado_C:

        print("Seu triangulo é Equilatero")

        break

    elif Lado_A == Lado_B != Lado_C or Lado_A != Lado_B == Lado_C:

        print("Seu Triângulo é Isóceles")

        break

    elif Lado_A != Lado_B != Lado_C:

        print("Seu Triângulo é Escaleno")

        break

while True:

    if A ** 2 < B ** 2 + C ** 2:

        print("Seu Triângulo é Acutângulo")

        break

    elif A ** 2 == B ** 2 + C ** 2:

        print("Seu Triângulo é Retangulo")

        break

    elif A ** 2 > B ** 2 + C ** 2:

        print("Seu Triângulo é Obtusangulo")

        break

print("_____________________________________________________________________________________")
