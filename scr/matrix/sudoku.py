n = int(input())

for i in range(n):

    tabuleiro = [[int(x) for x in input().split()] for _ in range(9)]

    sudoku = True

    for lin in range(9):
        c = set(tabuleiro[lin])
        if len(c) != 9:
            sudoku = False
            break

    if sudoku:
        for col in range(9):
            c = set(tabuleiro[lin][col] for lin in range(9))
            if len(c) != 9:
                sudoku = False
                break

    if sudoku:
        for lin in range(0, 9, 3):
            for col in range(0, 9, 3):
                c = set(tabuleiro[lin][col:col + 3] + tabuleiro[lin + 1][col:col + 3] + tabuleiro[lin + 2][col:col + 3])
                if len(c) != 9:
                    sudoku = False
                    break
    print("Instancia", i+1)
    print("SIM" if sudoku else "NAO")
