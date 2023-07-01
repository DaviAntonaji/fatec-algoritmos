saldoMedio = float(input("Diigite o saldo médio do cliente: "))

if saldoMedio <=200:
  ajuste = 0
elif saldoMedio > 200 and saldoMedio <= 400:
  ajuste = 20
elif saldoMedio > 400 and saldoMedio <= 600:
  ajuste = 30
else:
  ajuste = 40

saldo = saldoMedio + (saldoMedio*(ajuste/100))
print(f"O saldo ajustado é {saldo} ") 