#Ordem de apresentação
#sortear um dentre 4 alunos e mostrar o nome

from random import shuffle, random

alunosQtd = 5
alunos = []

#Lendo nome dos alunos
for i in range(alunosQtd):
    alunoNome = str(input("Nome do aluno {}: ".format(i + 1)))
    alunos.append(alunoNome)

random.shuffle(alunos)


for i in range(alunosQtd):
    print("{:2<} - {}".format(i+1, alunos[i]))

