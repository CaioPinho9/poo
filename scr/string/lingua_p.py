s = input()

for i in range(len(s) - 1):
    if i < len(s) - 1 and s[i] == "p":
        s = s[:i] + s[i+1:]
    if i < len(s) - 1 and s[i + 1] == " ":
        i += 1
print(s)

