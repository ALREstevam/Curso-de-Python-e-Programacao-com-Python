#Desafio 10 reais para dólares

reais = float(input("R$ "))
taxaconv = float(3.27)

print('R$ {:.2f} => US$ {:.2f}'.format(reais, reais/taxaconv))
