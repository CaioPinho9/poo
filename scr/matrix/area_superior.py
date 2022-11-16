operacao = input()

matriz = [[float(input()) for i in range(12)] for j in range(12)]

soma = 0

for l in range(len(matriz)):
    for c in range(l+1, len(matriz)-l-1):
        soma += matriz[l][c]
    #soma += sum(matrix[l][l+1:10-l]

if operacao == "S":
    print(soma)
else:
    cont = (2+10) * 5 / 2
    print(soma/cont)
