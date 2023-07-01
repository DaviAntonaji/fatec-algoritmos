numero = float(input("Digite um numero positivo: "))
if(numero <= 0):
  print("Esse número é negativo")
else:
  cubo = (numero**3)
  raiz_quadrada = (numero**0.5)
  raiz_cubica = (numero**0.33)
  print(f"Cubo: {cubo:.2f}\nRaiz Quadrada: {raiz_quadrada:.2f}\nRaiz Cubica: {raiz_cubica:.2f}")
