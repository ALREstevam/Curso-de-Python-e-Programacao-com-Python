#Pessoa possui silva no nome?

findWord = 'Silva'
nome = str(input('Seu nome: '))

print('Possui "{}" no nome?    :   {}'.format(findWord, nome.find(findWord) >= 0))