codigo_produto = int(input("Digite o código do produto: "))
peso_quilos = float(input("Digite o peso em quilos: "))
codigo_pais = input("Digite o código do país: ")


peso_em_gramas = peso_quilos * 1000
print("O peso em gramas é: ", peso_em_gramas)

if codigo_produto >= 1 and codigo_produto <= 4:
   preco_por_grama = 10
elif codigo_produto >= 5 and codigo_produto <= 7:
   preco_por_grama = 25
elif codigo_produto >= 8 and codigo_produto <= 10:
   preco_por_grama = 35    
preco_total = peso_em_gramas * 1
print("O preço total é: ", preco_total)
if codigo_pais == 1:
    imposto = 0
elif codigo_pais == 2:
    imposto = preco_total * 15/100
elif codigo_pais == 3:
    imposto = preco_total * 25/100    
print("O imposto é: ", imposto)
valor_total = preco_total + imposto
print("O valor total é de: ", valor_total)