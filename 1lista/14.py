# O correto seria pegar o ano atual pegando do datetime, mas vamos lá KKKKK
# ano_atual = datetime.datetime.year
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano do nascimento: "))
idade_atual = ano_atual - ano_nascimento
idade_2050 = 2050-ano_nascimento
print(f"Você tem {idade_atual} anos de idade\nEm 2050 você terá {idade_2050} anos")