from agno.agent import Agent
from agno.models.openai import OpenAIChat

API_KEY = "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"

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),markdown=True
)
pergunta ="Escreva uma função em Python que verifica se um numero é par"

agent.print_response(pergunta,stream=True)