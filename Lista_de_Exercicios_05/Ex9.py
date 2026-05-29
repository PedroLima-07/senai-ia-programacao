# Exercício 9 — Texto para Fala
# Utilizando gTTS:
# peça um texto usando input()
# transforme em áudio
# salve como fala.mp3
from openai import OpenAI
from gtts import gTTS

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

palavra = input("Digite o Texto que deseja converter em audio:\n")


# Converter texto em voz
tts = gTTS(
    text=palavra,
    lang="pt"
)

tts.save("ex9.mp3")

print("\nÁudio salvo como ex9.mp3")
