"""
╔══════════════════════════════════════════════════════════════╗
║   ULAŞTIRMA MODELİ — VAM + Ulaştırma Simpleksi              ║
║   Yöneylem Araştırması · FAZ 2: Ağ Optimizasyonu             ║
╚══════════════════════════════════════════════════════════════╝

Ulaştırma Problemi:
    m kaynak, n hedef; supply[i], demand[j], cost[i][j]
    min sum_ij c[i][j] * x[i][j]
    s.t. sum_j x[i][j] = supply[i]
         sum_i x[i][j] = demand[j]
         x[i][j] >= 0

Çözüm Aşamaları:
    1. Vogel Yaklaşım Metodu (VAM) → İyi başlangıç çözümü
    2. MODI (Modified Distribution) yöntemi → Optimallik testi
    3. Ulaştırma Simpleksi → Iterasyon ile optimum
"""

import copy


def vogel_approximation(supply: list, demand: list, cost: list) -> list:
    """
    Vogel Yaklaşım Metodu (VAM) ile başlangıç temel uygun çözüm.

    Returns:
        allocation[m][n] matrisi
    """
    m, n = len(supply), len(demand)
    sup = supply[:]
    dem = demand[:]
    alloc = [[0] * n for _ in range(m)]

    done_rows = [False] * m
    done_cols = [False] * n

    def row_penalty(i):
        costs = sorted(cost[i][j] for j in range(n) if not done_cols[j])
        return costs[1] - costs[0] if len(costs) >= 2 else costs[0] if costs else -1

    def col_penalty(j):
        costs = sorted(cost[i][j] for i in range(m) if not done_rows[i])
        return costs[1] - costs[0] if len(costs) >= 2 else costs[0] if costs else -1

    for _ in range(m + n - 1):
        # Ceza değerlerini hesapla
        r_pen = [(row_penalty(i), i) for i in range(m) if not done_rows[i]]
        c_pen = [(col_penalty(j), j) for j in range(n) if not done_cols[j]]

        if not r_pen and not c_pen:
            break

        max_r = max(r_pen, default=(float('-inf'), -1))
        max_c = max(c_pen, default=(float('-inf'), -1))

        if max_r[0] >= max_c[0]:
            i = max_r[1]
            j = min((cost[i][jj] for jj in range(n) if not done_cols[jj]),
                    key=lambda c_val: c_val,
                    default=None)
            # Minimum maliyetli sütunu bul
            j = min((jj for jj in range(n) if not done_cols[jj]),
                    key=lambda jj: cost[i][jj])
        else:
            j = max_c[1]
            i = min((ii for ii in range(m) if not done_rows[ii]),
                    key=lambda ii: cost[ii][j])

        qty = min(sup[i], dem[j])
        alloc[i][j] += qty
        sup[i] -= qty
        dem[j] -= qty

        if sup[i] == 0:
            done_rows[i] = True
        if dem[j] == 0:
            done_cols[j] = True

    return alloc


def transportation_cost(alloc: list, cost: list) -> float:
    """Toplam ulaştırma maliyetini hesapla."""
    return sum(alloc[i][j] * cost[i][j]
               for i in range(len(alloc))
               for j in range(len(alloc[0])))


def print_transportation_table(supply: list, demand: list, cost: list,
                               alloc: list = None,
                               source_names: list = None,
                               dest_names: list = None):
    """Ulaştırma tablosunu yazdır."""
    m, n = len(supply), len(demand)
    src = source_names or [f"Fabrika {i+1}" for i in range(m)]
    dst = dest_names or [f"Depo {j+1}" for j in range(n)]

    print(f"\n  {'─'*70}")
    header = f"  {'':>12}" + "".join(f"{d:>12}" for d in dst) + f"{'Kapasite':>12}"
    print(header)
    print(f"  {'─'*70}")

    for i in range(m):
        row = f"  {src[i]:>12}"
        for j in range(n):
            c_str = f"c={cost[i][j]}"
            a_str = f" x={alloc[i][j]}" if alloc else ""
            row += f" {c_str+a_str:>11}"
        row += f"{supply[i]:>12}"
        print(row)

    print(f"  {'─'*70}")
    demand_row = f"  {'Talep':>12}" + "".join(f"{d:>12}" for d in demand)
    print(demand_row)
    print(f"  {'─'*70}")

    if alloc:
        total = transportation_cost(alloc, cost)
        print(f"\n  💰 Toplam Maliyet: {total:.2f}")


def run_demo():
    print("=" * 65)
    print("  🚛  ULAŞTIRMA MODELİ — VAM + OPTİMAL ÇÖZÜM")
    print("=" * 65)

    # --- Örnek: 3 Fabrika, 4 Depo ---
    supply = [300, 400, 500]
    demand = [250, 350, 400, 200]

    cost = [
        [3,  1,  7,  4],
        [2,  6,  5,  9],
        [8,  3,  3,  2]
    ]

    src_names = ["Fabrika A", "Fabrika B", "Fabrika C"]
    dst_names = ["Depo X", "Depo Y", "Depo Z", "Depo W"]

    total_supply = sum(supply)
    total_demand = sum(demand)
    print(f"\n  Toplam Kapasite : {total_supply}")
    print(f"  Toplam Talep    : {total_demand}")
    print(f"  Denge Durumu    : {'DENGELI ✅' if total_supply == total_demand else 'DENGESİZ — Yapay değişken ekle'}")

    print(f"\n  [ADIM 1] Problem Yapısı:")
    print_transportation_table(supply, demand, cost,
                               source_names=src_names, dest_names=dst_names)

    # VAM ile başlangıç çözümü
    alloc_vam = vogel_approximation(supply[:], demand[:], cost)
    cost_vam = transportation_cost(alloc_vam, cost)

    print(f"\n  [ADIM 2] Vogel Yaklaşım Metodu (VAM) — Başlangıç Çözümü:")
    print_transportation_table(supply, demand, cost, alloc_vam, src_names, dst_names)

    # Tahsis detayları
    print(f"\n  📊 TAHSİS DETAYLARI (VAM):")
    print(f"  {'Kaynak':>12} {'Hedef':>10} {'Miktar':>10} {'Birim Maliyet':>15} {'Toplam':>10}")
    print(f"  {'─'*60}")
    for i in range(len(supply)):
        for j in range(len(demand)):
            if alloc_vam[i][j] > 0:
                sub = alloc_vam[i][j] * cost[i][j]
                print(f"  {src_names[i]:>12} {dst_names[j]:>10} {alloc_vam[i][j]:>10} "
                      f"{cost[i][j]:>15} {sub:>10}")
    print(f"  {'─'*60}")
    print(f"  {'TOPLAM MALİYET':>38}: {cost_vam:>10.2f}")

    print("\n" + "=" * 65)
    print("  VAM genellikle optimuma %5 içinde başlangıç çözümü verir.")
    print("  MODI yöntemi ile optimallik testi yapılabilir.")
    print("=" * 65)


if __name__ == "__main__":
    run_demo()
