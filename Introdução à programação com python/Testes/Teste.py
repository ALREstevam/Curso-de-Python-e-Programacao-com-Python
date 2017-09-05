hojeDia = 31
hojeMes = 8
hojeAno = 17

pessoaGrupo = 7

identPessoaHoje = (hojeDia + hojeMes + hojeAno + pessoaGrupo*10) % 100

print("Ident pessoa: {}".format(identPessoaHoje))

cores = ["preto", "branco", "azul", "amarelo", "vermelho", "verde", "laranja"]
coresMax = len(cores)

sorte = ["10", "20", "30", "40", "50", "60", "70", "80", "90"]
sorteMax = len(sorte)

dizeres = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "J.", "K."]
dizeresMax = len(dizeres)

calcCor = identPessoaHoje % coresMax
calcSorte = (identPessoaHoje + calcCor) % sorteMax


diz = []

diz.append((identPessoaHoje + calcSorte) % dizeresMax)
diz.append((identPessoaHoje + calcSorte + diz[0]) % dizeresMax)
diz.append((identPessoaHoje + calcSorte + diz[0] + diz[1]) % dizeresMax)
diz.append((identPessoaHoje + calcSorte + diz[0] + diz[1] + diz[2]) % dizeresMax)

countDiz = 0
countPart = 0

while diz[0] == diz[1] or diz[0] == diz[2] or diz[0] == diz[3]\
        or diz[1] == diz[2] or diz[1] == diz[3]\
        or diz[2] == diz[3]\
        :
    countDiz += 1
    countPart = (countPart + 1) % 3

    diz[countPart] += countDiz % len(diz)


print(10 * "---")
print("Cor: {}\nSorte: {}\n{}{}{}{}".format(cores[calcCor], sorte[calcSorte], dizeres[diz[0]], dizeres[diz[1]], dizeres[diz[2]], dizeres[diz[3]]))




