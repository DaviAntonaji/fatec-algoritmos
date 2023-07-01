numero1 = int(input("Digite o 1° número: "))
numero2 = int(input("Digite o 2° número: "))
numero3 = int(input("Digite o 3° número: "))

if numero1 < numero2 and numero1 < numero3:
    if numero2 < numero3:
        print("A ordem crescente é: ",numero1,"-",numero2,"-",numero3)
    else:
        print("A ordem crescente é: ",numero1,"-",numero3,"-",numero2)
if numero2 < numero1 and numero2 < numero3:
    if numero1 < numero3:
        print("A ordem crescente é: ",numero2,"-",numero1,"-",numero3)
    else:
        print("A ordem crescente é: ",numero2,"-",numero3,"-",numero1)
if numero3 < numero1 and numero3 < numero2:
    if numero1 < numero2:
        print("A ordem crescente é: ",numero3,"-",numero1,"-",numero2)
    else: 
        print("A ordem crescente é: ",numero3,"-",numero2,"-",numero1)
