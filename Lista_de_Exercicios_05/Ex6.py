# Exercício 6 — Explicador de Palavras
# Faça uma IA que:
# receba uma palavra
# explique o significado de forma simples
# Exemplo:
# “algoritmo”
# “internet”
# “inteligência artificial”

# Resposta no fim do arquivo

from openai import OpenAI

cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)
print("DIgite 'sair' para fechar o programa")
while True:
    palavra = input("\nDigite a palavra que deseja saber o significado: \n")
    if palavra.lower() == "sair" :
        print("Programa Encerrado")
        break

    resposta = cliente.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",

        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em siginificados das palavras, vc sempre entrega a explicação das palavras solicitadas de maneira breve"
            },

            {
                "role": "user",
                "content": palavra
            }
        ]
    )

    print("Tradução da IA:")
    print(resposta.choices[0].message.content)

# Neste exercicio a capacidade dela expressar o significado da palvra está correto, eu ainda exigi que ele fizesse
# coisas curtas para não ter problema com um texto gigante e ainda assim ficou bem claro todos os significados solicitados e os que eu pedi
