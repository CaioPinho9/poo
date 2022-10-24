num_postos, distancia_max = [int(x) for x in input().split()]
postos = [int(x) for x in input().split()]

consegue = True

for i in range(num_postos - 1):
    if postos[i + 1] - postos[i] > distancia_max:
        consegue = False
        break

print("S" if consegue else "N")
