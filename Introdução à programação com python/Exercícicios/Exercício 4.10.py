consumo = int(input("Consumo kWh: "))

print("R - Residência\n"
      "I - Indústrias\n"
      "C - Comércio\n"
     )
tipoInst = input("Tipo de instalação: ")

preco = 0
err = False

if tipoInst == 'R':
    if consumo <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif tipoInst == 'C':
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipoInst == 'I':
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Entrada inválida")
    err = True

if err == False:
    print("Preço R$ {}".format(preco))

