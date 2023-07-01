peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
  print("Abaixo do peso")
elif imc >= 18.5 and imc <= 25:
  print("No peso normal")
elif imc >= 25.1 and imc <=30:
  print("Acima do peso")
else:
  print("Obeso")

print(f"Seu IMC é de {imc}")