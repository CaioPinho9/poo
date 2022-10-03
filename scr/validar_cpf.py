cpf = input()


def verificador(numero):
    soma = 0
    peso = len(numero)
    digito = numero[-1:]
    for i in range(len(numero) - 1):
        soma += int(numero[i]) * peso
        peso -= 1
    dv = 11 - soma % 11
    if dv >= 10:
        dv = 0
    return dv == int(digito)


cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

verificado = len(cpf) == 11 and cpf.count(cpf[0]) != 11 and verificador(cpf) and verificador(cpf[:-1])

print(verificado)
