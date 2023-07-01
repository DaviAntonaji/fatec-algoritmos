pre = float(input("Digite o preço: "))
tipo = input("Digite o tipo: ")
refrig = input("Digite a refrigeração: ")
if refrig == "N":
    if tipo == "A":
        if pre < 15:
           valor_adic = 2
        else :
           valor_adic = 5
    if tipo == "L":
        if pre < 10:
           valor_adic = 1.5
        else :
           valor_adic = 2.5
    if tipo == "V":
        if pre < 30:
           valor_adic = 3
        else :
           valor_adic = 2.5
elif tipo == "A":
    valor_adic = 8
    if tipo == "L":
        valor_adic = 0
    if tipo == "V":
        valor_adic = 0
print("Valor adicional",valor_adic)
if pre < 25:
    imposto = 5/100 * pre
else:
    imposto = 8/100 * pre
print("Imposto:",imposto)
pre_custo = pre + imposto
print("Custo : ",pre_custo)
if tipo != "A" and refrig != "S":
  desconto = 3/100 * pre_custo
else:
  desconto = 0
print("Desconto", desconto)
novo_pre = pre_custo + valor_adic - desconto
print("Novo preço", novo_pre)
if novo_pre <= 50:
    print( "Barato")
elif novo_pre < 100:
    print( "Normal")
else: 
    print( "Caro")