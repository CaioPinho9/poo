tam_lin, tam_col = [int(x) for x in input().split()]

matriz = [[int(x) for x in input().split()] for _ in range(int(tam_lin))]

alvo_lin, alvo_col = [int(x)-1 for x in input().split()]

soma = 0
for lin in range(tam_lin):
  for col in range(tam_col):
    if abs(alvo_lin - lin) <= 1 and abs(alvo_col - col) <= 1 and (abs(alvo_lin - lin) != 0 and abs(alvo_col - col) != 0):
      print(lin, col)
      soma += matriz[lin][col]
      
soma *= 1/8
print(f'{soma:.3f}')