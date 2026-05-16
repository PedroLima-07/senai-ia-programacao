#Exercício 10 – Soma acumulada
#Peça ao usuário 5 números e ao final exiba a soma de todos eles.
soma = 0
for i in range(1, 6):
    num = int (input(f"Digite um número: "))
    soma += num
print(f"A soma dos números digitados é: {soma}")