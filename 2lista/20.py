salario = float(input("Digite o salário: "))

if salario <  500:
  bonificacao = 5
elif salario >= 500 and salario <= 1200:
  bonificacao = 12
else:
  bonificacao = 0
salario = salario + (salario * (bonificacao / 100))
print("O valor do salário ajustado é ",salario)

if salario <= 600:
  print("O Auxílio escola é de R$150.00")
else:
  print("O Auxílio escola é de R$100.00")