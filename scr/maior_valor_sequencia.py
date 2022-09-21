import math

n = int(input())
x = []

for i in range(n):
    x.append(int(input()))

maior = 0
posicao = 0
for i in range(n):
    if maior < x[i]:
        maior = x[i]
        posicao = i+1

print(maior, posicao)