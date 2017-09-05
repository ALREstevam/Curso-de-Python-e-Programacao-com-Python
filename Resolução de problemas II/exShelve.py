'''
Arquivo: ferramentas.dat
ID NOME QUANTIDADE CUSTO UN

Visualizar
Atualizar
Inserir
Remover

Você é dono de uma loja de ferramentas e deseja manter controle sobre o estoque.
Escreva um programa que inicialize um arquivo
shelve “ferramentas.dat”, que permita você inserir
os seguinte dados relativos às diversas
ferramentas:

ID Nome Quantidade Custo un.
34 Serra 25 12,00
45 Martelo 4 11,00

Escreva métodos para visualizar, atualizar valores,
inserir e remover itens do estoque

'''

import sys
import shelve



class Store:
    def __init__(self, ljust = 15, filePath = 'ferramentas.dat'):
        self.file = filePath
        self.ferramentas = []
        self.ljustNumber = ljust

    def openFile(self):
        try:
            ferramentas = shelve.open(self.file)
            return ferramentas
        except:
            print('File could not be opened.', file=sys.stderr)
            sys.exit(1)

    def closeFile(self, arquivoAberto):
        arquivoAberto.close()

    def readLine(self):
        id = str(input("ID: "))
        print("INSIRA:\nNome | Quantidade | Custo un. |")
        dados = str(input(": ")).split()

        return {'id': id, 'dados': dados}


    def add(self, arquivoAberto, res):
        arquivoAberto[res['id']] = res['dados']

        print(res['id'])
        print(res['dados'])

    def append(self, arquivoaberto):
        res = self.readLine()
        self.add(arquivoaberto, res)

    def formatLine(self, key, line):
        rsp = str(key.ljust(self.ljustNumber))
        for elem in line:
            rsp += elem.ljust(self.ljustNumber)

        return rsp

    def tableHeader(self):
        return 'ID'.ljust(self.ljustNumber) +\
               'Nome'.ljust(self.ljustNumber) +\
               'Quantidade'.ljust(self.ljustNumber) +\
               'Preço un.'.ljust(self.ljustNumber)

    def show(self, arquivoAberto):
        print(self.tableHeader())

        for i in range(4):
            print('-' * (self.ljustNumber), end='')
        print('')

        for ferrId in arquivoAberto.keys():
            print(self.formatLine(ferrId, arquivoAberto[ferrId]))

        for i in range(4):
            print('-' * self.ljustNumber, end='')
        print('')

    def removeByKey(self, arquivoAberto, keyToRemove):
        if keyToRemove in arquivoAberto:
            del arquivoAberto[keyToRemove]
            return True
        else:
            print("Registro não existe para ser removido.", file=sys.stderr)
            return False

    def remove(self, arquivoAberto):
        idFerr = str(input("Digite o id o produto a remover: "))
        if(self.removeByKey(arquivoAberto, idFerr)):
            print('Registro removido com sucesso.')


    def update(self, arquivoAberto):
        idFerr = str(input("Digite o id do produto a atualizar: "))

        if idFerr in arquivoAberto:
            print('-'*50)
            print(self.tableHeader())
            print(self.formatLine(str(idFerr), arquivoAberto[idFerr], ))
            print('-' * 50)

            print('Digite os dados atualizados')

            print("INSIRA:\nNome | Quantidade | Custo un. |")
            dados = str(input(": ")).split()

            rsp = {'id': idFerr, 'dados': dados}

            self.removeByKey(arquivoAberto, rsp['id'])
            self.add(arquivoAberto, rsp)

        else:
            print('Registro {} não existe.'.format(idFerr), file=sys.stderr)


    def venda(self, arquivoAberto):
        idFerr = str(input("Digite o id do produto a vendido: "))

        if idFerr in arquivoAberto:
            print('Você está vendendo {}.'.format(arquivoAberto[idFerr][0]))
            qtdVendida = int(input("Quantidade vendida: "))

            if int(arquivoAberto[idFerr][1]) >= qtdVendida:
                novaQtd = int(arquivoAberto[idFerr][1]) - qtdVendida
                dados = arquivoAberto[idFerr]
                dados[1] = str(novaQtd)
                self.removeByKey(arquivoAberto, idFerr)
                res = {'id': idFerr, 'dados': dados}
                self.add(arquivoAberto, res)

            else:
                print('Você não tem essa quantidade de {} para vender'.format(arquivoAberto[idFerr][0]))

        else:
            print('Registro {} não existe.'.format(idFerr), file=sys.stderr)

    def receber(self, arquivoAberto):
        idFerr = str(input("Digite o id do produto a recebido: "))

        if idFerr in arquivoAberto:
            print('Você está recebendo {}.'.format(arquivoAberto[idFerr][0]))
            qtdComprada = int(input("Quantidade vendida: "))

            novaQtd = int(arquivoAberto[idFerr][1]) + qtdComprada
            dados = arquivoAberto[idFerr]
            dados[1] = str(novaQtd)
            self.removeByKey(arquivoAberto, idFerr)
            res = {'id': idFerr, 'dados': dados}
            self.add(arquivoAberto, res)


        else:
            print('Registro {} não existe.'.format(idFerr), file=sys.stderr)

    def mudarPreco(self, arquivoAberto):
        idFerr = str(input("Digite o id do produto a ter o preço alterado: "))

        if idFerr in arquivoAberto:
            print('Você está alterando {} que custa R${:3.2f}.'.format(arquivoAberto[idFerr][0], arquivoAberto[2]))
            novoValor = int(input("Novo valor: R$"))

            dados = arquivoAberto[idFerr]
            dados[2] = str(novoValor)
            self.removeByKey(arquivoAberto, idFerr)
            res = {'id': idFerr, 'dados': dados}
            self.add(arquivoAberto, res)

        else:
            print('Registro {} não existe.'.format(idFerr), file=sys.stderr)





s = Store()
arq = s.openFile()


while(True):
    print('MENU - Escolha uma opção')

    options = (
        ('INSERT', 'Adicionar um produto'),
        ('UPDATE', 'Atualizar um produto'),
        ('DELETE', 'Remover um produto'),
        ('SELL', 'Registrar uma venda'),
        ('RECEIVE', 'Registrar um recebimento'),
        ('CHNGPRICE','Mudar o preço de um produto'),
        ('LEAVE','Sair')
    )

    i = 1
    for line in options:
        print('{:2}. {}.'.ljust(10).format(i, line[1]))
        i += 1

    opcao = int(input('Opção: '))

    if 0 < opcao < len(options)+1:
        optxt = options[opcao-1][0]

        if optxt == 'INSERT':
            s.append(arq)

        elif optxt == 'UPDATE':
            s.update(arq)

        elif optxt == 'DELETE':
            s.remove(arq)

        elif optxt == 'SELL':
            s.venda(arq)

        elif optxt == 'RECEIVE':
            s.receber(arq)

        elif optxt == 'CHNGPRICE':
            s.mudarPreco(arq)

        elif optxt == 'LEAVE':
            s.closeFile(arq)
            exit(0)

    else:
        print('Opção inválida')

