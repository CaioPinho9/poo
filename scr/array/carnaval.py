notas = [float(x) for x in input().split()]

notas.sort()

resultado = 0

for i in range(1, len(notas) - 1):
    resultado += notas[i]

print(round(resultado, 1))
