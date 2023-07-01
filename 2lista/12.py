print("Digite três números obrigatoriamente em ordem crescente e um quarto número que não siga essa regra.")
numero1 = int(input("Digite o 1° número: "))
numero2 = int(input("Digite o 2° número: "))
numero3 = int(input("Digite o 3° número: "))
numero4 = int(input("Digite o 4° número: "))

if numero4 > numero3:
    print("A ordem decrescente é: ",numero4,"-",numero3,"-",numero2,"-",numero1)
elif numero4 > numero2 and numero4 < numero3:
    print("A ordem decrescente é: ",numero3,"-",numero4,"-",numero2,"-",numero1)
elif numero4 > numero1 and numero4 < numero2:
    print("A ordem decrescente é: ",numero3,"-",numero2,"-",numero4,"-",numero1)
elif numero4 < numero1:
    print("A ordem decrescente é: ",numero3,"-",numero2,"-",numero1,"-",numero4)