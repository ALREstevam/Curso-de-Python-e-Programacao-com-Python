numeros = []



def swap(numeros, a, b):
    aux = numeros[a]
    numeros[a] = numeros[b]
    numeros[b] = aux

for i in range(3):
    numeros.append(int(input('Digite o {}º número: '.format(i+1))))

if numeros[0] > numeros[1] and numeros[0] > numeros[2]:#primeiro é o maior

elif numeros[1] > numeros[2]:#segundo é maior

else:#terceiro é maior


