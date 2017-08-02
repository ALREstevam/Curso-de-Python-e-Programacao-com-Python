# import <módulo>
# import <funcionalidade> from <móulo>

# import math
# from math import sqrt
# from math import sqrt, ceil, floor
# from math import ceil, floor

import math
num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print('raiz {} = {}'.format(num, raiz))

print('Arredondando pra cima: {}'.format(math.ceil(raiz)))
print('Arredondando para baixo: {}'.format(math.floor(raiz)))
print('Truncando: {}'.format(math.trunc(raiz)))