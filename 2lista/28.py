salario_base = float(input("Digite o salário base: "))
tempo = int(input("Digite o tempo: "))
 
if salario_base < 200:
    imposto = 0
elif salario_base <= 450:
    imposto = 3/100 * salario_base
elif salario_base < 700:
    imposto = 8/100 * salario_base
else:
    imposto = 12/100 * salario_base
print("Imposto: ", imposto)
if salario_base > 500:
    if tempo <= 3:
      gratificacao = 20
    else:
      gratificacao = 30
else:
    if tempo <= 3:
      gratificacao = 23
    elif tempo < 6:
      gratificacao = 35
    else:
      gratificacao = 33
print("Gratificação", gratificacao)

salario_liquido = salario_base - imposto + gratificacao
print("Salário liquido:", salario_liquido)
if salario_liquido <= 350:
    print("Classificação A")
elif salario_liquido < 600:
    print("Classificação B")
else:
    print("Classificação C")