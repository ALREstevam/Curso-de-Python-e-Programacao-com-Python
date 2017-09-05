'''

                                                                          -/ooyhddyo+-`
                                                                     `/ydhsssyyyyyyyyhy+:
                                                                   :ydhyy+::::+syyyyyyyyyho:
                                                                 /hdyyys//+ossyysssyyyyyyyyyy/`
                                                               .hdhyyyyhso+++oosysosssyyyyyyyyy:
                                                              +mhyyyyyyhoooo++//-:oysssyyyyyyyyyo`
                                                            `ydyyyyyyyssssssssssys+-/ysyyyyyyyyyys`
                                                           `hdyyyhysooossosssssssssy+.oyyyyyyyyyyyo
                                                          .dhyyhy:``  ``:oyossssssssyo.shyyyyyyyyyh.
                                                         .dhyyyy`  .-    `:ysssosssssyo+dyyyyyyyyyy+
                                                        -dhyyyh+   `-      hso+++oossossyyyyyyyyyyyy
                                                       -dhyyyyys          /o.`    `./ysyyyyyyyyyyyyy
                                                      :dhyyyyshy+.      .o+     `    -hyyyyyyyyyyyyy
                                                     +dhyhhyyyyhyyo+///osd.    .s`    hyyyyyyyyyyyyy
                                                   `sdyhdhhdddhyyyyshhsssyo`    `    -dyyyyyyyyyyyyo
                                                  .hdyymyNMMMMsdsoshyosyssso-`     ./hyyyyyyyyyyyyd-
                                                 -dhyyhdhMMMMMMoohshyyyssssysso+/+syhyyyyyyyyyyyyyy
                                                :dhyyyydyMMMMMMNm:oyyssssssyyyysshhyyyyyyyyyyyyyyd-
                                               /dhyyyyyyydNNMMMMNdNodd/mosmhhyssyyyyyyyyyyyyyyyyhs
                                              +dyyyyyysoyhhymNMMMMMMMNNMNNMNMNmyhdyyyyyyyyyyyyyyd`
                                             odhddhyyysssshdyhshMNMMMNmddmNMMMMMdmyyyyyyyyyyyyyd:
                                            sdyddhyyyyssssosyyshs/NmMMMNdhdNMMMMmdhyyyyyyyyyyyhs
                                          `sdyyyhyyyysssssssssssssh:ms+NmhhmMMMNhdyyyyyyyyyyyyh`
                                         `ydyyyyyyyyysssssssssssssssyoohomdmNmdddyyyyyyyyyyyyd-
                                        `yhyyyyyyyyyssssssssssssssssssssshdddhhyyyyyyyyyyyyyd:
                                       `hhyyyyyyyyyysssssssssssssssssssyyyyyyyyyyyyyyyyyyyyd/
                                      .hhyyyyyyyyyysssssssssssssssssssyyyyyyyyyyyyyyyyyyyyho
                                     .dhyyyyyyyyyyssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyhs
                                    -dhyyyyyyyyyyssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyhh`
                                   :dyyyyyyyyyyyssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyd.
                                  odyyyyyyyyyyyysssssssssssssossyyyyyyyyyyyyyyyyyyyyyyyd-
                                `yhyyyyyyyyyyyssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyd-
                               -dhyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyd-
                              +dyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyd-
                            `yhyhhyyyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyd:
                           :dhyddhyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyh/
                         `shyyyyhyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyhhyyyyyyyho
                        -hhyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyhdmdyyyyyyhs
                      `ohyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyhhhyyyyyyhy`
                     /hhyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhy`
                   -shyyyyyyyyyyyysssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyhs`
                 -shyyyyyyyyyyyyysssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyd+
               .ohyyyyyyyyyyyyyysssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyd/
             `+hhyyyyyyyyyyyyyysssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyd:
            :yhyyyyyyyyyyyyyysssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyhh.
          `ohyyyyyyyyyyhddhssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhy.
         -yhyyyyyyyyyyyddhsssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhs`
       `+hydddhyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyd+
      .yhyydddhyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhd:
     :hhyyyyhyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhh-
    /dyyyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhs`
   /dyyyyyyyyyyyyssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhh/
  :dyyyyyyyyyyyysssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhdo`
 `dhyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhds-
 sdyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhy:
`myyyyyyyyyyysssssssssssyyyyyyyyyyyyyyyyyhdddhyyyyyyyyyyhh/`
/dyyyyyyyyyyysssssssssyyyyyyyyyyyyyyyyyyydmmdhyyyyyyyyhh+`
shyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhyyyyyyyhho.
yhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhs.
yhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhs.
/dyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhs.
`dhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhho.
 .dhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhho.
  `odhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhy/`
    `+ydhyyyyyyyyyyyyyyyyyyyyyyyyyyhdhs+.                                               `
       `:+yhdhyyyyyyyyyyyyyyyyhddyo/.
            `-/+ssyyhhhyhyyso/:.



Crie quatro membros da classe BandMember. Use
o módulo Pickle para armazenar estes objetos em
um arquivo.
Crie um método que leia o arquivo e imprima os
nomes gravados

class BandMember:

 def __init__( self, name, instrument ):
self.name = name
self.instrument = instrument
 def __str__( self ):
 return "%s toca %s" % ( self.name, self.instrument )

'''

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
