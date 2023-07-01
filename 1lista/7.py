salario = float(input("Digite o salario do funcinário: "))
percent = float(input("Digite a porcentagem do imposto: "))
imposto = salario * percent/100
novoSalario = salario + 50 - imposto
print(f"O novo salario é {novoSalario:.2f}")