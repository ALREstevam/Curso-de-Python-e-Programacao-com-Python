def volume(comprimento = 1, largura = 1, altura = 1):
    return comprimento * largura * altura


print(volume())
print(volume(10))
print(volume(10, 11))
print(volume(10, 11, 12))

# volume(10, ,12) #causa error



