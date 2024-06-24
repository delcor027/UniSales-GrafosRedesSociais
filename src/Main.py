import os
from SocialNetwork import SocialNetwork
from CentralityMeasures import CentralityMeasures

def main():
    """
    Função principal que executa o programa de análise de redes sociais.
    """
    autores = ["Antonio", "Felipe", "Marcelo"]
    colaboracoes = [("Antonio", "Felipe"), ("Felipe", "Marcelo")]
    
    rede_social = SocialNetwork()
    rede_social.add_authors(autores)
    rede_social.add_collaborations(colaboracoes)
    
    betweenness = CentralityMeasures.calculate_betweenness_centrality(rede_social.graph)
    closeness = CentralityMeasures.calculate_closeness_centrality(rede_social.graph)
    degree = CentralityMeasures.calculate_degree_centrality(rede_social.graph)
    
    rede_social.display_centralities(betweenness, closeness, degree)
    
    pasta_resultados = 'public'
    if not os.path.exists(pasta_resultados):
        os.makedirs(pasta_resultados)
    
    caminho_arquivo = os.path.join(pasta_resultados, "centralidades.txt")
    rede_social.save_centralities(betweenness, closeness, degree, caminho_arquivo)

if __name__ == "__main__":
    main()
