n = int(input())
primo = [2, 3, 5]
i = 0

while i < 3:
    if n % primo[i] == 0:
        n *= 1 / primo[i]
    else:
        i += 1

print(n == 1)