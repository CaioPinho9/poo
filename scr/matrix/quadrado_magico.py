tam = int(input())

matriz = [[int(x) for x in input().split()] for _ in range(tam)]

magico = True
soma = sum(matriz[0])

for l in range(tam):
    if sum(matriz[l]) != soma:
        magico = False
        break

if magico:
    for c in range(tam):
        somatorio = 0
        for l in range(tam):
            somatorio += matriz[l][c]
        if somatorio != soma:
            magico = False
            break

if magico:
    somatorio = 0
    for i in range(tam):
        somatorio += matriz[i][i]
    if somatorio != soma:
        magico = False

if magico:
    somatorio = 0
    for i in range(tam):
        somatorio += matriz[i][tam - i - 1]
    if somatorio != soma:
        magico = False

print(magico)
