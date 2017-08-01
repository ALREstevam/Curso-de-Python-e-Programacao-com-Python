salario = float(input("Salário R$ "))
aumento = float(input("Aumento % "))

print("R${} com um aumento de {}% resulta em R${}".format(salario, aumento, salario+(salario * (aumento/100) )))