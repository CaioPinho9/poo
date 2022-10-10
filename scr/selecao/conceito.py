n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3) / 3

if media >= 9:
    conceito = "Ótimo"
elif media >= 7.5:
    conceito = "Bom"
elif media >= 6:
    conceito = "Satisfatório"
else:
    conceito = "Insuficiente"

print(conceito)