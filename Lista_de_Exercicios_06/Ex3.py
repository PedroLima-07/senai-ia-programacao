# Exercício 1.3 – Chatbot de Perguntas e Respostas (Desafio)
# Título: Construindo um Chatbot de FAQ
# Contextualização: Crie um chatbot que responda a perguntas frequentes sobre um tópico específico (ex: história do Python, regras de um esporte). O chatbot deve ser capaz de lidar com um conjunto predefinido de perguntas e respostas, e informar quando não souber a resposta.
# Objetivo: Desenvolver um chatbot funcional que gerencie um conjunto de conhecimentos e interaja com o usuário de forma controlada.
# Requisitos: Python, Agno, API Key da NVIDIA, lógica condicional.

from agno.agent import Agent
from agno.models.openai import OpenAIChat

API_KEY = "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"
agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    instructions="""Você é um especialista em perguntas sobre Python.
    Seu nome é PyBot, um assistente virtual dedicado a responder perguntas frequentes sobre a linguagem de programação Python.
    Se o usuário fizer uma pergunta que não esteja no seu conjunto de conhecimentos, responda educadamente que você não tem essa informação disponível.""",
    markdown=True
)
while True:
    entrada = input("Chat-Python: ")
    if entrada.lower() == 'sair':
        print("Encerrando o programa......")
        break
    agent.print_response(
        entrada, 
        session_id="dev_session",
        stream=True
        )