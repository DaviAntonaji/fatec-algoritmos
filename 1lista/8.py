dep = float(input("Digite o valor do deposito: "))
taxa = float(input("Digite o valor da taxa: "))
rendimento = dep * taxa / 100
total = dep + rendimento
print(f"Rendimento: {rendimento:.2f} \nTotal: {total:.2f}")