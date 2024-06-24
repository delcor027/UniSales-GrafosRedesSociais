# Análise de Redes Sociais

Este projeto implementa uma análise de redes sociais com base na teoria dos grafos, utilizando a biblioteca `networkx`. As centralidades de intermediação, proximidade e grau são calculadas para um conjunto de autores e suas colaborações.

## Estrutura do Código

- `Main.py`: Ponto de entrada do programa. Define a sequência de execução e salva os resultados das centralidades.
- `SocialNetwork.py`: Define a classe `SocialNetwork` que gerencia a rede social de colaborações utilizando grafos.
- `CentralityMeasures.py`: Contém métodos estáticos para calcular diferentes tipos de centralidades em um grafo.

## Como Executar

1. Garanta que Python 3 está instalado em seu ambiente.
2. Instale a biblioteca `networkx` usando pip:

```bash
pip install networkx
```

3. Clone este repositório ou baixe os arquivos do projeto.
4. Navegue até o diretório do projeto e execute o arquivo `Main.py` usando:

```bash
python Main.py
```


Isso irá calcular as centralidades, exibir os resultados no console e salvar em um arquivo chamado `centralidades.txt` no diretório `public`.

## Saída de um Caso de Teste

Quando você executa o `Main.py`, o programa calcula e exibe as centralidades para cada autor. Por exemplo:

```bash
Centralidade de Intermediação: {'Antonio': 0.0, 'Felipe': 1.0, 'Marcelo': 0.0}
Centralidade de Proximidade: {'Antonio': 0.6666666666666666, 'Felipe': 1.0, 'Marcelo': 0.6666666666666666}
Centralidade de Grau: {'Antonio': 0.5, 'Felipe': 1.0, 'Marcelo': 0.5}
```


Estas centralidades também são salvas em `public/centralidades.txt`.

## Autor

Matheus Delcor
