'''
• Contar quantas vezes aparece ‘amava’.
• Encontrar o primeiro e o último índice em que
aparece ‘amava’.
• Encontrar todos os índices em que aparece
‘amava’.
• Substituir ‘amava’ por ‘treinava’.
• Indique quais linhas começam com ‘que’.
'''

strOrig = '''João amava Teresa que amava Raimundo
que amava Maria que amava Joaquim que amava Lili
que não amava ninguém.
João foi pra os Estados Unidos, Teresa para o convento,
Raimundo morreu de desastre, Maria ficou para tia,
Joaquim suicidou-se e Lili casou com J. Pinto Fernandes
que não tinha entrado na história.'''

str = strOrig.lower()

print('-'*10 + '\n')

print('A palavra \'amava\' aparece {} vezes'.format(str.count('amava')))
print('A palavra \'amava\' aparece pela primeira vez no índice {}'.format(str.find('amava')))
print('A palavra \'amava\' aparece pela última vez no índice {}'.format(str.rfind('amava')))

print('-'*10 + '\n')

print('Substituindo amava por treinava\n')
print(strOrig.replace('amava', 'treinava'))

strAux = str.splitlines()

'''
n = 0
pos = 0
while pos != -1:
    pos = str[n:len(str)].find('amava')
    print(pos)
    n += 1
'''

print('-'*10 + '\n')
print('Começam com \'que\' as linhas: ')
lineCount = 0
for line in strAux:
    if line.startswith('que'):
        print('{} '.format(lineCount), end='')
    lineCount += 1

print('\n')


print(strOrig.split())
print(strOrig.split(','))
print(strOrig.replace(' ', '_'))

words = [""]

str = str.replace('.', '')
str = str.replace(',', '')
str = str.lower()

dic = {}

splitted = str.split()

for wordInText in splitted:
    numbr = str.count(wordInText)

    str = str.replace(wordInText, '')
    splitted = str.split()


    print(':: {} - {}'.format(wordInText, numbr))

    input()




