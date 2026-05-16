#Exercício 14 – Função calculadora
#Crie uma função que receba dois números e uma operação matemática, retornando o resultado do cálculo.
def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Operação inválida. Por favor, escolha entre soma, subtração, multiplicação ou divisão."
    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação ( + , - , * , / ): ")
    
resultado = calculadora(num1, num2, operacao)
print(f"O resultado da operação é: {resultado}")