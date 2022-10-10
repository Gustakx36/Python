N = int(input("Quantos caracois foram analizados? : "))
lista_tempo = []
nivel0 = []
nivel1 = []
nivel2 = []

Z = int(input("Qual primeiro tempo do percurso? : "))
lista_tempo.append(Z)

for x in range(1, N):
    Z = int(input("Qual o outro tempo de percurso? : "))
    lista_tempo.append(Z)

for x in lista_tempo:
    if x < 180:
        nivel0.append(x)
    if 180 <= x < 240:
        nivel1.append(x)
    if x >= 240:
        nivel2.append(x)


def Vel_Min():
    lista_tempo.sort()
    seg_min = float(lista_tempo[N-1] / 60)
    velminima = float(33 / seg_min)
    print(f"A velocidade minima é : {velminima: .1f}")


def Vel_Max():
    lista_tempo.sort()
    seg_min = float(lista_tempo[0] / 60)
    velmaxima = float(33 / seg_min)
    print(f"A velocidade maxima é : {velmaxima: .1f}")

print()
print(f"Caracois no nivel 0 : {len (nivel0)}")
print(f"Caracois no nivel 1 : {len (nivel1)}")
print(f"Caracois no nivel 2 : {len (nivel2)}")
print(f"Tempo medio : {sum (lista_tempo) / len (lista_tempo): .1f}s")
Vel_Max()
Vel_Min()
