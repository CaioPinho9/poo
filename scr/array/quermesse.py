num = int(input().strip())
cont = 1
while num != 0:
    teste = 0
    lista = [int(x) for x in input().split()]
    for index in range(len(lista)):
        if lista[index] == index + 1:
            teste = lista[index]
            break
    print("Teste", cont)
    print(teste)
    cont += 1
    num = int(input().strip())
