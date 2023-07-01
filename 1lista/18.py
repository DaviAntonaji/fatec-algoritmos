peso_saco  = int(input("Digite o peso do saco: "))
racao_gato1  = int(input("Digite a quantidade de ração dada ao 1°gato: "))
racao_gato2 = int(input("Digite a quantidade de ração dada ao 2°gato: "))

total_final = peso_saco - 5 * (racao_gato1 + racao_gato2)
if total_final < 0:
  print(f"Em 5 dias o saco de ração faltará {-total_final} g")
else:
  print(f"Em 5 dias o saco de ração terá {total_final} g")