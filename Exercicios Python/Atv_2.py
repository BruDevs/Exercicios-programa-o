#Ler um número inteiro entre 1 e 12 e escrever o mês correspondente.
#Caso o número seja fora desse intervalo, informar que não existe mês com este número.

Mes = int(input("Insira um número para saber seu mês correspondente: "))

if Mes == 1:
    print("Mês de Janeiro")
elif Mes == 2:
    print("Mês de Fevereiro")
elif Mes == 3:
    print("Mês de Março")
elif Mes == 4:
    print("Mês de Abril")
elif Mes == 5:
    print("Mês de Maio")
elif Mes == 6:
    print("Mês de Junho")
elif Mes == 7:
    print("Mês de Julho")
elif Mes == 8:
    print("Mês de Agosto")
elif Mes == 9:
    print("Mês de Setembro")
elif Mes == 10:
    print("Mês de Outubro")
elif Mes == 11:
    print("Mês de Novembro")
elif Mes == 12:
    print("Mês de Dezembro")
else:
    print("Mês inexistente")