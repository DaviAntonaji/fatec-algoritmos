print("----------------")
print("Lista de cargos:")
print("1 - Escriturário")
print("2 - Secretário")
print("3 - Caixa")
print("4 - Gerente")
print("5 - Diretor")
print("----------------")

salario = float(input("Digite o salario: "))
cargo = int(input("Digite o cargo: "))

if cargo == 1:
    print( "O cargo é Escriturário")
    aumento = salario * 50 / 100
    print( "O valor do aumento é: ", aumento)
    novo_sal = salario + aumento
    print( "O novo salário é: ", novo_sal)
elif cargo == 2:
    print( "O cargo é Secretário")
    aumento = salario * 35 / 100
    print( "O valor do aumento é: ", aumento)
    novo_sal = salario + aumento
    print( "O novo salário é: ", novo_sal)
elif cargo == 3:
    print( "O cargo é Caixa")
    aumento = salario * 20 / 100
    print( "O valor do aumento é: ", aumento)
    novo_sal = salario + aumento
    print( "O novo salário é: ",novo_sal)
elif cargo == 4:
    print( "O cargo é Gerente")
    aumento = salario * 10 / 100
    print( "O valor do aumento é: ", aumento)
    novo_sal = salario + aumento
    print( "O novo salário é: ", novo_sal)
elif cargo == 5:
    print( "O cargo é Diretor")
    aumento = salario * 0 / 100
    print( "O valor do aumento é: ", aumento)
    novo_sal = salario + aumento
    print( "O novo salário é: ", novo_sal)
else:
  print("Cargo invalido")