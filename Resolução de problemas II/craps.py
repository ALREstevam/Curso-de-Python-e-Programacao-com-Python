from random import randint

def dado():
    return randint(1, 6)

def search(value, array):
    for element in array:
        if element == value:
            return True
    return False


def jogo():
    rodada = 0
    pontos = 0

    ganhar  = [7, 1]
    perder  = [2, 3, 12]
    pontuar = [4, 5, 6, 8, 9, 10]

    while True:
        rodada += 1
        dado1 = dado()
        dado2 = dado()

        dados = dado1 + dado2

        #Primeira rodada
        if rodada == 1:
            print('PRIMEIRA RODADA')
            print('[{}] + [{}] = [{}]'.format(dado1, dado2, dados))
            if search(dados, ganhar):
                print('Ganhou')
                break
            elif search(dados, perder):
                print('Perdeu')
                break
            elif search(dados, pontuar):
                print('Pontuou {}'.format(dados))
                pontos = dados

        else:
            print('RODADA {}'.format(rodada))
            print('[{}] + [{}] = [{}]'.format(dado1, dado2, dados))
            if dados == 7:
                print('Perdeu')
                break
            elif dados == pontos:
                print('Ganhou')
                break


jogo()
