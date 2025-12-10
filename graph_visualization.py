import networkx as nx
import matplotlib.pyplot as plt
from knowledge_database import dbz_graph

def visualize_subgraph(my_graph, center, depth=1):
    #Criação de um grafo novo, vazio para podermos adicionar as entidades e relações
    G_visual = nx.DiGraph()
    
    #Aplicando BFS
    visited = set([center])
    frontier = [(center, 0)]
    
    while frontier:
        node, dist = frontier.pop(0)
        if dist >= depth:
            continue

        targets = my_graph.edges.get(node, [])
        for target, relation in targets:
            G_visual.add_edge(node, target, label=relation)
            if target not in visited:
                visited.add(target)
                frontier.append((target, dist + 1))

    plt.figure(figsize=(12, 10))     
    pos = nx.spring_layout(G_visual, seed=42)
    
    #Desenho do Grafo
    nx.draw(
        G_visual, pos,
        with_labels=True,
        node_size=3000,
        node_color="skyblue",
        font_weight="bold",
        font_size=9,
        arrows=True
    )
    edge_labels = nx.get_edge_attributes(G_visual, 'label')
    nx.draw_networkx_edge_labels(G_visual, pos, edge_labels=edge_labels, font_color='red')
    
    plt.title(f"Subgrafo: {center} (Profundidade {depth})")
    
    plt.show()

def visualize_all(my_graph):
    #Grafo novo
    G_visual = nx.DiGraph()
    
    #Adição de todos os nós, ou seja, as entidades que foram criadas na database
    G_visual.add_nodes_from(my_graph.nodes.keys())
    
    #Adição de todos os relacionamentos, ou seja, as arestas do grafo
    for source, targets in my_graph.edges.items():
        for target, relation in targets:
            G_visual.add_edge(source, target, label=relation)

    plt.figure(figsize=(14, 12)) 
    pos = nx.spring_layout(G_visual, seed=42, k=0.15, iterations=50)
    
    nx.draw(
        G_visual, pos,
        with_labels=True,
        node_size=2000,          
        node_color="lightgreen", 
        font_size=8,             
        font_weight="bold",
        arrows=True
    )
    
    edge_labels = nx.get_edge_attributes(G_visual, 'label')
    nx.draw_networkx_edge_labels(G_visual, pos, edge_labels=edge_labels, font_size=7)
    plt.title("Grafo de Conhecimento Completo: Dragon Ball Z")
    plt.show()

if __name__ == "__main__":
    
    #1 - Goku no centro:
    visualize_subgraph(dbz_graph, center="Goku", depth=1)
    #2 - Vegeta no centro:
    visualize_subgraph(dbz_graph, center="Vegeta", depth=1)
    #3 - Todo o grafo:
    visualize_all(dbz_graph)