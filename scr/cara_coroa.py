n = int(input())
while (n != 0):
    mary = 0
    john = 0
    jogos = input()
    jogos = jogos.replace(" ", "")
    for j in jogos:
        if int(j) == 0:
            mary += 1
        else:
            john += 1
    n = int(input())
    print("Mary won " + str(mary) + " times and John won " + str(john) + " times")

