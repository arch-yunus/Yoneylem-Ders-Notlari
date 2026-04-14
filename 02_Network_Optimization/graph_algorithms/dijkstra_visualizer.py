"""
Dijkstra'nın En Kısa Yol Algoritması — Görselleştirici
-------------------------------------------------------
Ağırlıklı yönlü/yönsüz bir grafik üzerinde kaynak düğümden tüm diğer
düğümlere olan en kısa yolları hesaplar ve görselleştirir.
Kütüphane: NetworkX, Matplotlib
"""

import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph: dict, source: str) -> tuple[dict, dict]:
    """
    Dijkstra algoritması implementasyonu — priority queue ile.

    Parametreler:
        graph: {düğüm: [(komşu, ağırlık), ...]} formatında adjacency listesi
        source: Başlangıç düğümü

    Dönüş:
        distances: {düğüm: mesafe} sözlüğü
        predecessors: {düğüm: önceki_düğüm} en kısa yol izleme için
    """
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    predecessors = {node: None for node in graph}

    # (mesafe, düğüm) min-heap
    pq = [(0, source)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue  # Eski girdi, atla

        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))

    return distances, predecessors


def reconstruct_path(predecessors: dict, target: str) -> list:
    """En kısa yolu predecessors sözlüğünden yeniden inşa eder."""
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    return path


def visualize_graph(graph: dict, distances: dict, predecessors: dict, source: str, target: str = None):
    """NetworkX ile grafik ve en kısa yolu görselleştirir."""
    G = nx.DiGraph()
    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)

    # En kısa yolu bul
    path_edges = []
    if target:
        path = reconstruct_path(predecessors, target)
        path_edges = list(zip(path[:-1], path[1:]))

    plt.figure(figsize=(12, 8))
    plt.title(f"Dijkstra En Kısa Yol Görselleştirmesi — Kaynak: {source}", fontsize=14, fontweight='bold')

    # Düğüm renkleri
    node_colors = []
    for node in G.nodes():
        if node == source:
            node_colors.append('lime')
        elif node == target:
            node_colors.append('red')
        else:
            node_colors.append('skyblue')

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800)
    nx.draw_networkx_labels(G, pos, font_weight='bold')

    # Normal kenarlar
    normal_edges = [e for e in G.edges() if e not in path_edges]
    nx.draw_networkx_edges(G, pos, edgelist=normal_edges, arrows=True, width=1.5, alpha=0.5)

    # En kısa yol kenarları
    if path_edges:
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, arrows=True, 
                               edge_color='red', width=3.0, alpha=0.9)

    # Ağırlık etiketleri
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Mesafe bilgisi
    dist_text = "\n".join([f"{n}: {d:.1f}" for n, d in sorted(distances.items())])
    plt.text(1.05, 0.5, f"Mesafeler:\n{dist_text}", transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='center', bbox=dict(boxstyle='round', facecolor='wheat'))

    plt.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Örnek ağ — Lojistik dağıtım ağı
    graph = {
        'Fabrika': [('Depo_A', 4), ('Depo_B', 7)],
        'Depo_A': [('Magaza_1', 3), ('Magaza_2', 6)],
        'Depo_B': [('Magaza_2', 2), ('Magaza_3', 5)],
        'Magaza_1': [('Musteri_X', 4)],
        'Magaza_2': [('Musteri_X', 3), ('Musteri_Y', 2)],
        'Magaza_3': [('Musteri_Y', 4)],
        'Musteri_X': [],
        'Musteri_Y': []
    }

    print("=" * 50)
    print("DIJKSTRA EN KISA YOL ANALİZİ")
    print("=" * 50)

    distances, predecessors = dijkstra(graph, 'Fabrika')

    print(f"Kaynak: Fabrika\n")
    for dest, dist in distances.items():
        path = reconstruct_path(predecessors, dest)
        print(f"{dest:<15}: Mesafe={dist:6.1f}  Yol: {' → '.join(path)}")

    visualize_graph(graph, distances, predecessors, 'Fabrika', target='Musteri_Y')
