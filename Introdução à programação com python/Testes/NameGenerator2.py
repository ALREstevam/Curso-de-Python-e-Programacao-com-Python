import random

class NameGenerator:
    def __init__(self, vowels='aeiou', consonants='bcdfghjklmnpqrstvwxyz', minNames=2, maxNomes=4, nameMinSize=3, nameMaxSize=7, separator = ' '):
        self.setParams(vowels, consonants, minNames, maxNomes, nameMinSize, nameMaxSize, separator)

    def setDefaultParams(self):
        self.maxNomes       = 5
        self.minNames       = 2
        self.vowels         = 'aeiou'
        self.consonants     = 'bcdfghjklmnpqrstvwxyz'
        self.nameMinSize    = 3
        self.nameMaxSize    = 7
        self.name           = []
        self.separator      = ' '
        self.order          = []


    def setParams(self, vowels, consonants, minNames, maxNomes, nameMinSize, nameMaxSize, separator):
        self.maxNames       = maxNomes
        self.minNames       = minNames
        self.vowels         = vowels
        self.consonants     = consonants
        self.nameMinSize    = nameMinSize
        self.nameMaxSize    = nameMaxSize
        self.name           = []
        self.separator      = separator
        self.order          = []

    def getOrder(self):
        return self.order

    def printOrder(self):
        for i in range(len(self.order)-2):
            print(self.order[i], end=''),
        #print('\n')

    def generate(self):
        self.name = []
        self.order = []
        letterType = bool(random.randint(0, 1))
        namesAmount = random.randint(self.minNames, self.maxNames)


        for nameCount in range(namesAmount):
            nameSize = random.randint(self.nameMinSize, self.nameMaxSize)
            for letterCount in range(nameSize):

                #Inserir uma vogal
                if letterType:
                    self.name.append(self.vowels[random.randint(0, len(self.vowels)-1)])
                    self.order.append(1)

                #Inserir uma consoante
                else:
                    conSel = random.randint(0, len(self.consonants) - 1)
                    letterCons = self.consonants[conSel]

                    if letterCons == 'r' or letterCons == 's':
                        if random.randint(0, 3) == 2:
                            self.name.append(letterCons)
                            self.name.append(letterCons)

                            self.order.append(2)
                            self.order.append(2)

                        else:
                            self.name.append(letterCons)
                            self.order.append(3)
                    else:
                        self.name.append(letterCons)
                        self.order.append(1)

                letterType = not letterType
            self.name.append(' ')
            self.order.append(4)

        strname = (''.join(self.name)).title()
        return strname

#nameGen = NameGenerator()
#vowels='aeiou', consonants='bcdfghjklmnpqrstvwxyz', minNames=2, maxNomes=4, nameMinSize=3, nameMaxSize=7, separator = ' '):
#nameGen = NameGenerator('aaaaaaaaaaaaeeeeeeeeiiiiiioooouu', 'bbbbbbbbccccccddddddfffggggghhhhhjjjjlllmmmnnnpppqqqrrrrrrrrrrrsssssssssssttttvvvvvkwxyz',
#                       3, 5, 2, 10, ' ')

nameGen = NameGenerator('a', 'bbbrr',
                       1, 1, 8, 8, ' ')


'''
for i in range(10000):
    print()


for i in range(20):
    nome = nameGen.generate()
    #print(nameGen.printOrder())
    print('[ {}]'.format(nome))
'''


isIn = False
nome = str('')
while isIn != True:

    nome = nameGen.generate()
    print(nome)
    if 'Barbara' in nome:
        print(nome)
        break
