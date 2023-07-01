preco_fabrica = float(input("Digite o preço da fabrica: "))
percentual_lucro_distribuido = float(input("Digite o percentual do lucro distribuido: "))
percentual_imposto = float(input("Digite o percentual de imposto: "))

lucro_distribuidor = preco_fabrica * percentual_lucro_distribuido / 100
valor_imposto = preco_fabrica * percentual_imposto / 100
preco_final = preco_fabrica + lucro_distribuidor + valor_imposto

print(f"O lucro do distribuidor é {lucro_distribuidor}\nO valor de imposto é {valor_imposto}\nO preço final é {preco_final}")