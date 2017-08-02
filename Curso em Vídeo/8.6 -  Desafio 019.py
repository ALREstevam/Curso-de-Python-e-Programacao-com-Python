#sortear um dentre 4 alunos e mostrar o nome
import random

alunosQtd = 4
aux = alunosQtd
escolhido = random.randint(0, alunosQtd - 1)
alunos = []

while alunosQtd > 0:
    alunoNome = input("Nome do aluno {}: ".format(aux - alunosQtd + 1))
    alunos.append(alunoNome)
    alunosQtd = alunosQtd - 1

print("O aluno {} foi escolhido".format(alunos[escolhido]))

