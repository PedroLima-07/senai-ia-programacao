#Exercício 6 – Maior número
#Faça um programa que receba dois números e informe:
#qual é o maior
#ou se ambos são iguais
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:    
    print("Os números são iguais.")