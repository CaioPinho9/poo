correta = '2002'
senha = ''

while senha != correta:
    senha = input()
    if senha == correta:
        print("Acesso Permitido")
        break
    print("Senha Invalida")


