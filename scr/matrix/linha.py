l = int(input())
operacao = input()

matriz = [[float(input()) for i in range(12)] for j in range(12)]

soma = 0

for c in range(len(matriz)):
    soma += matriz[l][c]

if operacao == "S":
    print(soma)
else:
    print(soma/len(matriz))
