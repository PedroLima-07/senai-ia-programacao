# importando PANDAS

import sqlite3
import pandas as pd

# dataframe
dados ={
    'nome': ['Bob', 'Stwew', 'Stwart'],
    'idade': [10, 12, 13]
}
df = pd.DataFrame(dados)

print("DataFrame original:")
print(df)

#salvar as informações no SQLite
with sqlite3.connect('escola.db') as conn:
    df.to_sql(
        'pessoas',
        conn,
        if_exists='replace', 
        index=False
    )
print("\nDados salvos no banco de dados SQLite.")

#consultar os dados do banco de dados
with sqlite3.connect('escola.db') as conn:
    consulta = pd.read_sql_query(
        'SELECT * FROM alunos', conn
    )

print("\nDados consultados do banco de dados SQLite:")
print(consulta)