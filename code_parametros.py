from openai import OpenAI

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

# --- Parâmetros que os alunos irão modificar ---
personalidade = (
    "Contador de historias engraçadas"
)

idioma = "português de Brasil"

tamanho_resposta = (
    "com no máximo 80"
)

tema_historia = (
    "Um ninja que não sabia se esconder"
)

print(f"\nPreparando a história com a personalidade: {personalidade}")
print(f"No idioma: {idioma}")
print(f"Sobre o tema: {tema_historia}\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",  # Modelo da NVIDIA

    messages=[
        {
            "role": "system",
            "content": (
                f"{personalidade} "
                f"Responda em {idioma}."
            )
        },

        {
            "role": "user",
            "content": (
                f"Fale sobre   "
                f"{tamanho_resposta} "
                f"sobre {tema_historia}."
            )
        }
    ]
)

print("--- Resposta da IA ---")
print(resposta.choices[0].message.content)
print("---------------------\n")