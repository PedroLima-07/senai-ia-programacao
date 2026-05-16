#Exercício 15 – Número primo
#Crie um programa com função que verifique se um número informado é primo.
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print("DIgite um numero inteiro:")
num = int(input())
resultado = eh_primo(num)
print(f"O número {num} é primo? {resultado}")