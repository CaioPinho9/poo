nome = [str(x) for x in input().split()]

nome_abreviado = nome[0]

for i in range(1, len(nome) - 1):
    nome_abreviado += " "
    if len(nome[i]) > 3:
        nome_abreviado += nome[i][0] + "."
    else:
        nome_abreviado += nome[i]

nome_abreviado += " " + nome[-1]

print(nome_abreviado)
