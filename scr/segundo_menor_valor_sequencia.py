import math

n = int(input())
x = []

for i in range(n):
    x.append(int(input()))

menor = math.inf
segundo_menor = math.inf

for i in range(n):
    if menor > x[i]:
        menor = x[i]
    if segundo_menor > x[i] > menor:
        segundo_menor = x[i]

print(segundo_menor)