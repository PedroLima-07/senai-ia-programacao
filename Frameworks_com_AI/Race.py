from openai import OpenAI

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

# =========================
# FRAMEWORK RACE
# =========================

# R = Role (Papel da IA)
papel_ia = (
    "Você é um contador de histórias engraçadas e criativas."
)

# A = Action (Ação desejada)
acao = (
    "Crie uma história divertida."
)

# C = Context (Contexto)
contexto = (
    "A história é sobre um ninja que não sabia se esconder."
)

# E = Expectation (Resultado esperado)
expectativa = (
    "A resposta deve estar em português do Brasil, "
    "ter no máximo 80 palavras "
    "e ser engraçada para jovens estudantes."
)

print("\nPreparando resposta usando o framework RACE...\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": (
                f"{papel_ia}"
            )
        },

        {
            "role": "user",
            "content": (
                f"""
                Ação: {acao}

                Contexto: {contexto}

                Expectativa: {expectativa}
                """
            )
        }
    ]
)

print("--- Resposta da IA ---")
print(resposta.choices[0].message.content)
print("----------------------\n")