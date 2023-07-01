salario  = float(input("Digite o valor do salario: "))
valor_cheque1  = float(input("Digite o valor do 1° cheque: "))
valor_cheque2 = float(input("Digite o valor do 2° cheque: "))

imposto_cheque1 = valor_cheque1 * 0.38 / 100
saque1 = valor_cheque1 + imposto_cheque1
imposto_cheque2 = valor_cheque2 * 0.38 / 100
saque2 = valor_cheque2 + imposto_cheque2
saldo = salario - saque1 - saque2
print(f"Você tem {saldo} reais de saldo")