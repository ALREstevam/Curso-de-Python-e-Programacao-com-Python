conta = float(input('Saldo inicial R$ '))
depMensal = float(input('Depósito mensal R$ '))
txJuro = float(input('Taxa juros mensal (%): '))


print('Mês {:2} Saldo R$ {:>5.2f}'.format(0, conta))
for mes in range(24):
    conta = conta + conta * (txJuro/100)
    print('Mês {:2} Saldo R$ {:>5.2f}'.format(mes+1, conta))
    cont = conta + depMensal