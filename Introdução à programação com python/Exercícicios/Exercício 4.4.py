salario = float(input("Salário R$ "))

if salario > 1250:
    # + 10%
    print("Novo salário (+10%) R${}".format(salario + (salario * 0.10)))
else:
    # + 15%
    print("Novo salário (+15%) R${}".format(salario + (salario * 0.15)))
