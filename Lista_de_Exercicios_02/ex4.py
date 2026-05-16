# =========================================
# CÓDIGO ORIGINAL
# =========================================

def processa_dados_a(dados):

    # Lógica de processamento específica A
    return [x * 2 for x in dados]


def processa_dados_b(dados):

    # Lógica de processamento específica B

    # ERRO:
    # "=" não pode ser usado dentro da expressão.
    #
    # Isso gera erro de sintaxe imediatamente.
    #
    # Errado:
    # x = 10
    #
    # Correto:
    # x + 10

    # LINHA COM ERRO:
    # return [x = 10 for x in dados]

    pass


def processa_dados_c(dados):

    # Lógica de processamento específica C

    # MÁ PRÁTICA:
    # Espaçamento inconsistente.
    return [x - 5 for x in dados]


# MÁ PRÁTICA:
# Falta espaço ao redor do "="
lista_a = [1, 2, 3]

# ERRO:
# Faltava "=" na atribuição
#
# Errado:
# lista_b [4, 5, 6]
#
# Correto:
lista_b = [4, 5, 6]

# ERRO:
# Faltava "=" na atribuição
lista_c = [7, 8, 9]


# As chamadas abaixo falhariam
# no código original por causa dos erros.
print(processa_dados_a(lista_a))
print(processa_dados_b(lista_b))
print(processa_dados_c(lista_c))



# =========================================
# CÓDIGO CORRIGIDO
# =========================================

def processa_dados_a(dados):

    # Multiplica cada número por 2
    return [x * 2 for x in dados]


def processa_dados_b(dados):

    # CORREÇÃO:
    # Agora soma 10 corretamente
    return [x + 10 for x in dados]


def processa_dados_c(dados):

    # CORREÇÃO:
    # Espaçamento ajustado
    return [x - 5 for x in dados]


# CORREÇÃO:
# Espaçamento ajustado
lista_a = [1, 2, 3]

# CORREÇÃO:
# Adicionado "="
lista_b = [4, 5, 6]

# CORREÇÃO:
# Adicionado "="
lista_c = [7, 8, 9]


# Testes das funções
print(processa_dados_a(lista_a))
print(processa_dados_b(lista_b))
print(processa_dados_c(lista_c))

# Resultado:
# [2, 4, 6]
# [14, 15, 16]
# [2, 3, 4]



# =========================================
# CÓDIGO REFATORADO
# =========================================

# REFATORAÇÃO:
# Os nomes foram melhorados
# para deixar mais claro o objetivo
# de cada função.


def dobrar_numeros(numeros):

    # Multiplica cada número por 2
    return [numero * 2 for numero in numeros]


def adicionar_dez(numeros):

    # Soma 10 em cada número
    return [numero + 10 for numero in numeros]


def subtrair_cinco(numeros):

    # Subtrai 5 de cada número
    return [numero - 5 for numero in numeros]


# Listas de entrada
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = [7, 8, 9]


# Exibição dos resultados
print(dobrar_numeros(lista_a))
print(adicionar_dez(lista_b))
print(subtrair_cinco(lista_c))

# Resultado:
# [2, 4, 6]
# [14, 15, 16]
# [2, 3, 4]