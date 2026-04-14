"""
╔══════════════════════════════════════════════════════════════╗
║   FORD-FULKERSON — Maksimum Akış Algoritması                 ║
║   Yöneylem Araştırması · FAZ 2: Ağ Optimizasyonu             ║
╚══════════════════════════════════════════════════════════════╝

Maksimum Akış Problemi:
    Kaynak s'den hedef t'ye maksimum akışı bul.
    Her kenar (u,v) kapasitesi cap[u][v].

Ford-Fulkerson Yöntemi:
    1. Tüm akışları sıfırla
    2. Artık grafta (residual graph) s'den t'ye yol bul (BFS/DFS)
    3. Yol boyunca minimum artık kapasite = bottleneck
    4. Akışı bottleneck kadar artır
    5. Artık yol kalmayıncaya kadar tekrar

Karmaşıklık:
    Ford-Fulkerson (DFS): O(E * max_flow) — rasyonel kapasiteler gerekebilir
    Edmonds-Karp  (BFS): O(V * E²)        — polinomial garantili
"""

from collections import deque


def bfs_find_path(graph: list, source: int, sink: int, parent: list) -> bool:
    """
    BFS ile artık grafta genişletme yolu bul.
    (Edmonds-Karp varyantı — en kısa yolları seçer)
    """
    n = len(graph)
    visited = [False] * n
    visited[source] = True
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)

    return False


def edmonds_karp(capacity: list, source: int, sink: int) -> tuple:
    """
    Edmonds-Karp Maksimum Akış Algoritması (Ford-Fulkerson + BFS).

    Args:
        capacity : n×n kapasite matrisi
        source   : Kaynak düğüm
        sink     : Hedef düğüm

    Returns:
        (max_flow, flow_matrix, iterations)
    """
    n = len(capacity)
    graph = [row[:] for row in capacity]  # Artık kapasite grafiği
    flow_matrix = [[0] * n for _ in range(n)]
    max_flow = 0
    iterations = []

    while True:
        parent = [-1] * n
        if not bfs_find_path(graph, source, sink, parent):
            break

        # Yol boyunca minimum kapasite
        path_flow = float('inf')
        v = sink
        path = [v]
        while v != source:
            u = parent[v]
            path.append(u)
            path_flow = min(path_flow, graph[u][v])
            v = u
        path.reverse()

        # Akışı güncelle
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            flow_matrix[u][v] += path_flow
            flow_matrix[v][u] -= path_flow
            v = u

        max_flow += path_flow
        iterations.append({
            'path': path[:],
            'bottleneck': path_flow,
            'cumulative_flow': max_flow
        })

    return max_flow, flow_matrix, iterations


def min_cut(capacity: list, flow_matrix: list, source: int) -> tuple:
    """
    Max-Flow Min-Cut Teoremi: Minimum kesim bul.
    Artık grafta source'dan ulaşılabilen düğümler S kümesi.
    Kesim kenarları: S'den T'ye giden doymuş kenarlar.
    """
    n = len(capacity)
    # Artık kapasite hesapla
    residual = [[capacity[i][j] - max(0, flow_matrix[i][j])
                 for j in range(n)] for i in range(n)]

    # BFS ile source'dan ulaşılanları bul
    visited = [False] * n
    visited[source] = True
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and residual[u][v] > 0:
                visited[v] = True
                queue.append(v)

    S = [i for i in range(n) if visited[i]]
    T = [i for i in range(n) if not visited[i]]
    cut_edges = [(i, j, capacity[i][j]) for i in S for j in T if capacity[i][j] > 0]

    return S, T, cut_edges


def run_demo():
    print("=" * 65)
    print("  🌊  FORD-FULKERSON (EDMONDS-KARP) — MAKSİMUM AKIŞ")
    print("=" * 65)

    # --- Örnek 1: Klasik Ağ (CLRS kitabından) ---
    print("\n[ÖRNEK 1] 6 Düğümlü Akış Ağı:")
    # Düğümler: 0=s(kaynak), 1=A, 2=B, 3=C, 4=D, 5=t(hedef)
    n1 = 6
    cap1 = [
        [0, 16,  13,  0,  0,  0],
        [0,  0,   4, 12,  0,  0],
        [0,  0,   0,  0, 14,  0],
        [0,  9,   0,  0,  0, 20],
        [0,  0,   0,  7,  0,  4],
        [0,  0,   0,  0,  0,  0]
    ]
    nodes1 = ['s', 'A', 'B', 'C', 'D', 't']
    source1, sink1 = 0, 5

    max_flow1, flow1, iters1 = edmonds_karp(cap1, source1, sink1)

    print(f"\n  Kaynak: {nodes1[source1]}, Hedef: {nodes1[sink1]}")
    print(f"\n  📊 ARTIŞ YOLLARI (Augmenting Paths):")
    print(f"  {'İter':>5} {'Yol':>35} {'Bottleneck':>12} {'Kümülatif':>12}")
    print(f"  {'─'*65}")
    for k, it in enumerate(iters1):
        path_str = " → ".join(nodes1[p] for p in it['path'])
        print(f"  {k+1:>5}  {path_str:>35} {it['bottleneck']:>10}  {it['cumulative_flow']:>10}")

    print(f"\n  ✅ MAKSİMUM AKIŞ    : {max_flow1}")
    print(f"  Toplam İterasyon  : {len(iters1)}")

    # Gerçek akışlar
    print(f"\n  🔄 KENAR AKIŞLARI (akış / kapasite):")
    print(f"  {'Kenar':>8} {'Akış/Kapasite':>20}")
    print(f"  {'─'*30}")
    for i in range(n1):
        for j in range(n1):
            if cap1[i][j] > 0:
                f_val = max(0, flow1[i][j])
                print(f"  {nodes1[i]}→{nodes1[j]:>6}  {f_val:>6} / {cap1[i][j]:<6}")

    # Min-Cut
    S, T, cut_edges = min_cut(cap1, flow1, source1)
    print(f"\n  ✂️  MİNİMUM KESİM (Max-Flow Min-Cut Teoremi):")
    print(f"  S kümesi: {{{', '.join(nodes1[i] for i in S)}}}")
    print(f"  T kümesi: {{{', '.join(nodes1[i] for i in T)}}}")
    print(f"  Kesim Kenarları ve Kapasiteleri:")
    cut_total = 0
    for u, v, cap in cut_edges:
        print(f"    {nodes1[u]} → {nodes1[v]}: {cap}")
        cut_total += cap
    print(f"  Min-Cut Kapasitesi: {cut_total}  (= Max-Flow ✅)")

    # --- Örnek 2: Tedarik Zinciri ---
    print("\n\n[ÖRNEK 2] Tedarik Zinciri Akış Ağı:")
    # 0=Fabrika, 1=Depo1, 2=Depo2, 3=Mağaza1, 4=Mağaza2, 5=Müşteri
    cap2 = [
        [0, 20, 15,  0,  0,  0],
        [0,  0,  0, 12, 10,  0],
        [0,  0,  0,  8, 14,  0],
        [0,  0,  0,  0,  0, 15],
        [0,  0,  0,  0,  0, 18],
        [0,  0,  0,  0,  0,  0]
    ]
    nodes2 = ['Fabrika', 'Depo1', 'Depo2', 'Mağaza1', 'Mağaza2', 'Müşteri']
    max_flow2, _, iters2 = edmonds_karp(cap2, 0, 5)
    print(f"\n  Maksimum Tedarik Kapasitesi: {max_flow2} birim/gün")
    print(f"  (Bottleneck analizi için cut hesaplanabilir)")

    print("\n" + "=" * 65)
    print("  Max-Flow = Min-Cut (Ford & Fulkerson, 1956)")
    print("  Uygulama: nakliye, bant genişliği, eşleşme problemleri")
    print("=" * 65)


if __name__ == "__main__":
    run_demo()
