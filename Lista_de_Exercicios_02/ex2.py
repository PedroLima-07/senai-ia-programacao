# =========================================
# CÓDIGO ORIGINAL
# =========================================

# MÁ PRÁTICA:
# O nome da função possui espaço desnecessário
# antes do parêntese.
def soma_pares (Lista_numeros):

    total = 0

    # ERRO:
    # O parâmetro foi declarado como "Lista_numeros"
    # mas dentro do for foi usado "lista_numeros".
    #
    # Python diferencia letras maiúsculas e minúsculas,
    # então isso gera erro de variável não definida.
    for numero in lista_numeros:

        # ERRO LÓGICO:
        # A condição está verificando números ímpares.
        #
        # numero % 2 != 0
        #
        # Isso significa:
        # "se o resto da divisão por 2 for diferente de 0"
        #
        # Ou seja:
        # 1, 3, 5...
        #
        # Porém a função deveria somar os números PARES.
        if numero % 2 != 0:

            total += numero

    return total


# MÁ PRÁTICA:
# Espaços desnecessários nos parênteses.
print(soma_pares ([1, 2, 3, 4, 5, 6]) )

# Resultado atual:
# 9 -> (1 + 3 + 5)

# Resultado esperado:
# 12 -> (2 + 4 + 6)



# =========================================
# CÓDIGO CORRIGIDO
# =========================================

# CORREÇÃO:
# Removido espaço desnecessário no nome da função.
def soma_pares(lista_numeros):

    total = 0

    # CORREÇÃO:
    # Agora o nome da variável está igual ao parâmetro.
    for numero in lista_numeros:

        # CORREÇÃO:
        # Agora verifica números pares.
        #
        # numero % 2 == 0
        #
        # Isso significa:
        # "se o resto da divisão por 2 for igual a 0"
        if numero % 2 == 0:

            total += numero

    return total


# CORREÇÃO:
# Removidos espaços desnecessários.
print(soma_pares([1, 2, 3, 4, 5, 6]))

# Resultado correto:
# 12



# =========================================
# CÓDIGO REFATORADO
# =========================================

# REFATORAÇÃO:
# Nome da função mantido claro e descritivo.
def soma_pares(lista_numeros):

    # REFATORAÇÃO:
    # Utilizamos sum() com generator expression.
    #
    # VANTAGENS:
    # - Código mais curto
    # - Mais legível
    # - Mais Pythonico
    # - Melhor manutenção
    # - Evita variável acumuladora manual
    return sum(
        numero
        for numero in lista_numeros
        if numero % 2 == 0
    )


# Teste da função
print(soma_pares([1, 2, 3, 4, 5, 6]))

# Resultado:
# 12