from datetime import datetime


ano1 = int(input("Digite o 1° ano: "))
mes1 = int(input("Digite o 1° mês: "))
dia1 = int(input("Digite o 1° dia: "))
ano2 = int(input("Digite o 1° ano: "))
mes2 = int(input("Digite o 2° mês: "))
dia2 = int(input("Digite o 2° dia: "))

if ano1 > ano2:
    print( "A maior data é: ",dia1,"-",mes1,"-",ano1)
elif ano2>ano1:
    print( "A maior data é: ",dia2,"-",mes2,"-",ano2)
elif mes1>mes2:
    print( "A maior data é: ",dia1,"-",mes1,"-",ano1)
elif mes2>mes1:
    print( "A maior data é: ",dia2, "-",mes2,"-",ano2)
elif dia1>dia2:
    print( "A maior data é:" ,dia1,"-",mes1," -",ano1)
elif dia2>dia1:
    print( "A maior data é: ",dia2," -",mes2,"-",ano2)
else:
    print( "As datas são iguais!")