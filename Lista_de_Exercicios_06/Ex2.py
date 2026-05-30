# Exercício 1.2 – Chatbot Personalizado (Fixação)
# Título: Personalizando a Persona do Chatbot
# Contextualização: Modifique o chatbot interativo para que ele atue como um especialista em culinária, respondendo a perguntas sobre receitas e ingredientes de forma amigável e informativa.
# Objetivo: Aplicar o conceito de instructions para moldar a persona de um agente de IA.
# Requisitos: Python, Agno, API Key da NVIDIA, conhecimento do exemplo “Chatbot com Instruções de Comportamento”.

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
    instructions="""Você é um especialista em culinária. Sua função é ajudar os usuários a encontrar receitas e informações sobre ingredientes de forma amigável e informativa.
    Responda sempre de forma resumida e educada.
    Seu nome é ChefAI, um assistente virtual dedicado a tornar a experiência culinária mais divertida e acessível.""",
    markdown=True
)
while True:
    entrada = input("Chat-Culinário: ")
    if entrada.lower() == 'sair':
        print("Encerrando o programa......")
        break
    agent.print_response(
        entrada, 
        session_id="dev_session",
        stream=True
        )