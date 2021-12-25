#!/usr/bin/env python3

from random import randrange as r

max = 20
total = 5
score = 0
def add():
    global score
    a = r(max + 1)
    b = r(max - a + 1)
    result = a + b
    print(a, ' + ', b, ' = ', end='')
    result_in = int(input())
    if result == result_in:
        score = score + 1

def sub():
    global score
    a = r(max + 1)
    b = r(a + 1)
    result = a - b
    print(a, ' - ', b, ' = ', end='')
    result_in = int(input())
    if result == result_in:
        score = score + 1

if __name__ == '__main__':
    for i in range(total):
        add()
        sub()
    total = total * 2
    print('you complete', total, 'exercises and get score ', score)

    print()