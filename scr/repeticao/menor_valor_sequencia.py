import math

n = int(input())
x = []

for i in range(n):
    x.append(int(input()))

menor = math.inf
for i in range(n):
    if menor > x[i]:
        menor = x[i]

print(menor)