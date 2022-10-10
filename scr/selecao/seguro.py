valor = float(input())
nacionalidade = input()
classe = input()
idade = int(input())

if nacionalidade == "nacional":
    premio = valor * 0.1
else:
    premio = valor * 0.15

if classe == "A":
    desconto = .3
elif classe == "B":
    desconto = .2
elif classe == "C":
    desconto = .1
elif classe == "D":
    desconto = .05
else:
    desconto = 0

premio *= 1-(desconto + 0.1)

print(round(premio, 2))