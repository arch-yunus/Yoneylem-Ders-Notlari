"""
Kruskal Algoritması — Minimum Yayılan Ağaç (MST)
------------------------------------------------
Tüm düğümleri birbirine bağlayan ve toplam kenar ağırlığı minimum olan
ağacı Kruskal'ın açgözlü yaklaşımı ile bulur.
Kütüphane: NetworkX, Matplotlib
"""

import networkx as nx
import matplotlib.pyplot as plt


class UnionFind:
    """Kruskal için Union-Find (Disjoint Set Union) veri yapısı."""
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 0 for n in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return False  # Aynı bileşende — döngü oluşturur
        # Union by rank
        if self.rank[ru] < self.rank[rv]:
            ru, rv = rv, ru
        self.parent[rv] = ru
        if self.rank[ru] == self.rank[rv]:
            self.rank[ru] += 1
        return True


def kruskal_mst(nodes: list, edges: list) -> list:
    """
    Kruskal algoritması ile MST hesaplar.

    Parametreler:
        nodes: Düğüm listesi ['A', 'B', ...]
        edges: [(ağırlık, düğüm1, düğüm2), ...] formatında kenar listesi

    Dönüş:
        mst_edges: MST kenarları [(ağırlık, u, v), ...]
    """
    sorted_edges = sorted(edges)
    uf = UnionFind(nodes)
    mst_edges = []
    total_weight = 0

    print("Kruskal Adım Adım:")
    print(f"{'Adım':<6} {'Kenar':<20} {'Ağırlık':>10} {'İşlem':>15}")
    print("-" * 55)

    step = 1
    for weight, u, v in sorted_edges:
        if uf.union(u, v):
            mst_edges.append((weight, u, v))
            total_weight += weight
            print(f"{step:<6} {u} ──── {v:<12} {weight:>10} {'✅ Eklendi':>15}")
            step += 1
        else:
            print(f"{'-':<6} {u} ──── {v:<12} {weight:>10} {'⛔ Döngü':>15}")

        if len(mst_edges) == len(nodes) - 1:
            break

    print(f"\nMST Toplam Ağırlık: {total_weight}")
    return mst_edges


def visualize_mst(nodes, edges, mst_edges):
    G = nx.Graph()
    for weight, u, v in edges:
        G.add_edge(u, v, weight=weight)

    mst_set = {(min(u,v), max(u,v)) for _, u, v in mst_edges}
    mst_edge_list = [(u, v) for _, u, v in mst_edges]
    other_edges = [e for e in G.edges() if (min(e[0],e[1]), max(e[0],e[1])) not in mst_set]

    pos = nx.spring_layout(G, seed=7)
    plt.figure(figsize=(10, 7))
    plt.title("Kruskal Algoritması — Minimum Yayılan Ağaç (MST)", fontsize=13, fontweight='bold')

    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightyellow', edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, style='dashed', alpha=0.4, width=1)
    nx.draw_networkx_edges(G, pos, edgelist=mst_edge_list, edge_color='darkgreen', width=3)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Örnek: Şehirlerarası fiber optik ağ planlaması
    nodes = ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Eskisehir', 'Balikesir']
    edges = [
        (4, 'Istanbul', 'Bursa'),
        (6, 'Istanbul', 'Balikesir'),
        (7, 'Istanbul', 'Ankara'),
        (3, 'Bursa', 'Balikesir'),
        (5, 'Bursa', 'Eskisehir'),
        (2, 'Balikesir', 'Izmir'),
        (4, 'Eskisehir', 'Ankara'),
        (6, 'Eskisehir', 'Izmir'),
        (8, 'Ankara', 'Izmir'),
    ]

    print("=" * 55)
    print("MİNİMUM YAYILAN AĞAÇ — KRUSKAL ALGORİTMASI")
    print("Uygulama: Şehirlerarası Fiber Optik Altyapı")
    print("=" * 55)

    mst = kruskal_mst(nodes, edges)
    visualize_mst(nodes, edges, mst)
