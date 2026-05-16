#Exercício 7 – Calculadora simples
#Crie um programa que receba dois números e uma operação matemática (+, -, *, /), realizando o cálculo correspondente.
print("--Menu--")
print(f"1 - Soma(+)\n2 - Subtração(-)\n3 - Multiplicação(*)\n4 - Divisão(/)")
opcao = int(input("Escolha a operação desejada: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
match opcao:
    case 1:
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    case 2:
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    case 3:
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    case 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")