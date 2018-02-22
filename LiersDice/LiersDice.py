from Jogador import *

jogadores = []
jogadores += [JogadorPC()]
jogadores += [JogadorPCInteligente()]
jogadores += [JogadorHumano()]


ultimoPalpite = 0
eliminado = False


print "Liers Dice"
while len(jogadores) > 1:  # termina quando restar um jogador na mesa

    for i in range(len(jogadores)):
        if ultimoPalpite == 0:
            for j in jogadores:
                j.jogaDados()
        jogada = jogadores[i].joga(ultimoPalpite)

        if jogada == "TURN":
            palpite = jogadores[i].getPalpite()
            faceDado = jogadores[i].getFaceDadoPalpite()
            ultimoPalpite = palpite
        elif jogada == "LIER":          #conta-se as faces dos dados referente ao palpite
            somaFaces = 0
            for j in jogadores:
                somaFaces += j.getDados().count(faceDado)
                j.mostraDados()
            if palpite <= somaFaces:
                jogadores[i].perdeuMao()
            else:
                if i == 0:
                    jogadores[len(jogadores)-1].perdeuMao()    # jogador anterior ganha
                else:
                    jogadores[i-1].perdeuMao()
            ultimoPalpite = 0

        elif jogada == "EVEN":
            somaFaces = 0
            for j in jogadores:
                somaFaces += j.getDados().count(faceDado)
                j.mostraDados()
            if palpite != somaFaces:
                jogadores[i].perdeuMao()
            else:
                for m in range(len(jogadores)):
                    if m <> i:
                        jogadores[m].perdeuMao()    #  todos jogador anterior ganha
            ultimoPalpite = 0

        if jogada == "LIER" or jogada == "EVEN":
            jogadores[0].dadosRestanteNaMesa -= 1
            for p in range(len(jogadores)):
                print "%s: " % jogadores[p].getId(),
                jogadores[p].mostraDados()
                if len(jogadores[p].getDados()) == 0:
                    print "Jogador %s eliminado" % jogadores[p].getId()
                    jogadores.pop(p)
                    eliminado = True

        if eliminado:
            eliminado = False
            break


print "Jogador %s venceu" % jogadores.getId()