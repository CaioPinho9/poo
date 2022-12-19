tam_lin, tam_col = [int(x) for x in input().split()]

matriz = [[int(x) for x in input().split()] for _ in range(int(tam_lin))]

direcao = input()

deslocamento_col = -1 if direcao == "esquerda" else 0
deslocamento_lin = -1 if direcao == "frente" else 0

nova_matrix = [[int(0) for _ in range(tam_col)] for _ in range(int(tam_lin))]

for lin in range(tam_lin):
  for col in range(tam_col):
    nova_lin = lin + deslocamento_lin
    nova_col = col + deslocamento_col
    
    nova_matrix[nova_lin][nova_col] = matriz[lin][col]
    
for lin in range(tam_lin):
  print(*nova_matrix[lin])
