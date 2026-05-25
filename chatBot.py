from openai import OpenAI

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

historico_conversa = [
    {
        "role": "system",
        "content": "Você é um divertido amigo, prestativo e atencioso. Responde de forma casual e amigável."
    }
]

print("Olá, eu sou seu amigo chatbot. Digite 'sair' para encerrar nossa conversa")

while True:

    pergunta_usuario = input("Você: ")

    if pergunta_usuario.lower() == "sair":
        print("Até mais!")
        break

    historico_conversa.append({
        "role": "user",
        "content": pergunta_usuario
    })

    resposta_ai = cliente.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=historico_conversa
    )

    conteudo_resposta = resposta_ai.choices[0].message.content

    print(f"Amigo Chatbot: {conteudo_resposta}")

    historico_conversa.append({
        "role": "assistant",
        "content": conteudo_resposta
    })