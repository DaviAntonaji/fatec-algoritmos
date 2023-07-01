a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
if a == 0:
    print("Estes valores não formam uma equação de segundo grau") 
else:
    delta = (b * b) - ( 4 * a * c)
    if delta < 0:
        print("Não existe raiz real")
    elif delta == 0:
        print("Existe uma raiz real")
        x1 = (- b) / (2 * a)
        print("X1: ", x1)
    else:
        print("Existem duas raízes reais")
        import math
        x1 = (- b) + math.sqrt(delta) / (2 * a)
        x2 = (- b) - math.sqrt(delta) / (2 * a)
        print("X1: ", x1, "\nX2: ", x2)