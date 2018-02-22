# define diferentes jogadores para Liers' Dice
from random import randrange

class JogadorPC:

    dadosRestanteNaMesa = 15

    def __init__(self):
        self.dados = [0] * 5
        self.dadosRestantes = 5
        self.palpite = 0
        self.faceDado = 0
        self.id = "PC random"


    def jogaDados(self):
        for i in range(0,self.dadosRestantes):
            self.dados[i] = randrange(1,7)

    def joga(self, ultimoPalpite):
        print "%s: " % self.id,
        if ultimoPalpite == 0:
            op = 1
        else:
            op = randrange(1,4)

        if op == 1:
            self.palpite = randrange(ultimoPalpite, JogadorPC.dadosRestanteNaMesa)
            self.faceDado = randrange(1, 7)
            print "Turn, There are %d faces of %d" % (self.palpite, self.faceDado)
            return "TURN"
        if op == 2:
            print "You Lier!"
            return "LIER"
        if op == 3:
            print "I call it even!"
            return "EVEN"

    def perdeuMao(self):
        self.dados.pop()
        self.dadosRestantes -= 1

    def mostraDados(self):
        for d in self.dados:
            print d,
        print

    def getPalpite(self):
        return self.palpite

    def getFaceDadoPalpite(self):
        return self.faceDado

    def getDados(self):
        return self.dados

    def getId(self):
        return self.id

class JogadorPCInteligente(JogadorPC):

    def __init__(self):
        JogadorPC.__init__(self)
        self.id = "PC smart",

    def joga(self, ultimoPalpite):
        print "%s: " % self.id,
        if ultimoPalpite == 0:
            op = 1
        else:
            op = randrange(1,4)

        if op == 1:

            contaFaceDados = [0] * 7  # representa face do dado + o 0
            for i in range(len(self.dados)):
                contaFaceDados[self.dados[i]] += 1

            maior = 0
            faceMaior = 0
            for j in range(1, len(contaFaceDados)):
                if maior < contaFaceDados[j]:
                    maior = contaFaceDados[j]
                    faceMaior = j

            if maior > 1:
                self.palpite = ultimoPalpite + randrange(1,maior)
            else:
                self.palpite = ultimoPalpite + 1

            self.faceDado = faceMaior
            print "Turn, There are %d faces of %d" % (self.palpite, self.faceDado)
            return "TURN"
        if op == 2:
            print "You Lier!"
            return "LIER"
        if op == 3:
            print "I'll call even!"
            return "EVEN"


class JogadorHumano(JogadorPC):

    def __init__(self):
        JogadorPC.__init__(self)
        self.id = "Player",

    def joga(self, ultimoPalpite):
        print "%s: " % self.id,
        self.mostraDados()
        if ultimoPalpite == 0:
            op = 1
        else:
            op = int(raw_input("Turn: 1; Call Lier: 2; Call Even: 3 "))
            while op <> 1 and op <> 2 and op <> 3:
                op = int(raw_input("Turn: 1; Call Lier: 2; Call Even: 3 "))

        if op == 1:
            self.faceDado = int(raw_input("Face do dado: "))
            palpiteValido = int(raw_input("Palpite: "))
            while palpiteValido <= ultimoPalpite:
                print "Entre com um palpite maior que %d" % ultimoPalpite
                palpiteValido = int(raw_input("Palpite: "))

            self.palpite = palpiteValido
            print "Turn, There are %d faces of %d" % (self.palpite, self.faceDado)
            return "TURN"
        if op == 2:
            print "Lier"
            return "LIER"
        if op == 3:
            print "Even"
            return "EVEN"

