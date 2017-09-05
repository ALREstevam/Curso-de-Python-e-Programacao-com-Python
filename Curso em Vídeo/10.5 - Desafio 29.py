vel = float(input('Vel Km/h '))


if vel > 80:
    print('Foi multado')
    multa = (vel - 80) * 7
    print('R$ {:.2f}'.format(multa))


