import math

num = int(input().strip())

for i in range(num):
    qnt_alunos, numero = [int(x) for x in input().split()]
    alunos = [int(x) for x in input().split()]
    diferenca = math.inf
    valor = 0
    for aluno in alunos:
        if abs(numero - aluno) < diferenca:
            diferenca = abs(numero - aluno)
            valor = aluno
    print(alunos.index(valor))
