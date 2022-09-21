import math


def fatorial(n):
    fat = 1
    for i in range(n, 1, -1):
        fat *= n
    return fat


def elevado(n):
    return math.pow(n, 10)


x = 1
while True:
    if fatorial(x) > elevado(x):
        print(x)
        break
    else:
        x += 1
