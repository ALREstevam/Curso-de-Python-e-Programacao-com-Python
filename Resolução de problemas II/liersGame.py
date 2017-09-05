import random

class Dices:
    def roll(self, dices):
        dices = []
        for i in range(dices):
            dices.append(random.randint(1,6))
            return dices

    def print(self,  dices):
        for dice in dices:
            print('[{:2}], '.format(dice), end='')
        print('\n')


class HumanPlayer:
    def __init__(self, nome):
        self.nome = nome
        self.dices = 5

    def takeAction(self, isFirstRound):
        if isFirstRound

class Npc0:
    def __init__(self):
        i = 0


class Game:
    def __init__(self):
        ph = HumanPlayer('Teste')
        npcA = Npc0()
        npcB = Npc0()
        npcC = Npc0()
        self.players = [ph, npcA, npcB, npcC]
        self.qtdPlayers = len(self.players)
        self.playerRound = 0
        self.isFirstRound = True

    def nextRound(self):
        self.playerRound = (self.playerRound + 1) % self.qtdPlayers


    def play(self):
        while True:
            self.players[self.playerRound].takeAction(self.isFirstRound)
            self.nextRound()

            if self.isFirstRound == True:
                self.isFirstRound == False





