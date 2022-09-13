x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x3 = x2 - x1
y3 = y2 - y1

move = abs(x3) <= 2 and abs(y3) <= 2 and x3 + y2 == 3

print(move)