#Ordem de apresentação
#sortear um dentre 4 alunos e mostrar o nome

import random

alunosQtd = 5
alunos = []
ordemApresent = []

#Lendo nome dos alunos
for i in range(alunosQtd):
    alunoNome = input("Nome do aluno {}: ".format(i + 1))
    alunos.append(alunoNome)

print("Ordem de apresentação:")
for i in range(alunosQtd):
    escolhido = random.randint(0, len(alunos) - 1)
    ordemApresent.append(alunos[escolhido])
    alunos.pop(escolhido)

    print("{:2<} - {}".format(i+1, ordemApresent[i]))











