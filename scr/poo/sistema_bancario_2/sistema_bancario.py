from banco import Banco

bc = Banco("Meu Primeiro Banco", 999)
num_cta_joaozinho = bc.abre_conta_pf('Joazinho', 123)
print(num_cta_joaozinho)

num_cta_cia = bc.abre_conta_pj('Cia e Cia', 8982234)
bc.deposito(num_cta_cia, 100000)
print(num_cta_cia)

num_cta_mariazinha = bc.abre_conta_pf('Mariazinha', 456)
print(num_cta_mariazinha)

bc.deposito(num_cta_joaozinho, 100)
bc.deposito(num_cta_mariazinha, 250)
bc.saque(num_cta_joaozinho, 50)
bc.transferencia(num_cta_mariazinha, num_cta_joaozinho, 20)

saldo = bc.saldo(num_cta_joaozinho)
if saldo == False:
    print("Conta inexistente")
else:
    print(f"Saldo da conta {num_cta_joaozinho} = {saldo}")
    
print(f"Saldo da conta {num_cta_mariazinha} = {bc.saldo(num_cta_mariazinha)}")

n_conta = 789
print(f"Saldo da conta {n_conta} = {bc.saldo(n_conta)}")

print("Conta maior saldo", bc.conta_pf_maior_saldo())
