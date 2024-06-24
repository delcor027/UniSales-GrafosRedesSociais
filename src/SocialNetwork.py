import networkx as nx

class SocialNetwork:
    """
    Classe que representa uma rede social de colaborações entre autores utilizando a teoria dos grafos.
    
    Atributos:
        graph (nx.Graph): Um grafo não-direcionado representando a rede social.
    """

    def __init__(self):
        """
        Inicializa um novo grafo vazio.
        """
        self.graph = nx.Graph()
    
    def add_authors(self, authors):
        """
        Adiciona autores (nós) ao grafo.

        Parâmetros:
            authors (list): Uma lista de nomes de autores a serem adicionados como nós no grafo.
        """
        self.graph.add_nodes_from(authors)
    
    def add_collaborations(self, collaborations):
        """
        Adiciona colaborações (arestas) ao grafo.

        Parâmetros:
            collaborations (list of tuples): Uma lista de tuplas onde cada tupla representa uma colaboração entre dois autores.
        """
        self.graph.add_edges_from(collaborations)
    
    def save_centralities(self, betweenness, closeness, degree, filepath):
        """
        Salva as centralidades de intermediação, proximidade e grau em um arquivo.

        Parâmetros:
            betweenness (dict): Centralidades de intermediação calculadas.
            closeness (dict): Centralidades de proximidade calculadas.
            degree (dict): Centralidades de grau calculadas.
            filepath (str): O caminho do arquivo onde as centralidades serão salvas.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("Centralidade de Intermediação:\n")
                f.write(f"{betweenness}\n")
                f.write("Centralidade de Proximidade:\n")
                f.write(f"{closeness}\n")
                f.write("Centralidade de Grau:\n")
                f.write(f"{degree}\n")
            print(f"Centralidades salvas em {filepath}")
        except Exception as e:
            print(f"Erro ao salvar as centralidades no arquivo: {e}")

    def display_centralities(self, betweenness, closeness, degree):
        """
        Exibe as centralidades de intermediação, proximidade e grau para cada nó do grafo.

        Parâmetros:
            betweenness (dict): Centralidades de intermediação calculadas.
            closeness (dict): Centralidades de proximidade calculadas.
            degree (dict): Centralidades de grau calculadas.
        """
        print("Centralidade de Intermediação:", betweenness)
        print("Centralidade de Proximidade:", closeness)
        print("Centralidade de Grau:", degree)
