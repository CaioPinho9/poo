lado1 = int(input())
lado2 = int(input())
lado3 = int(input())
lados = [lado1, lado2, lado3]
lados_iguais = 0

for i in range(3):
    for j in range(3):
        if i != j and lados[i] == lados[j]:
            lados_iguais += 1

if lados_iguais == 0:
    tipo = "Escaleno"
elif lados_iguais == 2:
    tipo = "Isosceles"
else:
    tipo = "Equilátero"
print(tipo)