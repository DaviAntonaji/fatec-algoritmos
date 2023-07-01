import math
altura_degrau = int(input("Digite a altura de cada degrau em cm: "))
altura_desejada = int(input("Digite a altura desejada em cm: "))
quantidade_de_degraus = altura_desejada // altura_degrau
# ceil é função de arrendondar
print(f"Será preciso {math.ceil(quantidade_de_degraus)} degraus")