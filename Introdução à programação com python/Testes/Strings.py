#Tamanho da string
print(len('A'))
print(len('Oiee'))
print(len('Minha terra tem palmeiras, Onde canta o Sabiá; As aves, que aqui gorjeiam, Não gorjeiam como lá.'))


#Posição em uma string
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for a in range(len(alfabeto)):
    print("{:<3d} : {}".format(a + 1, alfabeto[a]))

letra = int(input("Posição no alfabeto: "))
print("Letra da posição {}: {}".format(letra, alfabeto[letra-1]))

#Operadores numa string
s = 'abc'
print(s + 'd')
print(s + 'd' * 4)
print('+' + '-^-' * 10 + '+')

#Formatação de string
idade = 22
nome = 'João'
noBolso = float(22.50)

print('\nFORMATAÇÃO COM %')
print('[%d]' % idade)
print('[%03d]' % idade)
print('[%3d]' % idade)
print('[%-3d]' %idade)
print('%s tem %d anos e apenas R$%5.2f no bolso.' %(nome, idade, noBolso))

print('\nFORMATAÇÃO COM .format()')
print('[{}]'.format(idade))
print('[{:03d}]'.format(idade))
print('[{:3d}]'.format(idade))
print('[{:<3d}]'.format(idade))
print('{} tem {} anos e apenas R${:5.2f} no bolso.'.format(nome, idade, noBolso))

#Fatiamento
fatiaIni = int(0)
fatiaFim = int(3)

print('Fatia de {} até {} de {} é {}'.format(fatiaIni, fatiaFim, alfabeto, alfabeto[fatiaIni:fatiaFim]))
print('FATIA [:5] = {}'.format(alfabeto[:5]))
print('FATIA [20:] = {}'.format(alfabeto[20:]))
print('FATIA [0:-2] = {}'.format(alfabeto[0:-2]))
print('FATIA [-1:] = {}'.format(alfabeto[-1:]))
print('FATIA [-5:7] = {}'.format(alfabeto[-5:7]))
print('FATIA [-2:-1] = {}'.format(alfabeto[-2:-1]))