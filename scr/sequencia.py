n = int(input())

for i in range(n+1):
    if n == 0:
        print("")
        break
    if i == n:
        print(i, end='')
        break

    if i != 0:
        print(i, end=' ')

