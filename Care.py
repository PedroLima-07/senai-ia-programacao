from openai import OpenAI

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

# =========================
# FRAMEWORK CARE
# =========================

# C = Context (Contexto)
contexto = (
    "A história acontece em uma vila ninja onde todos "
    "precisam ser furtivos."
)

# A = Action (Ação)
acao = (
    "Crie uma história engraçada sobre um ninja "
    "que não sabia se esconder."
)

# R = Result (Resultado esperado)
resultado = (
    "A resposta deve estar em português do Brasil, "
    "ter no máximo 80 palavras "
    "e possuir humor leve."
)

# E = Example (Exemplo)
exemplo = (
    "Exemplo de humor esperado: "
    "'O ninja tentou se esconder atrás de um poste, "
    "mas esqueceu que estava segurando uma placa escrito: "
    "EU ESTOU AQUI.'"
)

print("\nPreparando resposta usando o framework CARE...\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": (
                "Você é um contador de histórias engraçadas."
            )
        },

        {
            "role": "user",
            "content": (
                f"""
                Contexto:
                {contexto}

                Ação:
                {acao}

                Resultado esperado:
                {resultado}

                Exemplo:
                {exemplo}
                """
            )
        }
    ]
)

print("--- Resposta da IA ---")
print(resposta.choices[0].message.content)
print("----------------------\n")