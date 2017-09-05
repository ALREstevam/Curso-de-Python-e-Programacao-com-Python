from random import randint
class Dices:
    def __init__(self, diceAmount):
        self.diceAmount = diceAmount
        self.dices = [0] * diceAmount


    def roll(self):
        for i in range(self.diceAmount):
            self.dices[i] = randint(1, 6)
        self.dices.sort()

    def present(self):
        print('[ ', end='')
        for dado in self.dices:
            print('{} '.format(dado), end='')
        print(']')

    def sortDices(self):
        self.dices = self.dices.sort()

    def looseDice(self):
        self.dices.pop()
        self.diceAmount -= 1
        self.dices.sort()
