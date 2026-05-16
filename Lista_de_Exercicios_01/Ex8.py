#Exercício 8 – Classificação por idade
#Faça um programa que receba a idade de uma pessoa e classifique como:
#Criança
#Adolescente
#Adulto
#Idoso
#Defina intervalos de idade para cada classificação.
idade = int(input("Digite a sua idade: "))
if idade <0:
    print("Idade inválida.")
elif idade < 12:
    print("Criança.")
elif idade < 18:
    print("Adolescente.")
elif idade < 60:
    print("Adulto.")
else:    
    print("Idoso.")