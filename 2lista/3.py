sexo = input("Digite seu sexo (M/F): ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
if sexo is "M" or sexo is "m":
  pesoIdeal =  (72.7 * altura) - 58;
  if peso < pesoIdeal:
    print("Você está abaixo do peso ideal")
  elif peso == pesoIdeal:
    print("Você está no peso ideal")
  else:
    print("Você está acima do peso ideal")
  print(f"O peso ideal é: {pesoIdeal}")
elif sexo is "F" or sexo is "f":
  pesoIdeal = (62.1 * altura) - 44.7
  if peso < pesoIdeal:
    print("Você está abaixo do peso ideal")
  elif peso == pesoIdeal:
    print("Você está no peso ideal")
  else:
    print("Você está acima do peso ideal")
  print(f"O peso ideal é: {pesoIdeal}")
else:
  print("Sexo invalido")