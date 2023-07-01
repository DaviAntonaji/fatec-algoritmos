
valor_salario = float(input("Digite o valor do salário: "))
qtde_quilowatt = float(input("Digite o valor de quilowatts gastos: "))
valor_quilowatt = valor_salario / 5
valor_em_reais = valor_quilowatt * qtde_quilowatt
valor_descontado = valor_em_reais * 15 / 100
valor_com_desconto =  valor_em_reais - valor_descontado
print(f"O valor do quilowatt é {valor_quilowatt:.2f}\nO valor em reais é {valor_em_reais:.2f}\nO valor com desconto é {valor_com_desconto:.2f}")