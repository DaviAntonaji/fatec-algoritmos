salario_minino = float(input("Digite o salário minimo: "))
turno = input("Digite o turno: ")
categoria = input("Digite a categoria: ")
numero_de_horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))

if turno == "M":
     coeficiente = 10/100 * salario_minino
elif turno == "V":
     coeficiente = 15/100 * salario_minino
elif turno == "N":
     coeficiente = 12/100 * salario_minino
 
print("Coeficiente: ",coeficiente)
 
salario_bruto = numero_de_horas_trabalhadas * coeficiente
 
print("Salario bruto: ", salario_bruto)
 
if categoria == "O":
    if salario_bruto >= 300:
        imposto = 5/100 * salario_bruto
    else:
        imposto = 3/100 * salario_bruto
else: 
    if salario_bruto >= 400:
        imposto = 6/100 * salario_bruto
    else:
         imposto = 4/100 * salario_bruto
 
print("Imposto: ", imposto)
 
if turno == "N" and numero_de_horas_trabalhadas > 80:
    gratificacao = 50
else:
    gratificacao = 30
 
print("Gratificação: ", gratificacao)
 
if categoria == "O" or coeficiente <= 25:
    auxilio = 1/3 * salario_bruto
else:
    auxilio = 1/2 * salario_bruto
 
print("Auxilio:", auxilio)
 
salario_liquido = salario_bruto - imposto + gratificacao + auxilio
 
print("Salário liquido: ", salario_liquido)

 
if salario_liquido < 350:
     print("Mal Remunerado")
elif salario_liquido >= 350 and salario_liquido <= 600:
     print("Normal")
else:
     print("Bem Remunerado")