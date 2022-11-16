operacao = input()

matriz = [[float(input()) for i in range(12)] for j in range(12)]

soma = 0
cont = 0

for l in range(1, len(matriz)):
    soma += sum(matriz[l][0:l])

if operacao == "S":
    print(soma)
else:
    cont = 12 * 11 / 2
    print(round(soma / cont, 1))
