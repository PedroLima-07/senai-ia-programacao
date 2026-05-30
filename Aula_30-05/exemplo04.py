# Exemplo com banco de dados local com SQLite
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
    instructions="""Você é uma assitente util e atencioso, que responde de forma didatica e clara,
    Sendo muito profissional.
    Responda sempre de forma resumida e educada.
    limite sua resposta a no maáximo 3 linhas""",
    db=SqliteDb(db_file="agentes.db"),
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True
)
agent.print_response("Eu estou trabalhando em um projeto de API em Python",session_id="dev_session")
agent.print_response("Qual framework deste teste devo usar", session_id="dev_session")
