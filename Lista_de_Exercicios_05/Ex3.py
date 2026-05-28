# Exercício 3 — IA Pirata
# Crie uma IA personagem:
# pirata
# astronauta
# ninja
# robô
# O usuário deve digitar uma pergunta e a IA deve responder mantendo o personagem.

# Resposta no fim do Arquivo

from openai import OpenAI

cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)
personalidade = (
    "Você é um ninja da aldeia da folha, de categoria jonnin, sendo um dos caras mais fortes da aldeia e que e super amigavel e engraçado tanto com alunos e colegas"
)

print("Para sair do programa digite: sair\n")
while True:
    pergunta = input("Digite a sua pergunta :\n")
    if pergunta.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    else:
        resposta = cliente.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",

            messages=[
             {
                "role": "system",
                "content": personalidade
            },

            {
                "role": "user",
                "content": pergunta
            }
        ]
    )
    print("\nResposta da IA:\n")
    print("Ela agira como um:"+ " Ninja da aldeia da folha")
    print(resposta.choices[0].message.content)

