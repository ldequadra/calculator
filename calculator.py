# **********************************************************************
#  Project           : Simple calculator with basic operations
#
#  Program name      : calculator.py
#
#  Author            : Luiz Claudio de Quadra (ldequadra)
#
#  Date created      : 27/08/2020
#
#  Purpose           : Improve the python programming skills
# **********************************************************************

import time

print('='*20)
print('{: ^20}'.format('CALCULATOR'))
print('='*20)

n1 = float(input('First number: '))
n2 = float(input('Second number: '))

op = int(input('''Choose an option:
[1] Add
[2] Subtract
[3] Multiply
[4] Divide
[5] Exit
Option: '''))

while op != 5:
    if op == 1:
        res = n1 + n2
        print('{} + {} = {}'.format(n1, n2, res))

    elif op == 2:
        print('''Do you want to calc:
        [1] {} - {}
        [2] {} - {}'''.format(n1, n2, n2, n1))
        sub_mode = int(input('Choose an option: '))
        if sub_mode == 1:
            res = n1 - n2
            print('{} - {} = {}'.format(n1, n2, res))
        else:
            res = n2 - n1
            print('{} - {} = {}'.format(n2, n1, res))

    elif op == 3:
        res = n1 * n2
        print('{} * {} = {}'.format(n1, n2, res))

    elif op == 4:
        print('''Do you want to calc:
            [1] {} / {}
            [2] {} / {}'''.format(n1, n2, n2, n1))
        div_mode = int(input('Choose an option: '))
        if div_mode == 1:
            res = n1 / n2
            print('{} / {} = {}'.format(n1, n2, res))
        else:
            res = n2 / n1
            print('{} / {} = {}'.format(n2, n1, res))

    print('The program will end in 10 seconds!')
    time.sleep(10)

    break
