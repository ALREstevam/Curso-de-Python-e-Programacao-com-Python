'''
Arrays são chamados de sequências

Tipos
    String
        s = 'texto'
    Lista
        São elementos mútáveis
        Podem ter elementos de diferentes tipos
        l = ['asa', 1]
    Tupla
        t = (1, 2, 3)


Tuplas e strings não são mutáveis


Mapping (relacionam chave ao valor)

Acesso
    Com números positivos e negativos

     0  1  2  3
    [] [] [] []
    -1 -2 -3 -4


Úteis

aList = []

for number in range(1,11):
    aList += [number] #Adiciona elementos na listas

    #Os dois elementos são listas

print(aList)

==============================================================

#Via elemento
for item in aList:
    print(item) #imprime todos os elementos da lista


#Via índice
for i in range(len(aList)):
    print(aList[i]) #imprime todos os elementos da lista


===============================================================
Histograma

values = [0] * 10 # cria uma lista com 10 valores iguais a zero
print('10 inteiros')

for i in range(10):
    newValue = int(input('Valor: '))


for i in range(len(values)):
    print(values[i] * '*')

==============================================================
Tuplas - lista que não pode ser mudada



currentHour = hour, minute, second

print(currentTime[0])

===============================================================
Desempacotar sequências

aString = 'abc'

first, second, third = aString

===============================================================
Slicing

sequencia[inicio : ]
sequencia[inicio : fim]
sequencia[ : fim]
sequencia[inicio : incremento : fim]

até fim-1
===============================================================
Dicionários

Coleção de valores associativos
Chave -> valor

dictionart = {}

dictionary = {1 : 'one', 2 : 'two'}

> Manipulando
nums = {1 : 'one', 2 : 'two'}

nums[3] = 'three' #adiciona ao dicionárioo
del nums[3] #removendo 3

nums[1] = 'ones' #alterando valor


===============================================================
Métodos = lista, tupla, dicionário (built-in types)

append(item)            Insere item no final da lista
count( elemento )       Retorna o número de ocorrencias de elemento na lista.
extend( newList )       Insere os elementos de newList no final da lista
index( elemento )       Returna o indice da primeira ocorrência de elemento na lista
insert( indice, item )  Insere item na posição indice
pop( [indice] )         Sem parametro – remove e retorna o último elemento da lista. Se indice é especificado, remove e retorna o elemento na posição indice.
remove( elemento )      Remove a primeira ocorrencia de elemento da lista.
reverse()               Inverte o conteúdo da lista
sort( [function] )      Ordena o conteúdo da lista.

===============================================================
Mpetodos de dicionário

clear()                     Apaga todos os item do dicionário
copy()                      Cria uma cópia do dicionário. Cópia referencia o dicionário original
get( key [, returnValue] )  Retorna o valor associado à chave. Se chave não está no dicionário e returnValue é dado, retorna-o.
has_key( key )              Returna 1 se a chave está no dicionário; 0 se não está.
items()                     Retorna uma lista de tuplas no formato chave-valor.
keys()                      Retorna uma lista das chaves do dicionário.
popitem()                   Remove e retorna um par arbitrário como uma tupla de dois elementos.
setdefault( key [,value] )  Se key não está no dicionário e value é especificado, insere o par key-value. Se value não é especificado, value é None.
update( newDictionary )     Adiciona todos pares chave-valor de newDictionary ao dicionário corrente e sobrescreve os valores para as chaves ja existentes.
values()                    Retorna uma lista de valores no dicionário.


for key in dicionario.keys():


from copy import deepcopy

copiaDistinta  = deepcopy(dictionary)


'''


list = ['a','b','c']
list.remove('a')
print(list)