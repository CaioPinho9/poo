def encontrar_ventiladores(posisao, coluna_atual):
    i = 1
    forcaE = 0
    forcaD = 0
    if matrix[coluna_atual][posisao] != 0:
        return "BOOM " + str(posisao + 1) + " " + str(coluna_atual)

    while True:
        if posisao - i >= 0 and matrix[coluna_atual][posisao - i] != 0 and forcaE == 0:
            forcaE = matrix[coluna_atual][posisao - i]

        if posisao + i < c and matrix[coluna_atual][posisao + i] != 0 and forcaD == 0:
            forcaD = matrix[coluna_atual][posisao + i]

        if forcaE != 0 and forcaD != 0:
            return forcaE - forcaD
        i += 1


while True:
    l, c, p = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for y in range(l)]

    if l + c + p == 0:
        break

    p -= 1
    for i in range(l):
        force = encontrar_ventiladores(p, i)
        if isinstance(force, str):
            print(force)
            break
        p += force
        if p >= c:
            print("BOOM", p - force + 1, i)
            break
    else:
        print("OUT", p + 1)
