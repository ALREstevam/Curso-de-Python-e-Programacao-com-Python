from Player import *
from Dices import *

class HumanPlayer(Player):
    def __init__(self):
        """Class player implements general methods to simulate a human player"""
        self.playerType = Player.playerTypes[0]
        self.playerID = 0
        self.playerName = str(input('What\'s your name, player? '))

        self.dices = Dices(5)
        self.bet = {'Face': 0, 'Amount': 0, 'PlayerName': self.playerName}


    def takeAction(self, lastBet):
        print('YOUR TURN')
        print('Las bet was: {} time face [{}] '.format(lastBet[1], lastBet[0]))


        aux = False
        while aux == False:
            print('You can [b]et, call {} a [l]iar or say that {} has a [s]pot on')
            choice = str(input(': '))

            if(choice == 'b'):
                aux = True

            elif(choice == 'l'):
                aux = True

            elif(choice == 's'):
                aux = True



    def makeBet(self, lastBet):
        while True:
            print('You are about to make a bet. [Face] [Amount of]')
            choice = str(input()).split()
            print("{} [FACE / AMOUNT]".format(choice))

            self.bet['Face'] = choice[0]
            self.bet['Amount'] = choice[1]

            if(self.verifyBet(self.bet, lastBet)):
                return self.bet



    def callLiar(self, lastBet):
        Player.callLiar(self, lastBet)

        return 'LIAR'

    def agree(self, lastBet):
        Player.agree(self, lastBet)
        return 'AGREED'

p1 = Player('IA', 0, 'Ia test')
bet = {'Face' : 2, 'Amount': 1, 'PlayerName' : 'Myname'}

p1.takeAction(bet)




