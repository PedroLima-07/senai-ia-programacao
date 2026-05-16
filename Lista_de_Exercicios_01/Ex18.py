#Exercício 18 – Cadastro com dicionário
#Crie um cadastro contendo:
#nome
#idade
#cidade
#Armazene essas informações em um dicionário e exiba os dados formatados.
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
cidade = input("Digite a cidade onde a pessoa mora: ")
pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}
print("Informações da pessoa:")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
    