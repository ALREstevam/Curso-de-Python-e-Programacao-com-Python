num = int(input('Num: '))
numInvert = 0
numAux = num

'''
for i in range(5):
    numInvert += (num % 10) * (10 ** (4 - i))
    num //= 10
'''

for i in range(4, -1, -1):
    numInvert += (num % 10) * (10 ** i)
    num //= 10


print(numInvert)

if numInvert == numAux:
    print('SIM, É PALINDROME')
else:
    print('NÃO É PALINDROME')


