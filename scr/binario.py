import math

decimal = int(input())
binario = ''

while decimal > 0:
    binario += str(0 if decimal % 2 == 0 else 1)
    decimal *= 1/2
    decimal = math.floor(decimal)

print(binario[::-1])