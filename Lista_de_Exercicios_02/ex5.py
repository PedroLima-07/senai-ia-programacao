# =========================================
# CÓDIGO ORIGINAL
# =========================================

# ERRO:
# O código está sem indentação correta.
#
# Em Python, a indentação define os blocos do programa.
# Sem ela o código gera erro imediatamente.

def processar_pedido(status, quantidade, estoque):

# ERRO DE SINTAXE:
# Falta o operador "==" para comparação.
#
# Errado:
# if status "aprovado":
#
# Correto:
# if status == "aprovado":
if status "aprovado":

# ERRO:
# Falta indentação dentro do if
if quantidade > 0:

# ERRO:
# Falta indentação novamente
if estoque >= quantidade:

# ERRO:
# Comentário e return ficaram na mesma linha.
#
# Isso quebra o código.
#Lógica de processamento do pedido return "Pedido processado com sucesso!"

else:

return "Erro: Estoque insuficiente."

else:

return "Erro: Quantidade inválida."

else:

return "Erro: Status do pedido não aprovado."


# Essas chamadas não funcionariam
# devido aos erros acima.
print(processar_pedido("aprovado", 5, 10))
print(processar_pedido("aprovado", 5, 3))
print(processar_pedido("pendente", 5, 10))



# =========================================
# CÓDIGO CORRIGIDO
# =========================================

# CORREÇÃO:
# Ajustada toda a indentação do código.
def processar_pedido(status, quantidade, estoque):

    # CORREÇÃO:
    # Agora a comparação usa "=="
    if status == "aprovado":

        # Verifica se a quantidade é válida
        if quantidade > 0:

            # Verifica se existe estoque suficiente
            if estoque >= quantidade:

                # Lógica de processamento do pedido
                return "Pedido processado com sucesso!"

            else:

                return "Erro: Estoque insuficiente."

        else:

            return "Erro: Quantidade inválida."

    else:

        return "Erro: Status do pedido não aprovado."


# Testes da função
print(processar_pedido("aprovado", 5, 10))
print(processar_pedido("aprovado", 5, 3))
print(processar_pedido("pendente", 5, 10))

# Resultado:
# Pedido processado com sucesso!
# Erro: Estoque insuficiente.
# Erro: Status do pedido não aprovado.



# =========================================
# CÓDIGO REFATORADO
# =========================================

# REFATORAÇÃO:
# Aplicamos Early Return.
#
# VANTAGENS:
# - Reduz níveis de indentação
# - Código mais limpo
# - Mais fácil de ler
# - Melhor manutenção


def processar_pedido(status, quantidade, estoque):

    # Primeiro validamos o status do pedido
    if status != "aprovado":

        return "Erro: Status do pedido não aprovado."

    # Depois validamos a quantidade
    if quantidade <= 0:

        return "Erro: Quantidade inválida."

    # Depois verificamos o estoque
    if estoque < quantidade:

        return "Erro: Estoque insuficiente."

    # Se todas as validações passaram,
    # o pedido pode ser processado
    return "Pedido processado com sucesso!"


# Testes da função
print(processar_pedido("aprovado", 5, 10))
print(processar_pedido("aprovado", 5, 3))
print(processar_pedido("pendente", 5, 10))

# Resultado:
# Pedido processado com sucesso!
# Erro: Estoque insuficiente.
# Erro: Status do pedido não aprovado.