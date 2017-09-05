tabuadaDe = int(input("Tabuada do: "))
tabuadaInício = int(input("Início da tabuada: "))
tabuadaFim = int(input("Fim da tabuada: "))


while tabuadaInício <= tabuadaFim:
    print('{:<3} x {:>3} = {}'.format(tabuadaDe, tabuadaInício, tabuadaDe * tabuadaInício))
    tabuadaInício = tabuadaInício + 1
