soma = 0
digitados = 0

while True:
    num = int(input('Digite um número (0 para sair): '))
    if num == 0:
        break
    digitados = digitados + 1
    soma = soma + num

print('Foram digitados {} números, a soma é {} e a média aritmética é {}'.format(digitados, soma, soma/digitados))