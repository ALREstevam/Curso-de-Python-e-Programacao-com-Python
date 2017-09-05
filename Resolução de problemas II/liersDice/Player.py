from Dices import *
class Player:
    playerTypes = ('HUM', 'IA')
    playerNames = ('Ademilsom', 'Ana Maria', 'Bragança', 'Juliete', 'Cleusa')

    def __init__(self, playerType, playerID, playerName):
        """Class player implements general methods to simulate any type of player"""
        self.playerType = playerType
        self.playerID = playerID
        self.playerName = playerName

        self.dices = Dices(5)
        self.bet = {'Face': 0, 'Amount': 0, 'PlayerName': self.playerName}


    def takeAction(self, lastBet):
        """"Player should take an action"""
        print('It\'s player {} round. May take action.'.format(self.playerName))


    def callLiar(self, lastBet):
        """Player will say that the last one overestimated his bet"""
        print('{} says that {} overestimated his bet, lets see...'.format(self.playerName, lastBet[2]))
        return False


    def agree(self, lastBet):
        """Player agrees with the last one"""
        print('{} says that {} has a spot on, lets see...'.format(self.playerName, lastBet[2]))
        return False

    def makeBet(self, lastBet):
        """The player will make a bet"""
        print('{} wants to make a bet [FACE][AMOUNT]'.format(self.playerName))
        return False

    def verifyBet(self, actualBet, lastBet):
        """Verifies if a bet is valid according with the game rules and the last bet"""
        # A bet is an arrange with two integers [faceOfDice, amountOfInTable, nameOfThePlayerWhoMadeIt]
        # Tests if player has chosen a valid dice face
        if(actualBet['Face'] > 6 or actualBet['Face'] < 1):
            return False

        # If both players chosen tha same dice face, verify if the amount of dices has grown
        if(actualBet['Face'] < lastBet['Face']):
            return False

        if(actualBet['Face'] == lastBet['Face']):
            if(actualBet['Amount'] <= lastBet['Amount']):
                return False

        return True

    def rollDices(self):
        """Simulates a playet rolling it's dices"""
        self.dices.roll()
        return self.dices

    def loseADice(self):
        """Simulates a player losing a dice"""
        self.dices.looseDice()
        return self.dices.diceAmount



