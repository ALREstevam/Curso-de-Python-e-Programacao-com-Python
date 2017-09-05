import random
import pprint

class ListRandom:

    def __init__(self):
        self.list = []


    def chooseOne(self, list):
        self.list = list
        return list[random.randint(0, len(list)-1)]

    def chooseOne(self, list, seed):
        random.seed = seed
        self.list = list
        return list[random.randint(0, len(list)-1)]

    def secureChooseOne(self, list):
        self.list = list
        secure_random = random.SystemRandom()
        return secure_random.choice(list)

    def setListSelectNotRepeating(self, list):
        self.list = list

    def selectNotRepeating(self):

        if len(self.list) == 0:
            return None

        selectedIndex = random.randint(0, len(self.list)-1)

        rsp = self.list[selectedIndex]
        self.list.remove(rsp)
        return rsp

    def secureSelectNotRepeating(self):

        if len(self.list) == 0:
            return None

        secure_random = random.SystemRandom()
        rsp = secure_random.choice(list)

        self.list.remove(rsp)
        return rsp

    def getList(self):
        return self.list

    def printList(self):
        pprint.pprint(self.list)


    def printList2(self):
        print('[',end='')
        for elem in self.list:
            print('{} '.format(elem), end='')

        print(']')





randl = ListRandom()
t = 'a b c d e f g h i j k'.split()
print(t)
randl.setListSelectNotRepeating(t)


randl.printList2()

for i in range(20):
    print(randl.list)
    print(randl.selectNotRepeating())




