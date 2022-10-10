numero = float(input())

notacao = "{:.4e}".format(numero)

if numero > 0:
    notacao = "+" + notacao
print(notacao.upper())