tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('E acabou')


# Condição simplificada

print('Carro novo' if tempo <= 3 else 'carro velho')
print('Fim')