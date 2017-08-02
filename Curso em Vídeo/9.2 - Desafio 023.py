#NUM DE 0 A 9999
#mostrar cada um dos dígitos separados: dezena centena e milhar

valor = input('Número de 0 a 9999: ')
valor = valor[:4]
print(valor)
nomes = ['unidade(s)','dezena(s)','centena(s)','milhare(s)']
#Como string

print('COM MANIPULAÇÃO DE STRING\nO número tem')
for i in range(len(valor)):
    print('{} {}'.format(valor[(len(valor)-1) - i], nomes[i]))

#Forma matemática

print(10 * '--')
print('FORMA MATEMÁTICA\nO número tem')
valor = int(valor)
for i in range(len(str(valor))):
    aux = valor % 10
    print('{} {}'.format(aux, nomes[i]))
    valor = valor // 10

