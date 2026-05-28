# Exercício 5 — Tradutor Simples
# Crie um programa que:
# peça um texto
# peça um idioma
# use a IA para traduzir
# Exemplo:
# texto: “Bom dia”
# idioma: inglês

from openai import OpenAI

cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)
pergunta =("Digite 'sair' para encerrar o programa:\n")
texto = input("Digite o texto que deseja traduzir:\n")
idioma = input("Digite o idioma para o qual deseja traduzir:\n")

resposta = cliente.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",

        messages=[
            {
                "role": "system",
                "content": (
                    f"Você é um tradutor profissional. Traduza o seguinte texto para {idioma}: {texto}"
                )
            }
        ]
    )
print("\nTexto traduzido da IA:\n")
print(resposta.choices[0].message.content)
        
    

