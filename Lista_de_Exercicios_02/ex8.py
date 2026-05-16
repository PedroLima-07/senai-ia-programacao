# =========================================
# CÓDIGO ORIGINAL
# =========================================

class ProcessadorDeDados:

    # ERRO:
    # O método construtor está escrito errado.
    #
    # Errado:
    # _init_
    #
    # Correto:
    # __init__
    #
    # Em Python o construtor precisa ter
    # dois underscores antes e depois.
    def _init_(self, dados):

        self.dados = dados

    # MÁ PRÁTICA:
    # Espaço desnecessário antes do parêntese.
    def processar_dados (self):

        # Validação dos dados
        if not self.dados or not isinstance(self.dados, list):

            print("Erro: Dados inválidos.")

            return []

        # Filtragem dos dados
        dados_filtrados = []

        for item in self.dados:

            # Verifica se o item é inteiro positivo
            if isinstance(item, int) and item > 0:

                dados_filtrados.append(item)

        # Transformação dos dados
        dados_transformados = []

        # ERRO:
        # Nome da variável com espaço.
        #
        # Errado:
        # dados filtrados
        #
        # Correto:
        # dados_filtrados
        for item in dados_filtrados:

            dados_transformados.append(item * 10)

        # Geração de relatório
        print("--- Relatório de Processamento ---")

        print(f"Total de itens processados: {len(dados_transformados)}")

        print(f"Dados transformados: {dados_transformados}")

        print(" -")

        # ERRO:
        # Nome da variável com espaço.
        #
        # Errado:
        # dados transformados
        #
        # Correto:
        # dados_transformados
        return dados_transformados


# Instância da classe
proc = ProcessadorDeDados([1, 2, 3, 4, "a", 5])

# Execução do processamento
proc.processar_dados()



# =========================================
# CÓDIGO CORRIGIDO
# =========================================

class ProcessadorDeDados:

    # CORREÇÃO:
    # Nome correto do construtor.
    def __init__(self, dados):

        self.dados = dados

    # CORREÇÃO:
    # Removido espaço desnecessário.
    def processar_dados(self):

        # Verifica se os dados são válidos
        if not self.dados or not isinstance(self.dados, list):

            print("Erro: Dados inválidos.")

            return []

        # Lista para armazenar dados válidos
        dados_filtrados = []

        for item in self.dados:

            # Mantém apenas inteiros positivos
            if isinstance(item, int) and item > 0:

                dados_filtrados.append(item)

        # Lista para armazenar dados transformados
        dados_transformados = []

        # CORREÇÃO:
        # Nome da variável ajustado.
        for item in dados_filtrados:

            dados_transformados.append(item * 10)

        # Relatório
        print("--- Relatório de Processamento ---")

        print(f"Total de itens processados: {len(dados_transformados)}")

        print(f"Dados transformados: {dados_transformados}")

        print("-")

        # CORREÇÃO:
        # Nome da variável ajustado.
        return dados_transformados


# Instância da classe
proc = ProcessadorDeDados([1, 2, 3, 4, "a", 5])

# Execução
proc.processar_dados()

# Resultado:
# --- Relatório de Processamento ---
# Total de itens processados: 5
# Dados transformados: [10, 20, 30, 40, 50]



# =========================================
# CÓDIGO REFATORADO
# =========================================

class ProcessadorDeDados:

    # Construtor da classe
    #
    # Responsável por armazenar os dados recebidos.
    def __init__(self, dados):

        self.dados = dados

    # Método responsável apenas pela validação
    #
    # REFATORAÇÃO:
    # Aplicamos responsabilidade única.
    def dados_validos(self):

        return isinstance(self.dados, list) and len(self.dados) > 0

    # Método responsável apenas pela filtragem
    #
    # REFATORAÇÃO:
    # Utilizamos List Comprehension.
    def filtrar_dados(self):

        return [
            item
            for item in self.dados
            if isinstance(item, int) and item > 0
        ]

    # Método responsável apenas pela transformação
    def transformar_dados(self, dados_filtrados):

        return [
            item * 10
            for item in dados_filtrados
        ]

    # Método responsável apenas pela geração do relatório
    def gerar_relatorio(self, dados_transformados):

        print("--- Relatório de Processamento ---")

        print(
            f"Total de itens processados: "
            f"{len(dados_transformados)}"
        )

        print(f"Dados transformados: {dados_transformados}")

        print("-")

    # Método principal do processamento
    def processar_dados(self):

        # Validação dos dados
        if not self.dados_validos():

            print("Erro: Dados inválidos.")

            return []

        # Filtra os dados válidos
        dados_filtrados = self.filtrar_dados()

        # Transforma os dados
        dados_transformados = self.transformar_dados(
            dados_filtrados
        )

        # Gera relatório
        self.gerar_relatorio(dados_transformados)

        # Retorna os dados processados
        return dados_transformados


# Instância da classe
processador = ProcessadorDeDados(
    [1, 2, 3, 4, "a", 5]
)

# Executa o processamento
processador.processar_dados()

# Resultado:
# --- Relatório de Processamento ---
# Total de itens processados: 5
# Dados transformados: [10, 20, 30, 40, 50]