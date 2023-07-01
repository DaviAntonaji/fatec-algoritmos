print("Menu de opções: ")
print("1. Somar dois números")
print("2. Raiz quadrada de um número")
opcao = int(input("Digite a opção: "))

if opcao == 1:
  numero1 = float(input("Digite o 1 número a ser calculado: "))
  numero2 = float(input("Digite o 2 número a ser calculado: "))
  soma = numero1 + numero2
  print("A soma destes números é ",soma)  
elif opcao == 2:
  numero = float(input("Digite o número a ser calculado: "))
  numero = numero ** (1/2)
  print("A raiz quadrade desse número é ", numero)
else:
  print("Opção invalida")