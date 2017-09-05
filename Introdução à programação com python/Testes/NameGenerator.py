#Gerador de nomes

#'bcdfghjklmnpqrstvwxyz'
#'aeiou'

import random
class NameGenerator:
    def __init__(self, qtdNomesMax = 5, vogs='aiiiiooou', cons='bcdfghjklmnpqrstvwxyz', nameMinSize = 4, nameMaxSize = 7):
        self.qtdNome = qtdNomesMax
        self.vog = vogs
        self.con = cons
        self.qtdNomes = random.randint(nameMinSize, nameMaxSize)


    def genetateName(self):
        name = []
        each = bool(False)

        for i in range(self.qtdNomes):
            nameSize = random.randint(3, 7)
            for j in range(nameSize):

                if each:
                    vogSel = random.randint(0, len(self.vog) - 1)
                    name.append(self.vog[vogSel])
                else:
                    conSel = random.randint(0, len(self.con) - 1)
                    letterCons = self.con[conSel]

                    if letterCons == 'r' or letterCons == 's':
                        if random.randint(0, 2) == 2:
                            name.append(self.con[conSel])
                            name.append(self.con[conSel])
                        else:
                            name.append(self.con['*'])
                    else:
                        name.append(self.con[conSel])

                each = not each
            name.append(' ')

        name = (''.join(name)).title()
        return name

genNam = NameGenerator(5, 'bbbbcdfggghjklmmmmnnnnpqqrrrrrrrrsssssssttttvwxyz', 'aaaaaaaaaaaaaaaeeeeeeeeeeeeeiiiiiiooooouuu', 2, 7)
print(genNam.genetateName())

