codpreco = [
    [1, 0.50],
    [2, 1.00],
    [3, 4.00],
    [5, 7.00],
    [9, 8.00]
    ]


print(codpreco)
finded = bool(False)

soma = 0

prod = -1
while True:
    prod = int(input('>>> [R$ {:.2f}] Código do produto: '.format(soma)))

    if prod == 0:
        break

    for i in range(len(codpreco)):
        if codpreco[i][0] == prod:
            soma = soma + codpreco[i][1]
            # print('Total a pagar R$ {:.2f}'.format(soma))
            finded = True
            break
        else:
            finded = False

    if finded == False:
        print('\n[Código inválido]\n')


print('****' * 10 + '\n')
print('Total a pagar R$ {:.2f}'.format(soma))