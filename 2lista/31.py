angulo = float(input("Digite o angulo: "))

if angulo > 360 or angulo < -360:
    voltas = angulo // 360 
    
    angulo = angulo - (360*voltas)
else: 
    voltas = 0
if angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360 or angulo == -90 or angulo == -180 or angulo == -270 or angulo == -360:
  
  print("Está acima de algum dos eixos")
elif (angulo > 0 and angulo < 90) or (angulo < -270 and angulo > -360):
  print("1o Quadrante")
elif (angulo > 90 and angulo < 180) or (angulo < -180 and angulo > -270):
  print("2o Quadrante")
elif (angulo > 180 and angulo < 270) or (angulo < -90 and angulo > -180):
  print("3o Quadrante")
elif (angulo > 270 and angulo < 360) or (angulo < 0 and angulo > -90):
  print("4o Quadrante")
print(voltas, " volta(s) no sentido ")
if angulo < 0:
    print("horário")
else: 
    print("anti-horário")