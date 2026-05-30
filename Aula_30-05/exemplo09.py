from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

API_KEY = "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"

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    tools=[YFinanceTools(
        enable_stock_price=True
    )],
    markdown=True
)
agent.print_response(
    "Qual é o preço atual das ações da Apple?",
    stream=True
)