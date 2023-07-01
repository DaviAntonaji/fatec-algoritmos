codigo_estado = int(input("Digite o código do estado: "))
peso_em_toneladas = float(input("Digite o peso em toneladas: "))
codigo_carga = int(input("Digite o código da carga: "))

peso_em_quilos = peso_em_toneladas * 1000
print("Peso em quilos:", peso_em_quilos)

if codigo_carga >= 10 and codigo_carga <= 20:
    preco_da_carga = 100 * peso_em_quilos
elif codigo_carga >= 21 and codigo_carga <= 30:
    preco_da_carga = 250 * peso_em_quilos
elif codigo_carga >= 31 and codigo_carga <= 40:
    preco_da_carga = 340 * peso_em_quilos   
print("Preço da carga:", preco_da_carga)

if codigo_estado == 1:
    imposto = 35/100 * preco_da_carga
elif codigo_estado == 2:
    imposto = 25/100 * preco_da_carga
elif codigo_estado == 3:
    imposto = 15/100 * preco_da_carga
elif codigo_estado == 4:
    imposto = 5/100 * preco_da_carga
elif codigo_estado == 5:
    imposto = 0

print("Imposto: ", imposto)
valor_total = preco_da_carga + imposto
print("Valor total:",  valor_total)