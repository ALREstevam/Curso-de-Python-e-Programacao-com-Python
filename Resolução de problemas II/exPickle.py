## NLTK
## INSTALAR ANACONDA 3
import sys, _pickle as Pickle

class BandMember:
     def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
     def __str__(self):
        return '{} na(o) {}'.format(self.name, self.instrument)

class FileMngr:
    def __init__(self, filePath='bandMembers.dat'):
        self.filePath = filePath

    def openfile(self, cons):
        try:
            return open(self.filePath, cons)
        except:
            print('File could not be opened.', file=sys.stderr)
            sys.exit(1)

    def openFileToWrite(self):
        return self.openfile('wb')

    def openFileToRead(self):
        return self.openfile('rb')

    def closefile(self, openedFile):
        openedFile.close()

    def set(self, bandMember):
        fileOpened = self.openFileToWrite()
        Pickle.dump(bandMember, fileOpened)
        self.closefile(fileOpened)

    def read(self):
        fileOpened = self.openFileToWrite()
        rsp = Pickle.load(fileOpened)  # recupera item armazenado
        self.closefile(fileOpened)
        return rsp


bnd0 = BandMember('Julio', 'Gaita')
bnd1 = BandMember('Bicharada', 'Vocal')
bnd2 = BandMember('Bicharada', 'Cococoral')

flm = FileMngr('bandMembers.dat')

flm.set(bnd0)
rsp = flm.read()
