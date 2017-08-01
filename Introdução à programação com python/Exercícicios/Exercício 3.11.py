precoProduto = float(input("Preço do produto R$ "))
descontoPercent = float(input("Desconto % ")) / 100

print("Produto de R${} com desconto de {}% custa R${}.".format(precoProduto, descontoPercent*100, precoProduto - (precoProduto * descontoPercent)))