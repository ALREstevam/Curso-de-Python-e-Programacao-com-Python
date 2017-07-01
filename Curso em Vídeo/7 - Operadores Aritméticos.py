#Operadores Aritméticos
# = + - / * **
# ** potênciação
# // divisão inteira
# % módulo (resto da divisão)

# == (é igual a)

'''
PRECEDÊNCIA DE OPERADORES
1º ()
2º **
3º *, /, //, %
4º +, -
'''


#operador binário: precisa de dois operandos

a = int(input('n1:'))
b = int(input('n2:'))

print('a = {} e b = {}\n\n'.format(a, b))
print('a + b   = {}\n'
      'a - b   = {}\n'
      'a / b   = {}\n'
      'a * b   = {}\n'
      'a ** b  = {}\n'
      'a // b  = {}\n'
      'a % b   = {}\n'
      'a == b  = {}\n'.
      format(a + b,
             a - b,
             a / b,
             a * b,
             a ** b,
             a // b,
             a % b,
             a == b)
      )


print('a / b = {:.3f}'.format(a/b), end = ' ')
print('ESTOU NA MESMA LINHA')

