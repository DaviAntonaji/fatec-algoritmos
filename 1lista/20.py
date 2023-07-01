angulo = float(input("Digite o angulo: "))
altura = float(input("Digite a altura: "))
import math
radiano = angulo * math.pi / 180
escada = altura / math.sin(radiano)
print(f"Escada:{escada}")