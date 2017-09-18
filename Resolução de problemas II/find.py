with open('brmxmlwhttags.txt', 'r') as myfile:
    str = myfile.read()

str = str.splitlines()
strmode = '[naosei]'

for line in str:
    if line.startswith('TipoAtributo'):
        strmode = 'ATRIBUTO'

    elif line.startswith('EntidadeAssociativa'):
        strmode = 'ENTIDADE ASSOCIATIVA'

    elif line.startswith('Entidade'):
        strmode = 'ENTIDADE'

    elif line.startswith('Relacionamento'):
        strmode = 'RELACIONAMENTO'

    elif line.startswith('Cardinalidade'):
        strmode = 'CARDINALIDADE'

    if line.startswith('Texto'):
        line = line.replace('Texto ', '')
        print('{}: \"{}\"'.format(strmode, line))
