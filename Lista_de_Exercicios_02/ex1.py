# =========================================
# CÓDIGO ORIGINAL
# =========================================

# ERRO/MÁ PRÁTICA:
# Existe um espaço desnecessário entre o nome da função
# e o parêntese. Pela PEP 8 (padrão do Python),
# o correto é não usar esse espaço.
def saudacao (nome):

    # MÁ PRÁTICA:
    # Está sendo usada concatenação de strings com "+"
    # Isso funciona, mas não é a forma mais moderna em Python.

    # PROBLEMA:
    # Falta um espaço após a vírgula,
    # então a saída fica "Olá,Mundo!"
    print("Olá," + nome + "!")


# MÁ PRÁTICA:
# Também existe espaço desnecessário antes do parêntese.
saudacao ("Mundo")



# =========================================
# CÓDIGO CORRIGIDO
# =========================================

# CORREÇÃO:
# Removido o espaço desnecessário entre
# o nome da função e os parênteses.
def saudacao(nome):

    # CORREÇÃO:
    # Foi adicionado um espaço após a vírgula
    # para melhorar a saída visual.
    print("Olá, " + nome + "!")


# CORREÇÃO:
# Removido o espaço desnecessário na chamada da função.
saudacao("Mundo")



# =========================================
# CÓDIGO REFATORADO
# =========================================

# REFATORAÇÃO:
# Mantivemos a responsabilidade única da função:
# apenas exibir uma saudação.

def saudacao(nome):

    # REFATORAÇÃO:
    # Substituímos concatenação por f-string.
    #
    # VANTAGENS:
    # - Código mais moderno
    # - Melhor legibilidade
    # - Mais fácil de manter
    # - Mais Pythonico
    print(f"Olá, {nome}!")


# Chamada da função
saudacao("Mundo")