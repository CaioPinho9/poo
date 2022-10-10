while True:
    vezes = int(input())
    if vezes == 0: break
    jogo = [int(x) for x in input().split(" ")]
    print(f"Mary won {jogo.count(0)} times and John won {jogo.count(1)} times")

