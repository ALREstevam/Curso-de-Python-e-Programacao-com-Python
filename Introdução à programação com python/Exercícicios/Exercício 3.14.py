percorrido = float(input("Km percorridos: "))
diasAlugado = int(input("Dias alugados: "))

print("Carro percorreu {}km durante {}dia(s) \nTotal a pagar R${}".format(percorrido, diasAlugado, 60 * diasAlugado + 0.15 * percorrido))