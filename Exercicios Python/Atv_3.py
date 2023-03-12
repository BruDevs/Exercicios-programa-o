#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

Numero = range(0,50) #Variável Numero é igual a uma lista que vai de 0 a 50 através da função range

for Numero in Numero:   #Para cada Numero dentro da variável Numero faça:
    if Numero % 2 == 1: #Se o resto da divisão do Numero analisado por dois for igual a um
        print(Numero)   #Imprima o Numero