ano = int(input('Digite um ano: '))
bissexto = bool(False)

if ano % 4 == 0:
    bissexto = True
elif ano % 4 == 0 and (ano % 100) is not 0:
    bissexto = True

print('O ano {} '.format(ano), end='')

if bissexto:
    print('é bissexto')
else:
    print('não é bissexto')