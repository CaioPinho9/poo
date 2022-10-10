import math

n = int(input())
caixa = {}
notas = []

for i in range(n):
    valor = float(input())
    qntd = int(input())
    caixa[int(valor)] = qntd

valor_retirado = float(input())

for nota in reversed(caixa.keys()):
    nota_retirada = math.floor(valor_retirado / nota)
    max_retirado = caixa[nota]

    if nota_retirada > max_retirado:
        nota_retirada = max_retirado

    if nota_retirada > 0:
        notas.append(round(nota_retirada))
        valor_retirado -= nota_retirada * nota
    else:
        notas.append(0)

resposta = ""
for nota in notas:
    resposta += str(nota) + " "

print(resposta[::-1].strip(" "))

