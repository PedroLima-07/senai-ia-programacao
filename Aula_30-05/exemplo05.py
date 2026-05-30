# exemplo de extração de dados em uma pagina web

#exemplo de extração de dados de uma pagina web
import requests
from bs4 import BeautifulSoup

from agno.agent import Agent
from agno.models.openai import OpenAIChat

API_KEY ="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"

def etrair_texto(url:str)->str:
    headers={
        "User-Agent":"Mozzila/5.0"
    }

    response= requests.get(url,headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text,"html.parser")

    for tag in soup(["script","style","nonscript"]):
        tag.decompose()
    
    texto = soup.get_text(separator=" ",strip=True)

    return texto[:2000]

url= "https://g1.globo.com/sp/sorocaba-jundiai/"

conteudo=etrair_texto(url)

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),    
    markdown=True
)

agent.print_response(
    f"""Analise o conteudo abaixo extraido da pagina
    {conteudo}
    Tarefas:
    -Resuma o conteudo
    -Diga qual e o tema principal
    -Liste informações importantes""",
    stream=True
)