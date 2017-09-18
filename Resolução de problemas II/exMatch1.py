import re

exp1 = ['f(x) = log 4 + 3x',
        'f(y) = 34y - exp 3']

matchStr = '\w\(\w\)\s+=\s+(log|exp)?\s*\d+\w*\s[+,\-,\\,\*]\s(log|exp)?\s*\d+\w*'

for line in exp1:
    print(line)
    if re.match(matchStr, line):
        print('match')
    else:
        print('not match')