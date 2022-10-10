def verificador(numero):
    soma = 0
    peso = len(numero)
    for i in range(len(numero) - 1):
        soma += int(numero[i]) * peso
        peso -= 1
    dv = 11 - soma % 11
    if dv >= 10:
        dv = 0
    return dv == int(numero[-1])


n = input()

print(verificador(n))
