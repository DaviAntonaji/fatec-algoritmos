qtde_horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_salario_minimo = int(input("Digite o valor do salario minimo: "))

valor_hora_trabalhada = valor_salario_minimo / 2
valor_salario_bruto = valor_hora_trabalhada * qtde_horas_trabalhadas
imposto = valor_salario_bruto * 3 / 100
Valor_salario_liquido =  valor_salario_bruto - imposto
print(f"O salario liquido é {Valor_salario_liquido}")