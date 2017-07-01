#Desafio 13 - 15% de aumento

salario = float(input('Salário R$ '))
aumentoPercent = float(15)
salarioComAumento = salario + (salario * (aumentoPercent/100))

print('Salário com aumento de {}% fica em R$ {:.2f}'.format(aumentoPercent, salarioComAumento))