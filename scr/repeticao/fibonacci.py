n = int(input())

n1 = 0
n2 = 1

x = 1

for i in range(1, n):
    x = n1 + n2
    n1 = n2
    n2 = x

print(x)
