numero = float(input("Digite um número: "))
parte_inteira = int(numero)
parte_fracionaria = numero - parte_inteira

numero_arredondado = round(numero)
print(f"Parte inteira: {parte_inteira}\n Parte fracionaria: {parte_fracionaria:.2f}\n Numero arredondado: {numero_arredondado}")