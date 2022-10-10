Texto = input("Escreva o texto : ")

Texto_lista = Texto.split()

Palavra = []

Numero = []

Hashtag = []

Emoticon = []

for x in Texto_lista:
    if x.isalpha():
        Palavra.append(x)

for y in Texto_lista:
    if "#" in y:
        Hashtag.append(y)


for z in Texto_lista:
    if z.isdigit():
        Numero.append(z)
    elif z.strip("-").isdigit():
        Numero.append(z)

SUB1 = list(set(Texto_lista) - set(Palavra))
SUB2 = list(set(SUB1) - set(Hashtag))
SUB3 = list(set(SUB2) - set(Numero))
Emoticon = SUB3

print()

print(F"Palavra(s) : {Palavra}")

print(F"Numero(s) : {Numero}")

print(F"Hashtag(s) : {Hashtag}")

print(F"Emoticon(s) : {Emoticon}")
