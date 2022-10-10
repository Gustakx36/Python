NUM = str(input("Qual o numero, string ou ambos que sera invertido : "))
lista = []
lista2 = []
lista3 = []


def inverter(x):
    if x.isdigit():
        print(x[::-1])
    elif x.isalpha():
        print(x[::-1])
    else:
        for i in x:
            if i.isdigit():
                lista.append(i)
            elif i.isalpha():
                lista2.append(i)
            else:
                lista3.append(i)
        for i in lista[::-1]:
            print(i, end="")

        print('''
        ''')

        for i in lista2[::-1]:
            print(i, end="")

        print('''
        ''')

        for i in lista3[::-1]:
            print(i, end="")

if NUM.isdigit:
    print()
    inverter(NUM)
elif NUM.isalpha():
    print()
    inverter(NUM)
else:
    print()
    inverter(NUM)
