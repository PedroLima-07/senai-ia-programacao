from openai import OpenAI

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

# =========================
# FRAMEWORK CREATE
# =========================

# C = Character (Personagem/Papel)
personagem = (
    "Você é um contador de histórias engraçadas."
)

# R = Request (Solicitação)
solicitacao = (
    "Crie uma história sobre um ninja que não sabia se esconder."
)

# E = Examples (Exemplos)
exemplos = (
    "Exemplo de humor: "
    "'O ninja tentou se esconder atrás de uma árvore, "
    "mas deixou os pés aparecendo.'"
)

# A = Adjustments (Ajustes)
ajustes = (
    "Use linguagem simples, divertida e apropriada para jovens."
)

# T = Type (Tipo de saída)
tipo_saida = (
    "A saída deve ser uma história curta."
)

# E = Extras (Informações adicionais)
extras = (
    "A história deve estar em português do Brasil "
    "e ter no máximo 80 palavras."
)

print("\nPreparando resposta usando o framework CREATE...\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": personagem
        },

        {
            "role": "user",
            "content": (
                f"""
                Solicitação:
                {solicitacao}

                Exemplos:
                {exemplos}

                Ajustes:
                {ajustes}

                Tipo de saída:
                {tipo_saida}

                Extras:
                {extras}
                """
            )
        }
    ]
)

print("--- Resposta da IA ---")
print(resposta.choices[0].message.content)
print("----------------------\n")