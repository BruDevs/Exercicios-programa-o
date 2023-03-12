#Solicite a entrada de um número e descubra se um número digitado é par ou ímpar.

x = input("Digite um número e verifique se é impar ou par: ")

x = int(x)

if x % 2 == 1:
        print("Número Ímpar")
else:
        print("Número Par!")

