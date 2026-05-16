#Exercício 17 – Análise de números
#Receba 10 números, armazene em uma lista e mostre:
#maior número
#menor número
#média dos valores
soma = 0
lista = []
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)
    soma += num
print("Os números digitados foram:")
for num in lista:
    print(num)

print("A soma dos números é:", soma)
print("A média dos números é:", soma / len(lista))
print("O maior número é:", max(lista))
print("O menor número é:", min(lista))
