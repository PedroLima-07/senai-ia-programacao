# =========================================
# CÓDIGO ORIGINAL
# =========================================

def obter_desconto (tipo_cliente, valor_compra):

    # Verifica se o cliente é premium
    if tipo_cliente == "premium":

        # Verifica se a compra é maior que 1000
        if valor_compra > 1000:

            # ERRO:
            # Falta o operador "*"
            #
            # Errado:
            # valor_compra 0.20
            #
            # Correto:
            # valor_compra * 0.20
            return valor_compra == 0.20

        else:

            # Código correto
            return valor_compra * 0.10

    # Verifica se o cliente é gold
    elif tipo_cliente == "gold":

        # Verifica se a compra é maior que 500
        if valor_compra > 500:

            # Código correto
            return valor_compra * 0.15

        else:

            # ERRO:
            # Falta operador "*"
            return valor_compra == 0.05

    else:

        # MÁ PRÁTICA:
        # Falta espaço antes do comentário
        return 0# Sem desconto


# Testes
print(obter_desconto("premium", 1200))
print(obter_desconto("gold", 600))
print(obter_desconto("normal", 200))



# =========================================
# CÓDIGO CORRIGIDO
# =========================================

# CORREÇÃO:
# Removido espaço desnecessário no nome da função.
def obter_desconto(tipo_cliente, valor_compra):

    # Cliente premium
    if tipo_cliente == "premium":

        if valor_compra > 1000:

            # CORREÇÃO:
            # Adicionado operador "*"
            return valor_compra * 0.20

        else:

            return valor_compra * 0.10

    # Cliente gold
    elif tipo_cliente == "gold":

        if valor_compra > 500:

            return valor_compra * 0.15

        else:

            # CORREÇÃO:
            # Adicionado operador "*"
            return valor_compra * 0.05

    else:

        # CORREÇÃO:
        # Ajustado espaçamento
        return 0  # Sem desconto


# Testes
print(obter_desconto("premium", 1200))
print(obter_desconto("gold", 600))
print(obter_desconto("normal", 200))

# Resultado:
# 240.0
# 90.0
# 0



# =========================================
# CÓDIGO REFATORADO
# =========================================

# REFATORAÇÃO:
# Aplicamos Early Return para reduzir
# níveis de indentação.
#
# Também melhoramos legibilidade
# e organização das regras.


def obter_desconto(tipo_cliente, valor_compra):

    # Cliente premium
    if tipo_cliente == "premium":

        # Se compra maior que 1000
        # recebe 20% de desconto
        if valor_compra > 1000:

            return valor_compra * 0.20

        # Caso contrário recebe 10%
        return valor_compra * 0.10

    # Cliente gold
    if tipo_cliente == "gold":

        # Se compra maior que 500
        # recebe 15%
        if valor_compra > 500:

            return valor_compra * 0.15

        # Caso contrário recebe 5%
        return valor_compra * 0.05

    # Clientes comuns não recebem desconto
    return 0


# Testes
print(obter_desconto("premium", 1200))
print(obter_desconto("gold", 600))
print(obter_desconto("normal", 200))

# Resultado:
# 240.0
# 90.0
# 0