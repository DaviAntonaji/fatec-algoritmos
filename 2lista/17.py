hora_inicial = int(input("Digite a hora inicial: "))
min_inicial = int(input("Digite o minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))

if min_inicial > minuto_final:
  minuto_final = minuto_final + 60
  hora_final = hora_final - 1
if hora_inicial > hora_final:
  hora_final = hora_final + 24
  minuto_duracao = minuto_final - min_inicial
hora_duracao = hora_final - hora_inicial
print("A duração em horas é: ", hora_duracao)
