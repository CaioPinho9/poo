tam_lin, tam_col = [int(x) for x in input().split()]

matriz = [[int(x) for x in input().split()] for _ in range(int(tam_lin))]

lin, col = [int(x) - 1 for x in input().split()]

soma = 0
for valor in range(tam_col):
  soma += matriz[lin][valor]

for valor in range(tam_lin):
  soma += matriz[valor][col]
    
print(soma)