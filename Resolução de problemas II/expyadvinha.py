from random import randint

def jogo():
    escolha = randint(1, 1000)

    print('Escolhi um número entre 1 e 1000, você consegue adivinhar qual é?')

    while True:
        palpite = int(input('Número: '))

        if escolha == palpite:
            print('Parebéns, era {}. Você ganhou.'.format(escolha))
            break

        elif (palpite > escolha -10) and (palpite < escolha + 10):
            print('Passou perto!')

        elif palpite > escolha:
            print('Muito grande, tente novamente.')

        elif palpite < escolha:
            print('Muito pequeno, tente novamente.')

jogo()