import requests
from bs4 import BeautifulSoup
from agno.agent import Agent
from agno.models.openai import OpenAIChat

API_KEY = "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"


def extrair_texto(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    return soup.get_text(separator=" ", strip=True)[:4000]


url = "https://g1.globo.com/"
conteudo = extrair_texto(url)

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    markdown=True
)

agent.print_response(
    f"""
    Leia o artigo abaixo e responda APENAS com um resumo de exatamente 3 frases.
    Não escreva introdução, título, lista ou qualquer outro texto além das 3 frases.

    Artigo:
    {conteudo}
    """,
    stream=True
)