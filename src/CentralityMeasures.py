import networkx as nx

class CentralityMeasures:
    """
    Classe para calcular as centralidades de um grafo.
    """

    @staticmethod
    def calculate_betweenness_centrality(graph):
        """
        Calcula a centralidade de intermediação (betweenness) para cada nó do grafo.

        Parâmetros:
            graph (nx.Graph): O grafo da rede social.

        Retorna:
            dict: Um dicionário onde as chaves são os nós e os valores são as centralidades de intermediação.
        """
        try:
            return nx.betweenness_centrality(graph)
        except Exception as e:
            print(f"Erro ao calcular a centralidade de intermediação: {e}")
            return None

    @staticmethod
    def calculate_closeness_centrality(graph):
        """
        Calcula a centralidade de proximidade (closeness) para cada nó do grafo.

        Parâmetros:
            graph (nx.Graph): O grafo da rede social.

        Retorna:
            dict: Um dicionário onde as chaves são os nós e os valores são as centralidades de proximidade.
        """
        try:
            return nx.closeness_centrality(graph)
        except Exception as e:
            print(f"Erro ao calcular a centralidade de proximidade: {e}")
            return None

    @staticmethod
    def calculate_degree_centrality(graph):
        """
        Calcula a centralidade de grau (degree) para cada nó do grafo.

        Parâmetros:
            graph (nx.Graph): O grafo da rede social.

        Retorna:
            dict: Um dicionário onde as chaves são os nós e os valores são as centralidades de grau.
        """
        try:
            return nx.degree_centrality(graph)
        except Exception as e:
            print(f"Erro ao calcular a centralidade de grau: {e}")
            return None
