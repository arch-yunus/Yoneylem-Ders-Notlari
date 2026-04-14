"""
╔══════════════════════════════════════════════════════════════╗
║   MACAR ALGORİTMASI — Atama Problemi (Hungarian Method)      ║
║   Yöneylem Araştırması · FAZ 2: Ağ Optimizasyonu             ║
╚══════════════════════════════════════════════════════════════╝

Atama Problemi:
    n işçi, n iş; maliyet[i][j] = İşçi i'nin j işini yapma maliyeti.
    Amaç: Her işçiye tam bir iş ata, toplam maliyeti minimize et.

Macar Algoritması (Kuhn, 1955):
    1. Satır indirgemesi: Her satırdan satır minimumunu çıkar
    2. Sütun indirgemesi: Her sütundan sütun minimumunu çıkar
    3. Minimum satır/sütunla tüm sıfırları örtle (König Teoremi)
    4. Sıfır sayısı < n ise: Örtme sayısına göre revize et ve tekrar
    5. n bağımsız sıfır bulunduğunda optimal atama elde edildi

Karmaşıklık: O(n³)
"""


def hungarian_algorithm(cost_matrix: list) -> tuple:
    """
    Macar Algoritması ile atama problemi optimum çözümü.

    Args:
        cost_matrix: n×n maliyet matrisi

    Returns:
        (assignment, total_cost)
        assignment[i] = j: İşçi i → İş j
    """
    import copy

    n = len(cost_matrix)
    C = [row[:] for row in cost_matrix]  # Çalışma kopyası

    # ADIM 1: Satır indirgemesi
    for i in range(n):
        min_val = min(C[i])
        C[i] = [v - min_val for v in C[i]]

    # ADIM 2: Sütun indirgemesi
    for j in range(n):
        min_val = min(C[i][j] for i in range(n))
        for i in range(n):
            C[i][j] -= min_val

    # ADIM 3-4: Örtme ve revizyon (while döngüsü)
    for _ in range(n):
        # Minimum satır/sütun örtmesi bul (greedy)
        covered_rows = [False] * n
        covered_cols = [False] * n

        # Sıfır ataması (bipartite matching)
        assignment = [-1] * n
        assigned_cols = set()

        # Greedy ön atama
        for i in range(n):
            for j in range(n):
                if C[i][j] == 0 and j not in assigned_cols:
                    assignment[i] = j
                    assigned_cols.add(j)
                    break

        # Bağımsız sıfır sayısı = n ise optimal
        assigned_count = sum(1 for a in assignment if a != -1)
        if assigned_count == n:
            break

        # Örtme adımı
        unassigned_rows = {i for i in range(n) if assignment[i] == -1}
        marked_rows = set(unassigned_rows)
        marked_cols = set()

        changed = True
        while changed:
            changed = False
            for i in marked_rows:
                for j in range(n):
                    if C[i][j] == 0 and j not in marked_cols:
                        marked_cols.add(j)
                        changed = True
            for j in marked_cols:
                for i in range(n):
                    if assignment[i] == j and i not in marked_rows:
                        marked_rows.add(i)
                        changed = True

        covered_rows = [i not in marked_rows for i in range(n)]
        covered_cols = [j in marked_cols for j in range(n)]

        # Örtülü olmayan minimumu bul
        uncovered_vals = [
            C[i][j]
            for i in range(n) for j in range(n)
            if not covered_rows[i] and not covered_cols[j]
        ]
        if not uncovered_vals:
            break

        min_val = min(uncovered_vals)

        # Matrisi revize et
        for i in range(n):
            for j in range(n):
                if not covered_rows[i] and not covered_cols[j]:
                    C[i][j] -= min_val
                elif covered_rows[i] and covered_cols[j]:
                    C[i][j] += min_val

    # Son optimal atama (Hungarian matching)
    assign = _hungarian_match(C, n)

    total = sum(cost_matrix[i][assign[i]] for i in range(n))
    return assign, total


def _hungarian_match(C: list, n: int) -> list:
    """Azaltılmış matristeki sıfırlarda maksimum eşleşme bul."""
    assignment = [-1] * n
    used_cols = [False] * n

    def dfs(row, visited):
        for col in range(n):
            if C[row][col] == 0 and not visited[col]:
                visited[col] = True
                if not used_cols[col] or dfs(assignment_col[col], visited):
                    used_cols[col] = True
                    assignment[row] = col
                    assignment_col[col] = row
                    return True
        return False

    assignment_col = [-1] * n
    for i in range(n):
        visited = [False] * n
        dfs(i, visited)

    return assignment


def print_cost_matrix(matrix: list, row_names: list = None,
                      col_names: list = None, title: str = "Maliyet Matrisi"):
    """Maliyet matrisini formatlı yazdır."""
    n = len(matrix)
    rows = row_names or [f"İşçi {i+1}" for i in range(n)]
    cols = col_names or [f"İş {j+1}" for j in range(n)]

    print(f"\n  ┌─ {title} ─────")
    header = f"  │ {'':>10}" + "".join(f"{c:>8}" for c in cols)
    print(header)
    print(f"  │ {'─'*len(header)}")
    for i in range(n):
        row = f"  │ {rows[i]:>10}" + "".join(f"{matrix[i][j]:>8}" for j in range(n))
        print(row)
    print(f"  └{'─'*(len(header)+2)}")


def run_demo():
    print("=" * 60)
    print("  👔  MACAR ALGORİTMASI — OPTİMAL ATAMA PROBLEMİ")
    print("=" * 60)

    # --- Örnek 1: 4x4 klasik atama ---
    print("\n[ÖRNEK 1] 4 İşçi, 4 Proje — Maliyet Minimizasyonu:")
    cost1 = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]
    workers  = ["Ali", "Ayşe", "Mehmet", "Fatma"]
    projects = ["Proje A", "Proje B", "Proje C", "Proje D"]

    print_cost_matrix(cost1, workers, projects, "Maliyet Matrisi (TL/saat)")

    assign1, cost_total1 = hungarian_algorithm(cost1)

    print(f"\n  ✅ OPTIMAL ATAMA:")
    print(f"  {'İşçi':>10} {'Proje':>12} {'Maliyet':>10}")
    print(f"  {'─'*35}")
    for i, j in enumerate(assign1):
        print(f"  {workers[i]:>10} {projects[j]:>12} {cost1[i][j]:>8} TL/saat")
    print(f"  {'─'*35}")
    print(f"  {'TOPLAM':>10} {'':>12} {cost_total1:>8} TL/saat")

    # --- Örnek 2: Maksimizasyon (kâr atama) ---
    print("\n\n[ÖRNEK 2] Kâr Maksimizasyonu (Büyük-Küçük dönüşümü):")
    profit = [
        [5, 9, 3, 6],
        [8, 7, 8, 2],
        [2, 2, 7, 9],
        [9, 5, 1, 7]
    ]
    max_val = max(max(row) for row in profit)
    # Dönüşüm: c[i][j] = max - profit[i][j]
    cost2 = [[max_val - profit[i][j] for j in range(4)] for i in range(4)]

    print_cost_matrix(profit, workers, projects, "Kâr Matrisi")
    print_cost_matrix(cost2, workers, projects, "Dönüştürülmüş Maliyet (max - kâr)")

    assign2, _ = hungarian_algorithm(cost2)
    total_profit = sum(profit[i][assign2[i]] for i in range(4))

    print(f"\n  ✅ MAKSIMUM KÂR ATAMASI:")
    for i, j in enumerate(assign2):
        print(f"    {workers[i]:>8} → {projects[j]:<12}: {profit[i][j]} kâr")
    print(f"  Toplam Kâr: {total_profit}")

    # --- Örnek 3: 5x5 ---
    print("\n\n[ÖRNEK 3] 5x5 Makine-İş Çizelgeleme:")
    cost3 = [
        [3, 9, 2, 3, 7],
        [6, 1, 8, 1, 8],
        [2, 4, 7, 5, 1],
        [2, 8, 1, 7, 3],
        [5, 7, 8, 6, 4]
    ]
    machines = [f"Makine {i+1}" for i in range(5)]
    jobs = [f"İş {j+1}" for j in range(5)]
    print_cost_matrix(cost3, machines, jobs)
    assign3, cost3_total = hungarian_algorithm(cost3)
    print(f"\n  Optimal Atama: {[f'M{i+1}→J{assign3[i]+1}' for i in range(5)]}")
    print(f"  Minimum Maliyet: {cost3_total}")

    print("\n" + "=" * 60)
    print("  Macar Algoritması O(n³) — n=100 için bile milisaniyeler!")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
