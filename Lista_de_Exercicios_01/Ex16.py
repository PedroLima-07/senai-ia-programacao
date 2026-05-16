#Exercício 16 – Lista de compras
#Crie um programa que permita cadastrar 5 itens em uma lista e depois mostre todos os itens cadastrados.
lista_de_compras = []

print("Vamos adicionar itens a sua lista de compras!")
while lista_de_compras.__len__() < 5:
    item = input("Digite o nome do item: ")
    lista_de_compras.append(item)
print("Sua lista de compras é:")
for item in lista_de_compras:
    print(f"{lista_de_compras.index(item) + 1} - {item}")