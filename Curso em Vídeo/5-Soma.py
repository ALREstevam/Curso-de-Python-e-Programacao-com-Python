#Entrada de dados e soma
##Para strings o recomendado são as aspas simples

###N1 e N2 não tem tipo primitivo, são interpretados como strings

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

print(type(n1))
print(type(n2))


###Convertendo para float
sum = float(n1) + float(n2)

print(type(sum))

print("A soma vale:", sum)
print("A concatenação é:", n1 + n2)
