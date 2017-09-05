valor = float(input('Digite o valor a pagar: '))
cédulas = 0
atual = 100.0
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1

    else:
        print('%d cédula(s) de R$ %.2f' % (cédulas, atual))

        if apagar <= float(0.0) or apagar < 0.01:
            break

        if atual == 100.0:
            atual = 50.0

        elif atual == 50.0:
            atual = 20.0

        elif atual == 20.0:
            atual = 10.0

        elif atual == 10.0:
            atual = 5.0

        elif atual == 5.0:
            atual = 1.0

        elif atual == 1.0:
            atual = 0.50

        elif atual == 0.50:
            atual = 0.10

        elif atual == 0.10:
            atual = 0.05

        elif atual == 0.05:
            atual = 0.02

        elif atual == 0.02:
            atual = 0.01

        cédulas = 0