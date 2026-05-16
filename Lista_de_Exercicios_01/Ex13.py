#Exercício 13 – Função de saudação
#Crie uma função que receba um nome como parâmetro e exiba uma saudação personalizada.
def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo(a)!"

nome = input("Digite seu nome: ")

print(saudacao(nome))