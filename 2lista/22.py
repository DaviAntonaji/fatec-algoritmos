preco_atual = float(input("Digite o preço atual: "))
media_mensal_vendas = float(input("Digite a média mensal de vendas:"))

if media_mensal_vendas < 500 or preco_atual < 30:
    novo_preco = preco_atual + 10/100 * preco_atual
elif media_mensal_vendas >= 500 and media_mensal_vendas < 1200 or preco_atual >= 30 and preco_atual<80:
    novo_preco = preco_atual + 15 / 100 * preco_atual
elif media_mensal_vendas >= 1200 or preco_atual >= 80:
    novo_preco = preco_atual - 20 / 100 * preco_atual
 
print("O novo preço é: ",novo_preco)