from random import randint

print('Pensando num número entre 0 e 5...')
num = randint(0, 5)
print('Pensei!')

tent = int(input('Tente advinhar: '))

if tent == num:
    print('**** Acertou. ****')
else:
    print('Perdeu, era  {}'.format(num))


