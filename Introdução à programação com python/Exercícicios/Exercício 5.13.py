dividaInicial = float(input('Dívida inicial R$ '))
taxaJuroMensal = float(input('Taxa juros mensal (%)'))
pagamentoMes = float(input('Depósito por mês R$ '))

divida = dividaInicial
dividaAnt = 0
pago = 0
juroAcum = 0
juro = 0
mês = 0
erro = bool(False)

while divida > 0:

    juro = divida * (taxaJuroMensal/100)
    divida = (divida + juro) - pagamentoMes


    ##Acumuladores e contadoes
    mês = mês + 1
    juroAcum = juroAcum + juro
    pago = pago + pagamentoMes

    #print('Divi: {}'.format(divida))

    if divida == dividaAnt:
        print('Impossível pagar dívida: valor a pagar se estabiliza.')
        erro = True
        break
    else:
        dividaAnt = divida



    if divida == float('Inf'):
        print('Impossível pagar dívida: valor a pagar tende ao infinito.')
        erro = True
        break


if erro == False:
    print('A dívida será paga em {} meses.'.format(mês+1))
    print('Total pago R$ {:.2f}'.format(pago))
    print('Total de juros pago R$ {:.2f}'.format(juroAcum))




