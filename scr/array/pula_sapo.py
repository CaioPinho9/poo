limite, qtdade = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]
gameOver = False

if len(alturas) == qtdade:
    for i in range(len(alturas) - 1):
        if alturas[i + 1] - alturas[i] > limite:
            gameOver = True
            break
else:
    gameOver = True

if gameOver:
    print("GAME OVER")
else:
    print("YOU WIN")
