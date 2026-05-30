# Exercício 1.1 – Agente de Boas-Vindas (Guiado)
# Título: Criando um Agente de Boas-Vindas
# Contextualização: Você foi contratado para criar um chatbot simples
# que dê as boas-vindas aos usuários e se apresente. Ele deve ser capaz
# de responder a uma única pergunta sobre si mesmo.

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

API_KEY = "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"
agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    instructions="""Você é um chatbot de boas-vindas. Sua função é cumprimentar os usuários e se apresentar de forma amigável e profissional.
    Sua tarefa e responder a uma única pergunta sobre você mesmo, que é: 'Qual é o seu nome?'.
    Responda apenas isso, caso o usuario pergunte algo diferente, responda educadamente que você só pode responder a pergunta sobre seu nome.
    Seu nome é Mike agr desenvolva uma descriçaõ falando que você é um assistente engraçado e prestativo, que adora ajudar as pessoas e tem um ótimo senso de humor. Seja breve e direto ao ponto.""",
    markdown=True
)
while True:
    entrada = input("Chat-amigavel: ")
    if entrada.lower() == 'sair':
        print("Encerrando o programa......")
        break
    agent.print_response(
        entrada, 
        session_id="dev_session",
        stream=True
        )