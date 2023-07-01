I = int(input("Digite a operação: "))
A = float(input("Digite o número A: "))
B = float(input("Digite o número B: "))
C = float(input("Digite o número C: "))


if I == 1:
    if A<B and A<C:
        if B<C:
            print("A ordem crescente dos números é ",A," -",B,"-",C)
        else:
            print("A ordem crescente dos números é ",A," -",C,"-",B)
    elif B<A and B<C:
        if A<C:
            print("A ordem crescente dos números é ",B," -",A,"-",C)
        else:
            print("A ordem crescente dos números é ",B," -",C,"-",A)
    elif C<A and C<B:
        if A<B:
            print("A ordem crescente dos números é ",C," -",A,"-",B)
        else:
            print("A ordem crescente dos números é ",C," -",B,"-",A)
elif I == 2:
    if A>B and A>C:
        if B>C:
            print("A ordem decrescente dos números é: ",A," -",B,"-",C)
        else:
            print("A ordem decrescente dos números é: ",A," -",C,"-",B)
    elif B>A and B>C:
        if A>C:
            print("A ordem decrescente dos números é: ",B," -",A,"-",C)
        else:
            print("A ordem decrescente dos números é: ",B," -",C,"-",A)
    elif C>A and C>B:
        if A>B:
            print("A ordem decrescente dos números é: ",C," -",A,"-",B)
        else:
            print("A ordem decrescente dos números é: ",C," -",B,"-",A)

elif I == 3:
    if A>B and A>C:
        print("A ordem desejada é: ",B,"-",A,"-",C)
    elif B>A and B>C:
        print("A ordem desejada é: ",A,"-",B,"-",C)
    elif C>A and C>B:
        print("A ordem desejada é: ",A,"-",C,"-",B)
else:
  print("Operação invalida")