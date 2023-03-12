# Crie um programa em python que pergunte ao usuário seu nome e sua idade. 
# Em seguida verifique se a idade é maior ou menor que 18, exiba da seguinte forma:
# Fulano é maior de 18 e tem XX Anos ou Fulano não é maior de 18 e tem XX Anos.

nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

if idade >=18:
    print(f"O(a) Sr(a){nome} é maior de idade e possui {idade} anos de idade!")
else:
    print(f"O(a) Sr(a){nome} é menor de idade e possui {idade} anos de idade!")
