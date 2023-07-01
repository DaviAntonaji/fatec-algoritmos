from datetime import datetime

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

hoje = datetime.now()
mesExt = meses[hoje.month-1]
print ('Ano atual.:',hoje.year)
print ('Mês.......:',hoje.month)
print ('Dia.......:',hoje.day)
print ('Hora......:',hoje.hour)
print ('Minuto....:',hoje.minute)
print ('Segundos..:',hoje.second)

print("A data atual é: ", hoje.day, "/", hoje.month, "/", hoje.year, " - ", mesExt, " e ", hoje.hour, ":", hoje.minute, ":",hoje.second)