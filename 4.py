salario = int(input("Qual o valor do salario? "))
aumento_porc = int(input("Qual a porcentagem de aumento? "))

aumento = salario + ((salario * aumento_porc) / 100)
aumento_relacao = aumento - salario

print(f"O salario apos o aumento teve o valor de : R${aumento: .2f}")
print(f"Equivalente a um aumento de : R${aumento_relacao: .2f}")
