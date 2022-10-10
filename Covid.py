print('''Você está com Tosse
Se estiver digite [sim] 
Se não estiver digite [nao] 
''')
while True:
    option_1 = str(input('Digite sua Resposta : '))
    if option_1 == "sim":
        break
    elif option_1 == "nao":
        break
    else:
        print("Resposta não Identificada, Tente Novamente")
        exit("")
print()
print('''Voce esta com Febre
Se estiver digite [sim] 
Se não estiver digite [nao] 
''')
while True:
    option_2 = str(input('Digite sua Resposta : '))
    if option_2 == "sim":
        break
    elif option_2 == "nao":
        break
    else:
        print("Resposta não Identificada, Tente Novamente")
        exit("")
print()
print('''Você está com dificuldade para respirar
Se estiver digite [sim] 
Se não estiver digite [nao] 
''')
while True:
    option_3 = str(input('Digite sua Resposta : '))
    if option_3 == "sim":
        break
    elif option_3 == "nao":
        break
    else:
        print("Resposta não Identificada, Tente Novamente")
        exit("")
print("<-------------------------->")
while True:
    if option_1 == "nao" and option_2 == "nao" and option_3 == "nao":
        print('Você não está com Covid-19')
        break
    elif option_1 == "nao" and option_2 == "nao" and option_3 == "sim":
        print('Você não está com Covid-19')
        break
    elif option_1 == "nao" and option_2 == "sim" and option_3 == "nao":
        print('Você não está com Covid-19')
        break
    elif option_1 == "nao" and option_2 == "sim" and option_3 == "sim":
        print('Você não está com Covid-19')
        break
    elif option_1 == "sim" and option_2 == "nao" and option_3 == "nao":
        print('Você não está com Covid-19')
        break
    elif option_1 == "sim" and option_2 == "nao" and option_3 == "sim":
        print('Você não está com Covid-19')
        break
    elif option_1 == "sim" and option_2 == "sim" and option_3 == "nao":
        print('Você não está com Covid-19')
        break
    elif option_1 == "sim" and option_2 == "sim" and option_3 == "sim":
        print('Você está com Covid-19')
        break
print("<-------------------------->")
