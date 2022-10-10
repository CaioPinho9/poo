s1 = input()
s2 = input()

s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")

print((s1 == s2[::-1]))
