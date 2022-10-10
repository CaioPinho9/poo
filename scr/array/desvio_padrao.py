import math

n = int(input())
sequencia = [float(input()) for _ in range(n)]

media = sum(sequencia) / n

soma = sum([(x - media) ** 2 for x in sequencia])
desvio = math.sqrt(soma / (n - 1))

print(desvio)
