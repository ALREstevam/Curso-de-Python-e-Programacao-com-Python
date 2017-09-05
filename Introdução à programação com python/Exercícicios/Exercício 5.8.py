print('Multiplicação a * b')

a = int(input('a = '))
b = int(input('b = '))

cont = 1
acum = 0
while cont <= a:
    acum = acum + b
    cont = cont + 1

print(acum)