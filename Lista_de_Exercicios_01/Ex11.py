#Exercício 11 – Tabuada
#Faça um programa que receba um número inteiro e mostre sua tabuada de 1 até 10.
num = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   