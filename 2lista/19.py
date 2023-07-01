print("Menu de opções")
print("1. Imposto")
print("2. Novo salário")
print("3. Classificação")
opcao = input("Digite a opção desejada:")

if opcao is "1":
  salario = float(input("Digite o salário: "))
  if salario < 500:
    ajuste = 5
  elif salario >= 500 and salario <= 850:
    ajuste = 10
  elif salario > 850:
    ajuste = 15
  novoSalario = salario*(ajuste/100)
  print(f"O imposto do salário é: {novoSalario}")

elif opcao is "2":
  salario = float(input("Digite o salário: "))
  if salario < 450:
    aumento = 100
  elif salario >= 450 and salario < 750:
    aumento = 75
  elif salario >= 750 and salario < 1500:
    aumento = 50
  elif salario > 1500:
    aumento = 25
  novoSalario = salario+aumento
  print(f"O novo do salário é: {novoSalario}")
elif opcao is "3":
  salario = float(input("Digite o salário: "))
  if salario <= 700:
    print("Esse salario é mal remunerado")
  else:
    print("Esse salario é bem remunerado")
else:
  print("Opção invalida")



