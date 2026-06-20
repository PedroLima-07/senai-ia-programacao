# Exercício 2.1 – Resumo de Notícias
# Título: Resumindo Notícias de um Blog
# Contextualização: Modifique o exemplo de extração de dados de página web para que ele acesse um blog de tecnologia de sua escolha, extraia o conteúdo de um
# artigo e peça ao agente de IA para resumir o artigo em três frases.
# Objetivo: Aplicar web scraping e integração com LLM para resumir conteúdo de texto.
# Requisitos: Python, requests , BeautifulSoup4 , Agno, API Key da NVIDIA, conhecimento do exemplo “Extração e Análise de Conteúdo Web com IA”.
# exercicio de extração de dados em uma pagina web

import requests
from bs4 import BeautifulSoup

from agno.agent import Agent
from agno.models.openai import OpenAIChat

API_KEY ="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"

def extrair_texto(url:str)->str:
    headers={
        "User-Agent":"Mozilla/5.0"
    }

    response= requests.get(url,headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text,"html.parser")

    for tag in soup(["script","style","nonscript"]):
        tag.decompose()
    
    texto = soup.get_text(separator=" ",strip=True)
    #Limite de Texto para evitar o consumo da IA
    return texto[:2000]

url= "https://g1.globo.com/tecnologia/noticia/2026/06/12/quem-e-elon-musk.ghtml"

conteudo=extrair_texto(url)

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    )
)

agent.print_response(
    f"""Você é um assistente especializado em resumir notícias.

    Leia o artigo abaixo.

    Resuma em exatamente três frases.

    Não invente informações.

    Texto:
    {conteudo}
    
    
    """,
    stream=True
)