maquina1 = [int(x) for x in input().split()]
maquina2 = [int(x) for x in input().split()]

compativel = True

for i in range(len(maquina1)):
    if maquina1[i] + maquina2[i] != 1:
        compativel = False
        break

print("Y" if compativel else "N")
