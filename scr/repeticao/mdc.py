valor1 = int(input())
valor2 = int(input())

dividido = True
divisor = 2
mdc = 1

while (dividido):
    if valor1 % divisor == 0 and valor2 % divisor == 0:
        mdc *= divisor
    valor1 *= 1/divisor if valor1 % divisor == 0 else 1
    valor2 *= 1/divisor if valor2 % divisor == 0 else 1
    if valor1 == 1 and valor2 == 1:
        dividido = False
    if valor1 % divisor != 0 and valor2 % divisor != 0:
        divisor += 1
print(mdc)