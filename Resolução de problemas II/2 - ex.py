
num = int(input('Num: '))
numAux = num



selec = 0
mult = 10000
numInvert = 0

for i in range(5):
    selec = num % 10
    numInvert += selec * mult

    mult //= 10
    num //= 10

print('Número invertido: {}'.format(numInvert))

if numInvert == numAux:
    print('SIM, É PALINDROME')
else:
    print('NÃO É PALINDROME')




