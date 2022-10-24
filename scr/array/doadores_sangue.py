tam1 = int(input())
calouros = []
for i in range(tam1):
    calouros.append(input())

tam2 = int(input())
doadores = []
for i in range(tam2):
    doadores.append(input())

calouros_doadores = 0
for calouro in calouros:
    if calouro in doadores:
        calouros_doadores += 1

print(calouros_doadores/tam1)