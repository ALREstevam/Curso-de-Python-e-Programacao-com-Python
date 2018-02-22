import time
import random

class CoolWriter:

    def __init__(self, normal = 0.1, long = 0.5):
        self.normal = normal
        self.longer = long
        self.seps = ['.', ',', ';', '\t', '\n', ' ']


    def print(self, text):
        chars = list(text)

        for char in chars:
            print(char, end='')
            if char in self.seps:
                time.sleep(self.longer)
            else:
                time.sleep(self.normal)


    def randprint(self, text, randomRange):
        chars = list(text)
        for char in chars:
            print(char, end='')
            if char in self.seps:
                time.sleep(random.uniform(self.butNonZero(self.longer,randomRange), self.longer + randomRange))
            else:
                time.sleep(random.uniform(self.butNonZero(self.normal, randomRange), self.normal + randomRange))
            

    def butNonZero(self, basis, minus):
        if basis - minus < 0:
            return 0
        else:
            return basis - minus


text = '''
AUTOPSICOGRAFIA
O poeta é um fingidor.
Finge tão completamente
Que chega a fingir que é dor
A dor que deveras sente.

E os que lêem o que escreve,
Na dor lida sentem bem,
Não as duas que ele teve,
Mas só a que eles não têm.

E assim nas calhas da roda
Gira, a entreter a razão,
Esse comboio de corda
Que se chama o coração.
'''

cw = CoolWriter()
cw.randprint(text, 0.02)



