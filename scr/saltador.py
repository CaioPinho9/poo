n = int(input())

jogadores_distancia = []
jogadores_nome = []

for i in range(n):
    d1, d2, d3, nome = [w for w in input().split()]
    media = (int(d1) + int(d2) + int(d3)) / 3
    jogadores_distancia.append(media)
    jogadores_nome.append(nome)

maior = 0
nome = ""
for i in range(n):
    if maior < jogadores_distancia[i]:
        maior = jogadores_distancia[i]
        nome = jogadores_nome[i]

print(nome)