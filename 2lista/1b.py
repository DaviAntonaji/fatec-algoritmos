salario = float(input("Digite o salário: "))

if salario <=500:
  salario += salario*(50/100)
else:
  salario += salario*(30/100)
print(f"O valor correto do salário é: {salario}")
