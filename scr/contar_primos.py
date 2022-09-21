import math

x = int(input())
y = int(input())

contador = 0

for n in range(x, y):
    maiorDivisiorPossivel = math.floor(math.sqrt(n))

    primo = True

    if n == 1:
        primo = False
    elif n == 2:
        primo = True
    elif n % 2 == 0:
        primo = False
    else:
        for i in range(3, maiorDivisiorPossivel + 1, 2):
            if n % i == 0:
                primo = False
                break

    if primo:
        print(n)
        contador += 1

print(contador)