# Manipulando texto
## Fatiamento

frase = "Curso em Vídeo Python"

print(frase)
print(frase[9])

print(frase[9:13]) #do 'V' até o antes do 'o'
print(frase[9:250]) #não é a melhor maneira de fatiar

print(frase[9:21:2]) #do 9 ao 21 pulando de 2 em 2

print(frase[:5])
print(frase[15:])

print(frase[9::3])

## Análise

print('Comprimento: ', len(frase))
print('Letras "o": ', frase.count('o'))

print('Contagem de "o" com fatiamento: ', frase.count('o', 0, 13))
print('Busca por deo: ', frase.find('deo'))
print('Busca por Android', frase.find('Android'))
print('Existe "Curso" ? ', 'Curso' in frase)

## Transformação


print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #primeira letra maiúscula
print(frase.title()) #Toda primeira letra em maiúscula

frase = "   Aprenda python   "
print(frase)

#Remover espaços no começo e no final da string
print(frase.strip())

#rstrip right strip
#lstrip left strip

print(frase.rstrip())
print(frase.lstrip())

#Divisão
frase = "Curso em Vídeo Python"

fraseSplit = frase.split()
print(fraseSplit)
print('-'.join(fraseSplit))


print('''
Texto longo multilinha
Texto longo multilinha
Texto longo multilinha
Texto longo multilinha
Texto longo multilinha
''')

#Strings são imutáveis, os métodos irão retornar uma nova string

frase = "Oi"
frase = frase.replace('Oi', 'OIEEE!!!')

