s1 = input()
s2 = input()

anagrama = s1 != s2

s1_sorted = sorted(s1)
s2_sorted = sorted(s2)

anagrama = anagrama and s1_sorted == s2_sorted

print(anagrama)