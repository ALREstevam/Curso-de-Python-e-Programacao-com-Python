n1 = float(input('Nota da prova 1: '))
n2 = float(input('Nota da prova 2: '))

média = (n1 + n2)/2

print('Sua média foi {:.1f}'.format(média))

if média == 10:
    print('Ai sim!')
elif média >= 6.0:
    print('Tá valendo...')
else:
    print('Honre sua família!')
    
