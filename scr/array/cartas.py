cartas = [int(x) for x in input().split()]

cres = False
decr = False
not_ord = False

for i in range(len(cartas) - 1):
    if cartas[i] > cartas[i + 1]:
        decr = True
    elif cartas[i] < cartas[i + 1]:
        cres = True
    if cres and decr:
        not_ord = True
        break

if not_ord:
    print("N")
elif decr:
    print("D")
else:
    print("C")
