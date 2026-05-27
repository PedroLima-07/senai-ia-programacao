from openai import OpenAI
from gtts import gTTS

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

pergunta = input("O que se deseja? Qual sua dúvida?\n")

# Gera resposta da IA
resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": "Você é um assistente útil."
        },

        {
            "role": "user",
            "content": pergunta
        }
    ]
)

texto = resposta.choices[0].message.content

print("\nResposta:\n")
print(texto)

# Converter texto em voz
tts = gTTS(
    text=texto,
    lang="pt-br"
)

tts.save("resposta.mp3")

print("\nÁudio salvo como resposta.mp3")