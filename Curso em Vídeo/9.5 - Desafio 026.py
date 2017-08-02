#ler frase, primeira aparição da letra a e última aparição

frase = str(input("Digite sua frase: "))

primA = frase.find('a')
ultA = frase.rfind('a')

print('Primeiro "a" em {}\n'
      'Último "a" em {}'.format(primA, ultA))