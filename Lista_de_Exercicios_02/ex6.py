# =========================================
# CÓDIGO ORIGINAL
# =========================================

def ler_arquivo_manual(nome_arquivo):

    # MÁ PRÁTICA:
    # Arquivo aberto manualmente.
    #
    # Problema:
    # Se acontecer algum erro antes do close(),
    # o arquivo pode permanecer aberto.
    f = open(nome_arquivo, "r")

    # Lê todo o conteúdo do arquivo
    conteudo = f.read()

    # Fecha o arquivo manualmente
    f.close()

    # Retorna o conteúdo lido
    return conteudo


# Cria um arquivo de teste
with open("teste.txt", "w") as f:

    f.write("Olá, mundo!")


# Exibe o conteúdo do arquivo
print(ler_arquivo_manual("teste.txt"))



# =========================================
# CÓDIGO CORRIGIDO
# =========================================

def ler_arquivo_manual(nome_arquivo):

    # CORREÇÃO:
    # Adicionado encoding para evitar problemas
    # com caracteres especiais.
    f = open(nome_arquivo, "r", encoding="utf-8")

    # Lê o conteúdo do arquivo
    conteudo = f.read()

    # Fecha o arquivo
    f.close()

    # Retorna o conteúdo
    return conteudo


# Criação do arquivo de teste
with open("teste.txt", "w", encoding="utf-8") as f:

    f.write("Olá, mundo!")


# Exibição do conteúdo
print(ler_arquivo_manual("teste.txt"))



# =========================================
# CÓDIGO REFATORADO
# =========================================

# REFATORAÇÃO:
# Utilizamos "with open()".
#
# VANTAGENS:
# - Fecha o arquivo automaticamente
# - Mais seguro
# - Mais moderno
# - Evita vazamento de recursos
# - Código mais limpo


def ler_arquivo(nome_arquivo):

    # O "with" garante que o arquivo será fechado
    # automaticamente após o uso.
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        # Lê todo o conteúdo do arquivo
        conteudo = arquivo.read()

    # Retorna o conteúdo lido
    return conteudo


# Criação do arquivo de teste
with open("teste.txt", "w", encoding="utf-8") as arquivo:

    # Escreve conteúdo dentro do arquivo
    arquivo.write("Olá, mundo!")


# Exibe o conteúdo do arquivo
print(ler_arquivo("teste.txt"))

# Resultado:
# Olá, mundo!