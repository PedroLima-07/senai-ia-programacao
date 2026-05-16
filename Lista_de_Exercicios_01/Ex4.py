#Exercício 4 – Média escolar
#Faça um programa que receba 3 notas de um aluno, calcule a média e informe se ele está:
#Aprovado
#Recuperação
#Reprovado

for i in range(3):
    nota = float(input("Digite a nota do aluno: "))
    if i == 0:
        soma = nota
    else:
        soma += nota

media = soma / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:    print("Reprovado")