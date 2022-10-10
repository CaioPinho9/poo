n = int(input())
m = int(input())
i = 1

while n * i <= m:
    s = n * i
    print(str(s), end=' ')
    i += 1
