matriz = [[int(x) for x in input().split()] for _ in range(12)]
resultado = ""

for mes in matriz:
    media = sum(mes) / len(mes)
    resultado += format(media, '.2f') + " "

print(resultado)