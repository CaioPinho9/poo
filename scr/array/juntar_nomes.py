tam1 = int(input())
list1 = []
for i in range(tam1):
    list1.append(input())

tam2 = int(input())
list2 = []
for i in range(tam2):
    list2.append(input())

list_final = list1 + list2

list_final = sorted(list(dict.fromkeys(list_final)))

for item in list_final:
    print(item)
