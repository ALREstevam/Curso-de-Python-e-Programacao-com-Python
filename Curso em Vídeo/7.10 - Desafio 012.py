#Desafio 12 - 5% de desconto

preco = float(input('Preço do produto R$ '))
descontoPorcent = 5

print('Preço com desconto R$ {:.2f}'.format(preco - (preco * (descontoPorcent / 100))))

