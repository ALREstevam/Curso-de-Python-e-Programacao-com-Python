dist = float(input("Distância a percorrer (km): "))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45

print("Passagem custará R$ {:.2f}".format(preco))