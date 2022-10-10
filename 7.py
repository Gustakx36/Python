palavra = str(input("Digite uma palavra : "))
lista = []

for x in palavra:
    lista.append(x)
    if x == "a":
        lista.remove(x)
    if x == "e":
        lista.remove(x)
    if x == "i":
        lista.remove(x)
    if x == "o":
        lista.remove(x)
    if x == "u":
        lista.remove(x)
    else:
        continue

for x in lista:
    print(x, end="")
