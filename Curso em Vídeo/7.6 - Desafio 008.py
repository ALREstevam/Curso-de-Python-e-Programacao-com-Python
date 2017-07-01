#Desafio 8 - Converter de m para cm e mm

medidam = float(input("Digite um valor em metros: "))

print('{:.3f} m = [{:.3f} cm] e [{:.3f} mm]'.format(medidam, medidam*100, medidam*1000))