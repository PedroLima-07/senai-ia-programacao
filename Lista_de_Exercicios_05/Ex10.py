# Exercício 10 — IA + Voz
# Junte:
# NVIDIA API
# gTTS
# O programa deve:
# enviar pergunta para IA
# receber resposta
# transformar resposta em voz
# salvar áudio

from openai import OpenAI
from gtts import gTTS

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

palavra = input("Qual a sua duvida de hoje?\n")

# Gera resposta da IA
resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": "Seja fiel ao texto para ser narrado em voz alta"
        },

        {
            "role": "user",
            "content": palavra
        }
    ]
)

texto = resposta.choices[0].message.content

print("\nResposta:\n")
print(texto)
# Converter texto em voz
tts = gTTS(
    text=texto,
    lang="pt"
)

tts.save("ex10.mp3")

print("\nÁudio salvo como ex10.mp3")