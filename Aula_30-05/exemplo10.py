from pathlib import Path
import sqlite3
import pandas as pd
import yfinance as yf

from agno.agent import Agent
from agno.tools.pandas import PandasTools
from agno.models.openai import OpenAIChat
from agno.tools.sql import SQLTools
from agno.tools.yfinance import YFinanceTools

API_KEY ="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"

DB_PATH = Path(__file__).with_name("market_data.db")


def preparar_banco():
    tickers = ["NVDA", "AAPL", "MSFT"]
    linhas = []

    for ticker in tickers:
        historico = yf.Ticker(ticker).history(
            period="5d",
            interval="1d"  # corrigido
        )

        if historico.empty:
            continue

        historico = historico.reset_index()

        if "Date" in historico.columns:
            historico = historico.rename(columns={"Date": "data"})
        elif "Datetime" in historico.columns:
            historico = historico.rename(columns={"Datetime": "data"})

        historico["Ticker"] = ticker

        historico = historico.rename(
            columns={
                "Close": "fechamento",
                "Volume": "volume"
            }
        )

        historico = historico[
            ["data", "Ticker", "fechamento", "volume"]
        ]

        linhas.append(historico)

    # executa apenas após processar todos os tickers
    if linhas:
        df_historico = pd.concat(
            linhas,
            ignore_index=True
        )
    else:
        df_historico = pd.DataFrame(
            [{
                "data": pd.Timestamp.utcnow().normalize(),
                "Ticker": "NVDA",
                "fechamento": 0.0,
                "volume": 0
            }]
        )

    with sqlite3.connect(DB_PATH) as conn:
        df_historico.to_sql(
            "historico_precos",
            conn,
            if_exists="replace",
            index=False
        )


preparar_banco()

# Criando o agente

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.3-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    tools=[
        YFinanceTools(
            enable_stock_price=True,
            enable_analyst_recommendations=True,
            enable_stock_fundamentals=True
        ),
        PandasTools(),
        SQLTools(
            db_url=f"sqlite:///{DB_PATH.as_posix()}"
        ),
    ],
    description="""
    Você é um analista de investimentos que usa dados financeiros,
    SQL e análise de mercado para responder.
    """,
    instructions=[
        "use markdown nas respostas",
        "use tabelas quando possível",
        "consulte SQL para dados locais (historico_precos)"
    ],
    markdown=True
)

agent.print_response(
    """
    Use yfinance para obter o preço e recomendações da NVDA.
    Depois consulte o banco SQLite (historico_precos).
    """,
    stream=True
)