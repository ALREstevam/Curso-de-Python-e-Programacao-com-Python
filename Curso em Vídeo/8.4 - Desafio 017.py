#calcular hipotenusa dado cateto oposto e adjacente

import math

catOposto = float(input('Cateto oposto: '))
catAdjacente = float(input('Cateto adjacente: '))

hipotenusa = math.sqrt(math.pow(catOposto, 2) + math.pow(catAdjacente, 2))

print("Hipostenusa vale {}".format(hipotenusa))

#a² + b² = c²