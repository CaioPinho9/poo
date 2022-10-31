while True:
    num_lin, num_col, pos = [int(x) for x in input().split()]
    boom = False

    if num_lin + num_col + pos == 0:
        break

    pos -= 1

    for lin in range(num_lin):
        compartimentos = [int(x) for x in input().split()]

        if not boom:
            i = pos
            while compartimentos[i] == 0:
                i -= 1
            j = pos
            while compartimentos[j] == 0:
                j += 1

            pos += compartimentos[i] - compartimentos[j]

            if pos <= i or pos >= j:
                print(f"BOOM {lin + 1} {max(min(pos, j), i) + 1}")
                boom = True
    if not boom:
        print(f"OUT {pos + 1}")
