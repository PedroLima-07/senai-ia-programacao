#Exercício 19 – Eliminando duplicados
#Receba vários números do usuário e utilize conjunto (set) para remover valores repetidos.
#Mostre o resultado final sem duplicatas.
lista = []
for i in range(5):
    print("Digite um número: ")
    num = int(input())
    lista.append(num)
print("Números digitados: ", lista)
numeros_unicos = set(lista)
print("Números únicos: ", numeros_unicos)


    