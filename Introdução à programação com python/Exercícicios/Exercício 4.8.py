num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
oper = input("Operação (+, -, /, *): ")
res = 0
err = False

if oper == '+':
    res = num1 + num2

elif oper == '-':
    res = num1 - num2

elif oper == '/':
    res = num1 / num2

elif oper == '*':
    res = num1 * num2
else:
    print("Entrada inválida")
    err = True

if err == False:
    print("Resultado {} {} {} = {}".format(num1, oper, num2, res))