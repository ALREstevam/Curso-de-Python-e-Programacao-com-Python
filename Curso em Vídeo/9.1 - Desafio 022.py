#Nome completo
#Todas as letras maiúsculas
#Todas as letras minúsculas
#Quantas letras tem sem considerar espaços
#Tamanho do primeiro nome

nome = str(input('Nome: '))

print('Em maiúsculo: {}'.format(nome.upper()))
print('Em minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras no nome: {}'.format(len(nome) - nome.count(' ')))
print('Tamanho do primeiro nome: {}'.format(len((nome.split())[0])))
print('Tamanho do primeiro nome: {}'.format(nome.find(' ')))
