print('DIVISÃO a/b')

a = int(input('a = '))
b = int(input('b = '))

divAB = 0

while a >= b:
    a = a - b
    divAB = divAB + 1

print('{} / {} = {} com resto {}'.format(a, b, divAB, a))