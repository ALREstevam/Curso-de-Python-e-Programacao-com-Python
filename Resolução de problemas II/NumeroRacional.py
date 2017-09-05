

###########################################################
class Fracao:
    def __init__(self, a = 0, b = 0):
        self.num = a
        self.den = b

    def getNumerador(self):
        return self.num

    def getDenominador(self):
        return self.den


    def printAB(self):
        print('{}/{} '.format(self.num, self.den))

    def printFloat(self):
        print('{:.5f}'.format(self.num / self.den))


    def getAB(self):
        return ('{}/{} '.format(self.num, self.den))

    def getFloat(self):
        return ('{:.5f}'.format(self.num / self.den))


###########################################################
class AritméticaFracao:
    def __init__(self, fracao1, fracao2):
        self.f1 = fracao1
        self.f2 = fracao2

        self.lastOperation = '[None/None] @ [None/None] = [None/None]'


    def setLastOperation(self, fr1, operation, fr2, result):
        self.lastOperation = '|{}/{}| {} |{}/{}| = |{}/{}|'.format(fr1.getNumerador(), fr1.getDenominador(), operation, fr2.getNumerador(), fr2.getDenominador(), result.getNumerador(), result.getDenominador())

    def setLastOperation1(self, fr1, operation, fr2, result):

        self.lastOperation = '{:<6.3f}         {:<6.3f}       {:<6.3f}      \n' \
                             '---------  {}  ---------  =  ---------     \n' \
                             '{:<6.3f}         {:<6.3f}       {:<6.3f}      \n'.format(
                                                                       fr1.getNumerador(),
                                                                       fr2.getNumerador(),
                                                                       result.getNumerador(),

                                                                       operation,

                                                                       fr1.getDenominador(),
                                                                       fr2.getDenominador(),
                                                                       result.getDenominador()

                                                                       )


    def getState(self):
        return ('[ a = {} | b = {} ]'.format(self.f1.getAB(), self.f2.getAB()))

    def getLastOperation(self):
        return self.lastOperation

    def soma(self):
        print('[op: SUM SAME BASE]')
        if self.f1.getDenominador() == self.f2.getDenominador():#Mesma base
            fresp1 = self.f1.getNumerador() + self.f2.getNumerador()
            fresp2 = self.f1.getDenominador()

            resp = Fracao(fresp1, fresp2)

        else:#Bases diferentes
            print('[op: SUM DIFFERENT BASES]')
            fresp2 = self.mmc(self.f1.getDenominador(), self.f2.getDenominador())
            fresp1 = ((fresp2/self.f1.getDenominador()) * self.f1.getNumerador()) + ((fresp2/self.f2.getDenominador()) * self.f2.getNumerador())

            resp = Fracao(fresp1, fresp2)

        self.setLastOperation(self.f1, '+', self.f2, resp)
        return resp

    def subtriai(self):
        print('[op: SUBTRACT SAME BASES]')
        if self.f1.getDenominador() == self.f2.getDenominador():  # Mesma base
            fresp1 = self.f1.getNumerador() + self.f2.getNumerador()
            fresp2 = self.f1.getDenominador()

            resp = Fracao(fresp1, fresp2)

        else:  # Bases diferentes
            print('[op: SUBTRACT DIFFERENT BASES]')
            fresp2 = self.mmc(self.f1.getDenominador(), self.f2.getDenominador())

            fresp1 = ((fresp2 / self.f1.getDenominador()) * self.f1.getNumerador()) - (
            (fresp2 / self.f2.getDenominador()) * self.f2.getNumerador())

            resp = Fracao(fresp1, fresp2)

        self.setLastOperation(self.f1, '-', self.f2, resp)
        return resp

    def multiplica(self):
        print('[op: MULT]')
        fresp1 = self.f1.getNumerador() * self.f2.getNumerador()
        fresp2 = self.f1.getDenominador() * self.f2.getDenominador()

        resp = Fracao(fresp1, fresp2)
        self.setLastOperation(self.f1, '*', self.f2, resp)
        return resp

    def divide(self):
        print('[op: DIV]')
        fresp1 = self.f1.getNumerador() * self.f2.getDenominador()
        fresp2 = self.f1.getDenominador() * self.f2.getNumerador()

        resp = Fracao(fresp1, fresp2)
        self.setLastOperation(self.f1, '/', self.f2, resp)
        return resp

    def mmc(self, num1, num2):
        print('[op: MMC]')
        a = num1
        b = num2

        resto = None
        while resto is not 0:
            resto = a % b
            a = b
            b = resto

        return (num1 * num2) / a


frac1 = Fracao(1, 2)
frac2 = Fracao(1, 4)
frac3 = Fracao()

frac1.printAB()
frac2.printAB()
frac3.printAB()

calculadora = AritméticaFracao(frac1, frac2)
print(calculadora.getLastOperation())

print('\nDIVISÃO')
print(calculadora.getState())
calculadora.divide()
print(calculadora.getLastOperation())

print('\nMULTIPLICAÇÃO')
print(calculadora.getState())
calculadora.multiplica()
print(calculadora.getLastOperation())

print('\nSOMA')
print(calculadora.getState())
calculadora.soma()
print(calculadora.getLastOperation())


print('\nSUBTRAÇÃO')
print(calculadora.getState())
calculadora.subtriai()
print(calculadora.getLastOperation())




