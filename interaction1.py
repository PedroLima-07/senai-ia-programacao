from openai import OpenAI

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

mensagem_system = input("Digite a instrução do sistema: ")
mensagem_user = input("Digite a pergunta do usuário: ")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": mensagem_system
        },

        {
            "role": "user",
            "content": mensagem_user
        }
    ]
)

print("\nResposta da IA:\n")
print(resposta.choices[0].message.content)