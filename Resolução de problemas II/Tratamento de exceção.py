'''
Lidar com exceções
    Tratar eventos especiais ao invés de retornar um erro
    Permitir que o programa continue rodando

raise permite que o usuário crie uma exceção

toda exceção é uma classe derivada da classe exception


raise exceçãoNome, "mensagem de erro";

try except

try finnaly
bloco finally é executado com ou sem exceção

'''
'''
def div(a, b):
    if b == 0:
        raise(ZeroDivisionError, "Não dividirás por zero")
    else:
        return a/b



def trye():
    a = 1
    b = 0

    try:
        print(div(a, b))
    except ZeroDivisionError:
        print('You shall not divide by zero.')



trye()
'''
'''
Arquivos

Python sempre cria um objeto e associa um fluxo de arquivo a ele

sytem.stdin




'''


import sys

registro = "xyz"

try:
    file = open('notas.dat', 'w')

except IOError:
 #print>>(file, registro)
 print(registro, end="", file=file)

"""
import sys
import shelve

shelve é como um dicinário pesistente com tamanhos fixos para cada registro
Toda chave se um shelve deve ser string


"""
