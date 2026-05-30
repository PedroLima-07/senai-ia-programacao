import sqlite3
import pandas as pd
import yfinance as yf

df = yf.Ticker('AAPL').history(
    period='5d'
)

df = df.reset_index()

print(df.head)

with sqlite3.connect('acoes.db') as conn:
    df.to_sql(
        "historico_aapl",
        conn,
        if_exists='replace',
        index=False
    )
print("\n Gravando...")
with sqlite3.connect('acoes.db') as conn:
    resultado = pd.read_sql(
        """ 
        SELECT  Date, Close
        From historico_aapl
        """, 
        conn
    )
print("\n Consultando dados...")
print(resultado)