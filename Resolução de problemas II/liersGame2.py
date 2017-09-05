
import random

firstRound = True
actualRound = 0
playerTypes = {0: 'npc', 1: 'hum'}
actions = {0: 'Fazer uma aposta', 1: 'Concordar', 2: 'Discordar'}


players = [['HUM', playerTypes[1], 5],['NPC1', playerTypes[0], 5], ['NPC2', playerTypes[0], 5]]
random.shuffle(players)

print(players)

playerAmount = len(players)


def pause():
    input('Pressione enter...')

def nextRound(actualRound, playerAmount):
    return (actualRound + 1) % playerAmount

def iaRandom(options):
    return random.randint(0, options)


def rollDices(diceAmount):
    print('Rolando dados...')
    dicesList = []
    for i in range(diceAmount):
        dicesList.append(random.randint(1, 6))
        #print(dicesList)
    return dicesList


def printDices(dices):
    for dice in dices:
        print('[{:2}], '.format(dice), end='')
    print('\n')

def presentBet(playerName, face, amount):
    print('{} diz que existem {} dados de face {} na mesa.'.format(playerName, amount, face))

def collectHumanChoice():
    i = False
    while i == False:
        print('Você pode:\n'
              '1 - Concordar.\n'
              '2 - Discordar.\n'
              '3 - Fazer uma aposta.\n')

        escolha = int(input(':'))

        if(escolha == 1 or escolha == 2 or escolha == 3):
            return escolha



while True:
    print('É o round: {}'.format(actualRound))
    actualPlayer = players[actualRound]
    print('É a vez de: {}'.format(actualPlayer[0]))

    if firstRound == True:
        print('É a primeira rodada')
        firstRound = False

        if actualPlayer[1] == playerTypes[0]: #se é primeira jogada do npc
            dados = rollDices(actualPlayer[2])
            dadoFace = random.randint(1,6)
            dadoQtd = random.randint(1, 5 * playerAmount)
            presentBet(actualPlayer[0], dadoFace, dadoQtd)
            pause()


        else: #se é a primeira jogada do humano
            dados = rollDices(actualPlayer[2])
            printDices(dados)
            print('Você deve fazer uma aposta')
            dadoFace = int(input('Face do dado:'))
            dadoQtd = int(input('Quantidade na mesa: '))
            presentBet(actualPlayer[0], dadoFace, dadoQtd)
            pause()

    else: #não é o primeiro round
        if actualPlayer[1] == playerTypes[0]:  # se é primeira jogada do npc



    actualRound = nextRound(actualRound, playerAmount)


