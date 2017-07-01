#Desafio 11 - Área da parede e quanta tinta 1l -> 2m^2

paredeAltura = float(input('Altura: '))
paredeLargura = float(input('Largura: '))

metroQuadradoPorLitro = float(2)
paredeArea = paredeAltura * paredeLargura

print('Área da parede: {:.2f}m²'.format(paredeArea))

print('Você irá precisar de {:.2f}l de tinta'.format(paredeArea / metroQuadradoPorLitro))