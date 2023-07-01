n1 = float(input("Digite a nota do Trabalho de laboratório: "))
n2 = float(input("Digite a nota da Avaliação Semestral: "))
n3 = float(input("Digite a nota do Exame final: "))

media = (n1+n2+n3)/3

print(f"Média de: {media}")

if media <=10 and media >=8:
  print("Conceito: A")
elif media < 8 and media >= 7:
  print("Conceito: B")
elif media < 7 and media >=6:
  print("Conceito: C")
elif media < 6 and media >=5:
  print("Conceito: D")
else:
  print("Conceito: E")
