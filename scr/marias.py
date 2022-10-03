n = int(input())
s = []
maria = 0

for _ in range(n):
    s.append(input())

for i in range(len(s)):
    if "Maria" in s[i] and not "Mariana" in s[i]:
        maria += 1

print(maria)
