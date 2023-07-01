salario_minimo = float(input("Digite o valor do salário minimo: "))
numero_horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
numero_dependentes = int(input("Digite o número de dependentes: "))
numero_horas_extras =  int(input("Digite o número de horas extras: "))


valor_hora = 1/5 * salario_minimo
salario_mes = numero_horas_trabalhadas * valor_hora
valor_dependentes = 32 * numero_dependentes
valor_hora_extra = numero_horas_extras * (valor_hora + (valor_hora * 50/100))
salario_bruto =salario_mes + valor_dependentes + valor_hora_extra
 

if salario_bruto < 200:
  imposto = 0
elif salario_bruto >= 200 and salario_bruto <=500:
  imposto = salario_bruto * 10/100
else:
  imposto = salario_bruto * 20/100
salario_liquido = salario_bruto - imposto
if salario_liquido <= 350:
  gratificacao = 100
else:
  gratificacao = 50
salario_a_receber = salario_liquido + gratificacao

print("O salário a receber é de: ", salario_a_receber)