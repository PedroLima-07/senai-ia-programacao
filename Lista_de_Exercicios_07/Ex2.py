# Exercício 2.3 – Monitor de Preços
# Título: Construindo um Monitor de Preços de Produtos
# Contextualização: Crie um script que monitore o preço de um produto em um site de e-commerce (ex: Amazon, Mercado Livre). O script deve extrair o preço atual e,
# se o preço cair abaixo de um valor predefinido, enviar uma notificação (pode ser umprint no console).
# Objetivo: Desenvolver uma aplicação de web scraping com lógica condicional para monitoramento de dados.
# Requisitos: Python, requests , BeautifulSoup4 , lógica condicional.

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

url= "https://www.casasbahia.com.br/smart-tv-tcl-qled-50-polegadas-4k-hdr10-hdmi-wi-fi-50p7k/p/1576009254?idLojista=14738"

conteudo=extrair_texto(url)

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    )
)

agent.print_response(
    f"""Você é um assistente especializado em analisar o preço do produto para os clientes.
    
    eu te entreguei um site que possui um produto e quero que vc compere o preço dele com o meu preço ideal
    meu preço ideal é 300 reais, me diga se o preço do produto é maior ou menor que o meu preço ideal e me diga o valor do produto.

    Conteudo:
    {conteudo}
    
    
    """,
    stream=True
)