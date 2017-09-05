
dist = float(input('Distância da viagem (km): '))
passagem = 0

if dist <= 200:
    passagem = dist * 0.5
else:
    passagem = dist * 0.45

print('A passagem custará R$ {:.2f}'.format(passagem))