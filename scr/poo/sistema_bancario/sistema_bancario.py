from banco import Banco

bc = Banco("Banco do Brejo", 999)

nj = bc.abre_conta("Joãozinho", 23456)
nm = bc.abre_conta("Mariazinha", 23456)
nd = bc.abre_conta("Mariazinha", 2333)
na = bc.abre_conta("Mariazinha", 2346)



bc.deposito(nj, 100)
bc.deposito(nm, 250)
bc.saque(nj, 50)
bc.transferencia(nm, nj, 20)

bc.cpfs_duplicados()

print(bc.saldo(nj))
print(bc.saldo(nm))