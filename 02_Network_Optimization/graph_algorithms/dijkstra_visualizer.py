"""
╔══════════════════════════════════════════════════════════════╗
║   DIJKSTRA — En Kısa Yol Algoritması + Görselleştirme        ║
║   Yöneylem Araştırması · FAZ 2: Ağ Optimizasyonu             ║
╚══════════════════════════════════════════════════════════════╝

Dijkstra Algoritması:
    - Negatif olmayan ağırlıklı graflar için kaynak→tüm düğümler
    - Greedy: Her adımda en küçük geçici mesafeli düğümü seç
    - Karmaşıklık: O((V + E) log V) — min-heap ile

DP Bağlantısı:
    d[v] = min_{(u,v) ∈ E} [d[u] + w(u,v)]
    Bellman Optimalliğinin greedy özel hali.
"""

import heapq


def dijkstra(adj: dict, source: int) -> tuple:
    """
    Dijkstra algoritması — min-heap implementasyonu.

    Args:
        adj     : {node: [(neighbor, weight), ...]} adjacency list
        source  : Başlangıç düğümü

    Returns:
        (dist, prev) — mesafeler ve geri izleme sözlükleri
    """
    dist = {node: float('inf') for node in adj}
    dist[source] = 0
    prev = {node: None for node in adj}
    pq   = [(0, source)]     # (dist, node) min-heap
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        for v, w in adj.get(u, []):
            if w < 0:
                raise ValueError(f"Negatif kenar ({u}→{v}: {w}) — Bellman-Ford kullanın!")
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    return dist, prev


def reconstruct_path(prev: dict, source, target) -> list:
    """Önceki düğüm tablosundan en kısa yolu yeniden oluştur."""
    path = []
    node = target
    while node is not None:
        path.append(node)
        if node == source:
            break
        node = prev.get(node)
    path.reverse()
    return path if path and path[0] == source else []


def dijkstra_step_trace(adj: dict, source, node_names: dict = None):
    """
    Dijkstra'yı adım adım izle — eğitim amaçlı.
    Her iterasyonda mesafe tablosunu yazdırır.
    """
    nodes = list(adj.keys())
    names = node_names or {n: str(n) for n in nodes}

    dist  = {n: float('inf') for n in nodes}
    prev  = {n: None for n in nodes}
    dist[source] = 0
    unvisited = set(nodes)
    step = 0

    print(f"\n  {'═'*65}")
    print(f"  📊 DIJKSTRA ADIM ADIM — Kaynak: {names[source]}")
    print(f"  {'═'*65}")

    # Başlangıç durumu
    header = f"  {'Adım':>5}  " + "  ".join(f"{names[n]:>8}" for n in nodes)
    print(header)
    print(f"  {'─'*len(header)}")

    def print_row(step_label, current=None):
        row = f"  {str(step_label):>5}  "
        for n in nodes:
            d = f"{dist[n]:.0f}" if dist[n] != float('inf') else "∞"
            marker = " ★" if n == current else "  "
            row += f"{(d+marker):>8}  "
        print(row)

    print_row("Başl.")

    while unvisited:
        # Unvisited arasında min dist
        u = min(unvisited, key=lambda n: dist[n])
        if dist[u] == float('inf'):
            break
        unvisited.remove(u)
        step += 1

        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

        print_row(f"k={step} ({names[u]})", u)

    print(f"  {'═'*65}")
    return dist, prev


def ascii_graph(adj: dict, dist: dict = None, node_names: dict = None):
    """Basit metin tabanlı ağ özeti."""
    names = node_names or {n: str(n) for n in adj}
    print(f"\n  📡 ADJACENCY LIST:")
    for u in sorted(adj.keys()):
        neighbors = ", ".join(
            f"{names[v]}(w={w})" for v, w in sorted(adj[u], key=lambda x: x[1])
        )
        d_str = f" | d={dist[u]:.0f}" if dist and dist[u] != float('inf') else ""
        print(f"    {names[u]:>6} → {neighbors}{d_str}")


def run_demo():
    print("=" * 65)
    print("  🗺️   DIJKSTRA — EN KISA YOL ALGORİTMASI")
    print("=" * 65)

    # --- Örnek 1: Şehirler arası rota ---
    print("\n[ÖRNEK 1] Türkiye Şehirler Arası Mesafe (yaklaşık km):")
    cities = {
        'İstanbul': [('Ankara', 450), ('Bursa', 154), ('İzmir', 565)],
        'Ankara':   [('İstanbul', 450), ('Konya', 261), ('Kayseri', 336), ('İzmir', 600)],
        'İzmir':    [('İstanbul', 565), ('Ankara', 600), ('Denizli', 245)],
        'Bursa':    [('İstanbul', 154), ('Ankara', 380), ('İzmir', 330)],
        'Konya':    [('Ankara', 261), ('Kayseri', 248), ('Antalya', 220)],
        'Kayseri':  [('Ankara', 336), ('Konya', 248)],
        'Denizli':  [('İzmir', 245), ('Antalya', 310)],
        'Antalya':  [('Konya', 220), ('Denizli', 310)]
    }

    dist1, prev1 = dijkstra(cities, 'İstanbul')

    print(f"\n  {'─'*50}")
    print(f"  {'Hedef':>12} {'Mesafe (km)':>14} {'En Kısa Rota':>20}")
    print(f"  {'─'*50}")
    for city in sorted(cities.keys()):
        if city == 'İstanbul':
            continue
        d = dist1[city]
        path = reconstruct_path(prev1, 'İstanbul', city)
        path_str = " → ".join(path) if path else "Erişilemiyor"
        d_str = f"{d:.0f} km" if d != float('inf') else "∞"
        print(f"  {city:>12} {d_str:>14}   {path_str}")

    # --- Örnek 2: Adım adım izleme ---
    print("\n\n[ÖRNEK 2] Küçük Graf — Adım Adım İzleme:")
    adj2 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    names2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    ascii_graph(adj2, node_names=names2)
    dist2, prev2 = dijkstra_step_trace(adj2, 0, names2)

    print(f"\n  SONUÇ — Kaynak A'dan En Kısa Yollar:")
    for v in [1, 2, 3]:
        path = reconstruct_path(prev2, 0, v)
        path_str = " → ".join(names2[p] for p in path)
        print(f"    A → {names2[v]}: {dist2[v]:.0f}   ({path_str})")

    # --- Örnek 3: Proje ağı (CPM Benzeri) ---
    print("\n\n[ÖRNEK 3] Üretim Tesisi İçi Lojistik Ağı:")
    factory = {
        'Giriş':    [('Depo-A', 3), ('Depo-B', 7)],
        'Depo-A':   [('Hat-1', 2), ('Hat-2', 5)],
        'Depo-B':   [('Hat-2', 1), ('Hat-3', 4)],
        'Hat-1':    [('Kalite', 2)],
        'Hat-2':    [('Kalite', 3)],
        'Hat-3':    [('Kalite', 1)],
        'Kalite':   [('Çıkış', 1)],
        'Çıkış':    []
    }

    dist3, prev3 = dijkstra(factory, 'Giriş')
    path_to_exit = reconstruct_path(prev3, 'Giriş', 'Çıkış')
    print(f"\n  Giriş → Çıkış En Kısa Rota: {' → '.join(path_to_exit)}")
    print(f"  Minimum Geçiş Süresi: {dist3['Çıkış']:.0f} dakika")

    print("\n" + "=" * 65)
    print("  Dijkstra: O((V+E)logV) | Bellman-Ford: O(VE)")
    print("  Negatif kenar varsa → Bellman-Ford kullanın!")
    print("=" * 65)


if __name__ == "__main__":
    run_demo()
