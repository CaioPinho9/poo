qnt_disc = int(input())
horas = ['0730', '0820', '0910', '1010', '1100', '1330', '1420', '1510', '1620', '1710', '1830', '1920', '2020', '2110']

quadro_de_horario = [[None] * 6 for _ in range(len(horas))]
choque = False

for _ in range(qnt_disc):
    disc, *horarios = input().split()

    for horario in horarios:
        dia_semana = int(horario[0])
        hora_inicio = horario[1:-1]
        n_aulas = int(horario[-1])

        col = dia_semana - 2
        lin = horas.index(hora_inicio)

        for n in range(n_aulas):
            if quadro_de_horario[lin + n][col] is None:
                quadro_de_horario[lin + n][col] = disc
            else:
                print(quadro_de_horario[lin + n][col], disc)
                choque = True
                break
        if choque:
            break
    if choque:
        break
