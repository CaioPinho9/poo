n = int(input())

jogadores_distancia = []
jogadores_nome = []

for i in range(n):
    d1, d2, d3, nome = [w for w in input().split()]
    melhor = d1 if float(d1)>float(d2) else d2
    melhor = d3 if float(d3)>float(melhor) else melhor
    jogadores_distancia.append(float(melhor))
    jogadores_nome.append(nome)

maior = 0
nome = ""
for i in range(n):
    if maior < jogadores_distancia[i]:
        maior = jogadores_distancia[i]
        nome = jogadores_nome[i]

print(nome)