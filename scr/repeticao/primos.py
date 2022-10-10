import math

numero = int(input())

maiorDivisiorPossivel = math.floor(math.sqrt(numero))

primo = True

if numero == 1:
    primo = False
elif numero == 2:
    primo = True
elif numero % 2 == 0:
    primo = False
else:
    for i in range(3, maiorDivisiorPossivel + 1, 2):
        if numero % i == 0:
            primo = False
            break

print(primo)
