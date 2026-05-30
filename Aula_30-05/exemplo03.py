# agente com loop para conversar
# junto com intruções para o modelo
from agno.agent import Agent
from agno.models.openai import OpenAIChat

API_KEY = "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"

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    instructions="""Você é uma assitente util e atencioso, que responde de forma didatica e clara,
    Sendo muito profissional.
    Responda sempre de forma resumida e educada.
    limite sua resposta a no maáximo 3 linhas""",
    markdown=True
)
while True:
    pergunta = input("Faça uma pergunta: (ou 'sair' para encerrar o programa) ")

    if pergunta.lower() == 'sair':
        print("Encerrando o programa. Até mais!")
        break

    agent.print_response(pergunta,stream=True)