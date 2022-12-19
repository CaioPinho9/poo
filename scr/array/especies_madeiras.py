n = int(input())

for _ in range(n):
  especies = dict()
  total = 0
  madeira = input()

  while madeira != "":
      if madeira in especies:
        especies[madeira] += 1 
      else:
        especies[madeira] = 1
      total += 1
      madeira = input()
      
  for madeira, qnt in sorted(especies.items()):
    propocao = qnt / total * 100
    print(madeira, f"{propocao:.4f}")
