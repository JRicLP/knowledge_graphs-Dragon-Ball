import networkx as nx
import matplotlib.pyplot as plt
from knowledge_database import dbz_graph

def visualize_subgraph(my_graph, center, depth=1):
    #Visualizacao do grafo desejado
    G_visual = nx.DiGraph()
    
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

    #Layout e Desenho do Grafo:
    pos = nx.spring_layout(G_visual)
    plt.figure(figsize=(10, 8))
    nx.draw(
        G_visual, pos,
        with_labels=True,
        node_size=3000,
        node_color="orange",
        font_weight="bold",
        arrows=True
    )
    edge_labels = nx.get_edge_attributes(G_visual, 'label')
    nx.draw_networkx_edge_labels(G_visual, pos, edge_labels=edge_labels)
    plt.title(f"Subgrafo centrado em {center} (profundidade {depth})")
    plt.show()
