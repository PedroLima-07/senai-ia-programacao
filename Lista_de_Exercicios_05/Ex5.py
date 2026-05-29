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

print("\n--Digite 'sair' para encerrar o programa.--\n")

while True:

    texto = input("Digite o texto que deseja traduzir:\n")

    if texto.lower() == "sair":
        print("Programa encerrado.")
        break

    idioma = input("Digite o idioma para o qual deseja traduzir:\n")

    resposta = cliente.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",

        messages=[
            {
                "role": "system",
                "content": "Você é um tradutor profissional, que apenas entrega a tradução solicitada."
            },

            {
                "role": "user",
                "content": (
                    f"Traduza o seguinte texto para {idioma}: {texto}"
                )
            }
        ]
    )

    print("\nTexto traduzido pela IA:\n")
    print(resposta.choices[0].message.content)
    print("\n---------------------------\n")
        
    

