import math

n = int(input())
media = 1

for _ in range(n):
    media *= float(input())

media = math.pow(media, 1 / n)
print(media)
