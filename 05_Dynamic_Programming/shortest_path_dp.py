"""
╔══════════════════════════════════════════════════════════════╗
║   BELLMAN-FORD — En Kısa Yol (DP Yaklaşımı)                  ║
║   Yöneylem Araştırması · FAZ 5: Dinamik Programlama          ║
╚══════════════════════════════════════════════════════════════╝

Bellman-Ford Algoritması:
    - Yönlü ağlarda kaynak düğümden tüm diğer düğümlere en kısa yol
    - Negatif ağırlıklı kenarlarda çalışır (Dijkstra çalışmaz)
    - Negatif döngü tespiti yapabilir
    - DP geçişi: iterasyon k → en fazla k kenar kullanan en kısa yol

DP Geçiş Denklemi:
    d^k[v] = min over (u,v)∈E [ d^(k-1)[u] + w(u,v) ]
    d^0[kaynak] = 0, diğerleri = ∞

Karmaşıklık: O(V * E)  — V iterasyon × E kenar
"""


def bellman_ford(graph: dict, num_vertices: int, source: int):
    """
    Bellman-Ford DP algoritması.

    Args:
        graph       : {(u, v): weight} formatında kenar listesi
        num_vertices: Toplam düğüm sayısı
        source      : Kaynak düğüm (0-indexed)

    Returns:
        (dist, pred, has_negative_cycle)
        dist[v]  = source'dan v'ye en kısa mesafe
        pred[v]  = v'nin önceki düğümü (yol izleme)
        has_negative_cycle: True ise negatif döngü var
    """
    INF = float('inf')
    dist = [INF] * num_vertices
    pred = [-1] * num_vertices
    dist[source] = 0

    edges = [(u, v, w) for (u, v), w in graph.items()]

    # V-1 iterasyon: en fazla V-1 kenar kullanarak güncelle
    for iteration in range(num_vertices - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                updated = True
        if not updated:
            break  # Erken çıkış (zaten optimal)

    # V. iterasyon: negatif döngü kontrolü
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return dist, pred, has_negative_cycle


def reconstruct_path(pred: list, source: int, target: int):
    """Bellman-Ford'dan elde edilen önceki düğümlerle yolu geri izle."""
    path = []
    node = target
    while node != -1:
        path.append(node)
        if node == source:
            break
        node = pred[node]
        if node in path:  # Döngü koruması
            return None
    path.reverse()
    return path if path[0] == source else None


def print_distance_table(dist: list, pred: list, source: int,
                         node_names: list = None):
    """Mesafe tablosunu formatlı yazdır."""
    n = len(dist)
    names = node_names or [str(i) for i in range(n)]

    print(f"\n{'─'*52}")
    print(f"  MESAFE TABLOSU — Kaynak: {names[source]}")
    print(f"{'─'*52}")
    print(f"  {'Düğüm':>8} {'Mesafe':>10} {'Önceki':>10} {'Yol':>15}")
    print(f"{'─'*52}")

    for v in range(n):
        d_str = f"{dist[v]:.1f}" if dist[v] != float('inf') else "∞"
        prev  = names[pred[v]] if pred[v] != -1 else "-"
        path  = reconstruct_path(pred, source, v)
        path_str = "→".join(names[p] for p in path) if path else "Erişilemiyor"
        print(f"  {names[v]:>8} {d_str:>10} {prev:>10}   {path_str}")

    print(f"{'─'*52}")


def dp_table_trace(graph: dict, num_vertices: int, source: int,
                   node_names: list = None):
    """
    DP iterasyonlarını adım adım göster (eğitim amaçlı).
    """
    INF = float('inf')
    names = node_names or [str(i) for i in range(num_vertices)]
    dist = [INF] * num_vertices
    dist[source] = 0
    edges = [(u, v, w) for (u, v), w in graph.items()]

    print(f"\n{'═'*60}")
    print(f"  📊 BELLMAN-FORD DP TABLO İZLEME")
    print(f"{'═'*60}")

    # Başlangıç durumu
    row = "  k=0  | " + "  ".join(
        f"{names[v]}:{('0' if v==source else '∞'):>4}" for v in range(num_vertices)
    )
    print(row)

    for k in range(1, num_vertices):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True

        row = f"  k={k}  | " + "  ".join(
            f"{names[v]}:{dist[v] if dist[v]!=INF else '∞':>4}" for v in range(num_vertices)
        )
        print(row + ("  ← güncellendi" if changed else ""))

        if not changed:
            print(f"  → k={k}: Değişim yok, erken terminate.")
            break

    print(f"{'═'*60}")


def run_demo():
    print("=" * 60)
    print("  🗺️  BELLMAN-FORD — EN KISA YOL (DP YAKLAŞIMI)")
    print("=" * 60)

    # --- Örnek 1: Temel pozitif ağırlıklı graf ---
    print("\n[ÖRNEK 1] Pozitif Ağırlıklı Graf:")
    graph1 = {
        (0, 1): 4,
        (0, 2): 2,
        (1, 2): 5,
        (1, 3): 10,
        (2, 4): 3,
        (3, 5): 11,
        (4, 3): 4,
        (4, 5): 7,
    }
    nodes1 = ['A', 'B', 'C', 'D', 'E', 'F']
    V1 = 6

    dp_table_trace(graph1, V1, 0, nodes1)
    dist1, pred1, neg_cycle1 = bellman_ford(graph1, V1, 0)
    print_distance_table(dist1, pred1, 0, nodes1)
    print(f"\n  Negatif Döngü: {'EVET ⚠️' if neg_cycle1 else 'Hayır ✅'}")

    # --- Örnek 2: Negatif ağırlıklı kenarlar ---
    print("\n\n[ÖRNEK 2] Negatif Ağırlıklı Kenarlar:")
    graph2 = {
        (0, 1): 6,
        (0, 2): 7,
        (1, 3): 5,
        (1, 2): 8,
        (1, 4): -4,
        (2, 3): -3,
        (2, 4): 9,
        (3, 0): -2,
        (4, 3): 7,
    }
    nodes2 = ['s', 't', 'x', 'y', 'z']
    V2 = 5

    dist2, pred2, neg_cycle2 = bellman_ford(graph2, V2, 0)
    print_distance_table(dist2, pred2, 0, nodes2)
    print(f"\n  Negatif Döngü: {'EVET ⚠️' if neg_cycle2 else 'Hayır ✅'}")

    # --- Örnek 3: Negatif döngü tespiti ---
    print("\n\n[ÖRNEK 3] Negatif Döngü İçeren Graf:")
    graph3 = {
        (0, 1): 1,
        (1, 2): -1,
        (2, 3): -1,
        (3, 1): -1,  # Negatif döngü: 1→2→3→1
    }
    V3 = 4
    dist3, pred3, neg_cycle3 = bellman_ford(graph3, V3, 0)
    print(f"  Negatif Döngü: {'EVET ⚠️ — Sonsuz azalma mümkün!' if neg_cycle3 else 'Hayır ✅'}")

    print("\n" + "=" * 60)
    print("  Dijkstra → sadece pozitif kenarlar    O((V+E)logV)")
    print("  Bellman-Ford → negatif kenar desteği  O(V·E)")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
