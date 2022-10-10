X = int(input("Quantas vezes voce quer que repita a mensagem? "))
Num = "bom dia"
Num2 = "MEU AMORZINHO"


def mensagem():
    for x in range(0, X):
        print(Num)
        print(Num2)

print(mensagem())
