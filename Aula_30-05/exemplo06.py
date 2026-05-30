# conversa com historico usando o banco de dados local com SQLite com Loop

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
    db=SqliteDb(db_file="agente02.db"),
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True
)
while True:
    entrada = input("Usuario: ")
    if entrada.lower() == 'sair':
        print("Encerrando o programa......")
        break
    agent.print_response(
        entrada, 
        session_id="dev_session",
        stream=True
        )
