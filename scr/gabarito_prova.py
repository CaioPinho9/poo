s1 = input()
s2 = input()

index = 0
acertos = 0
for d in s1:
    if d == s2[index]:
        acertos += 1
    index += 1

print(acertos)
