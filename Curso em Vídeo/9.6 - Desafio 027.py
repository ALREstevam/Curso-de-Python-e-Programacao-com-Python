#mostrar o primeiro e último nome

nome = str(input("Nome: "))


print(nome[:nome.find(' ')])
print(nome[nome.rfind(' ') + 1:])



nome = nome.split()
if len(nome) > 0:
    print("Primeiro nome: {}\n"
      "Último nome: {}".format(nome[0], nome[len(nome) - 1])
    )
else:
    print("Você não digitou nada...")



