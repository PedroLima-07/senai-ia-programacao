import sqlite3

conn = sqlite3.connect('agente02.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

print("Tabelas no banco de dados:")
for row in cursor.fetchall():
    print(row[0])

cursor.execute("SELECT * FROM agno_sessions;")
for linha in cursor.fetchall():
    print(linha)

conn.close()