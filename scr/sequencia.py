n = []
while len(n) == 0 or n[len(n) - 1] != 0:
    n.append(int(input()))

for x in range(len(n)):
    for i in range(n[x]+1):
        if n[x] == 0:
            break
        if i == n[x]:
            print(i)
            break

        if i != 0:
            print(i, end=' ')

