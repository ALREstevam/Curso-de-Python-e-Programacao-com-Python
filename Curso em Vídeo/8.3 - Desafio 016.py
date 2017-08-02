#ler número real e mostrar parte inteira
from math import trunc

num = float(input('Digite um número real: '))
print('Parte inteira de {} é {}'.format(num, trunc(num)))