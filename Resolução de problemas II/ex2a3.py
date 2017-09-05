'''
Use uma lista para resolver o seguinte
problema. Leia 20 números; a cada número
lido, imprima-o na tela apenas se este ainda
não foi lido.
'''



list = []

for i in range(5):
    lido = int(input('{}º número: '.format(i+1)))

    if list.count(lido) == 0: #não foi lido
        print(10*'#' + ' O valor [{}] não estava na lista.'.format(lido))
        list.append(lido)


print(list)