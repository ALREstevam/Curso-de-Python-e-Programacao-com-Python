#nome de cidade começa com santo?

cidadeInput = str(input('Nome da cidade: ')).strip().lower()

#Modo 1
cidade = cidadeInput.split()
print('O nome da cidade começa com "Santo"?    :  {}'.format(cidade[0] == 'santo'))

#Modo 2
print('O nome da cidade começa com "Santo"?    :  {}'.format(cidadeInput.find('santo') == 0))

#Modo 3
print('O nome da cidade começa com "Santo"?    :  {}'.format(cidadeInput[:5] == 'santo'))


