n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
n3 = float(input("Digite a 3° nota: "))

media = (n1+n2+n3)/3
print(f"A média é de: {media}, portanto está: ")
if media <=10 and media >=6:
  print("Aprovado")
elif media >=3 and media <6:
  print("Exame")
else:
  print("Reprovado")