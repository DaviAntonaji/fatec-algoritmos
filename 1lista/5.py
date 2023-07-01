salario = float(input("Digite o salario do funcionário: "))
percent = float(input("Digite a porcentagem do aumento: "))
aumento = salario * percent/100
novoSalario = salario + aumento
print(f"O novo salario é {novoSalario:.2f}")