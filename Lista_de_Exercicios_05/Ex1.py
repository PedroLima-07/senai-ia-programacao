# Lista de Exercícios — Primeiros Passos com IA em Python (NVIDIA API)
# Exercício 1 — Primeira Pergunta para a IA
# Crie um programa que:
# faça uma pergunta usando input()
# envie para a IA
# mostre a resposta na tela

from openai import OpenAI

cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

pergunta = input("Digite a sua pergunta para a IA:\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": "Você é um assistente inteligente."
        },

        {
            "role": "user",
            "content": pergunta
        }
    ]
)
print("\nResposta da IA:\n")
print(resposta.choices[0].message.content)