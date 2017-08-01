vel = float(input("Velocidade do carro (km/h): "))

if vel > 80:
    print("Usuário foi multado em R${}".format((vel - 80) * 5))
else:
    print("Não foi multado")