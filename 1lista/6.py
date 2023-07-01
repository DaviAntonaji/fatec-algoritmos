salario = float(input("Digite o salario do funcionário: "))
gratificacao = salario*5/100
imposto = salario *7/100
novoSalario = salario + gratificacao - imposto
print(f"O novo salario será {novoSalario:.2f}")