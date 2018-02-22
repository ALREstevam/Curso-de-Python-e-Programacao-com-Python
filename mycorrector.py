# MYCORRECTOR

while (True):
    file = open("correcao.txt", "r+")
    print(file.read())
    file.close()

    correct =   str(input("PALAVRA CORRETA  : "))
    incorrect = str(input("PALAVRA INCORRETA: "))

    term = "{:20}\t->\te não: {:20}".format(correct, incorrect)

    print("DESEJA GRAVAR:")
    print(term)
    rsp = str(input("(s/n): "))

    if rsp == "s":
        print("GRAVANDO...");
        file = open("correcao.txt", "a")
        file.write(term)
        file.close()

    input()

    print("s para sair, enter para continuar: ")
    rsp = input("")

    if(rsp == "s"):
        break;
    






