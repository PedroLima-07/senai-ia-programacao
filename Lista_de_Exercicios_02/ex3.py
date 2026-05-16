# =========================================
# CÓDIGO ORIGINAL
# =========================================

# MÁ PRÁTICA:
# O nome da função está correto e descritivo,
# porém existe um espaço desnecessário na chamada da função.
def filtra_e_dobra(numeros):

    # Lista que irá armazenar os resultados
    resultado = []

    # Percorre todos os números da lista
    for num in numeros:

        # Verifica se o número é maior que 5
        if num > 5:

            # Dobra o número e adiciona na lista
            resultado.append(num * 2)

    # Retorna a lista final
    return resultado


# MÁ PRÁTICA:
# Espaço desnecessário antes do parêntese.
print(filtra_e_dobra ([1, 6, 3, 8, 2, 10]) )

# Resultado esperado:
# [12, 16, 20]



# =========================================
# CÓDIGO CORRIGIDO
# =========================================

# CORREÇÃO:
# O código já estava funcionando corretamente.
# Apenas foram corrigidos detalhes de formatação
# seguindo a PEP 8.

def filtra_e_dobra(numeros):

    resultado = []

    for num in numeros:

        if num > 5:

            resultado.append(num * 2)

    return resultado


# CORREÇÃO:
# Removido espaço desnecessário.
print(filtra_e_dobra([1, 6, 3, 8, 2, 10]))

# Resultado:
# [12, 16, 20]



# =========================================
# CÓDIGO REFATORADO
# =========================================

# REFATORAÇÃO:
# Mantivemos o nome da função porque ele já
# descreve bem sua responsabilidade.
def filtra_e_dobra(numeros):

    # REFATORAÇÃO:
    # Utilizamos List Comprehension.
    #
    # VANTAGENS:
    # - Código mais compacto
    # - Melhor legibilidade
    # - Mais Pythonico
    # - Evita append manual
    # - Facilita manutenção
    return [
        numero * 2
        for numero in numeros
        if numero > 5
    ]


# Teste da função
print(filtra_e_dobra([1, 6, 3, 8, 2, 10]))

# Resultado:
# [12, 16, 20]