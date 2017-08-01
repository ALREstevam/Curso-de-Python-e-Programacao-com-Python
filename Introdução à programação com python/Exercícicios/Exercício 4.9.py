valorCasa = float(input("Valor da casa R$ "))
salário = float(input("Salário R$ "))
anosPagar = int(input("Anos a pagar: "))

#valor da prestação mensal deve ser até 30% do salário

prest = valorCasa / (anosPagar * 12)

if prest <= (salário * 0.3):
    print("Crédito aprovado")
else:
    print("Crédito negado   ")