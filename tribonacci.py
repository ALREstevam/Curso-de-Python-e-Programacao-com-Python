numbers = [1, 1, 1, 1]
sms = len(numbers)

printSize = 50


for number in numbers:
    print(number)

for count in range(printSize):
    nsum = 0
    for i in range(sms):
        nsum += numbers[len(numbers) - i -1]
    numbers.append(nsum)
    print(nsum)
    
