x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))
if x < y + z and y < x + z and z < x + y:
    if x == y and y == z:
        print("Triângulo Equilátero")
    elif x == y or x == z or y == z:
        print("Triângulo Isósceles")
    elif x != y and x != z and y != z:
        print("Triângulo Escaleno")
else:
    print("Essas medidas não formam um triângulo")