"""
╔══════════════════════════════════════════════════════════════╗
║   0-1 KNAPSACK — Dinamik Programlama (Tabulation + Trace)    ║
║   Yöneylem Araştırması · FAZ 5: Dinamik Programlama          ║
╚══════════════════════════════════════════════════════════════╝

Problem:
    n adet nesne, her birinin ağırlığı w[i] ve değeri v[i].
    Kapasite W olan bir çanta.
    Toplam değeri maksimize et; kural: her nesne ya ya da yoktur (0-1).

DP Geçiş:
    dp[i][w] = max(dp[i-1][w], dp[i-1][w - w[i]] + v[i])   if w[i] <= w
    dp[i][w] = dp[i-1][w]                                   if w[i] > w

Karmaşıklık:
    Zaman: O(n * W)
    Uzay: O(W)  — optimize edilmiş 1D tablo
"""

import time


def knapsack_2d(weights: list, values: list, capacity: int):
    """
    2D DP tablosu ile tam çözüm + backtracking (hangi nesneler seçildi).
    Returns: (max_value, selected_items_list)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Nesne seçme
            dp[i][w] = dp[i - 1][w]
            # Nesne seç (eğer sığıyorsa)
            if weights[i - 1] <= w:
                pick = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], pick)

    # Seçilen nesneleri bul (backtracking)
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)  # 0-indexed
            w -= weights[i - 1]
    selected.reverse()

    return dp[n][capacity], selected


def knapsack_1d_optimized(weights: list, values: list, capacity: int):
    """
    1D DP ile uzay-optimized çözüm — O(W) bellek.
    NOT: Backtracking yapılamaz; sadece optimal değer döner.
    """
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):  # Sağdan sola!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


def print_dp_table(dp: list, weights: list, values: list, capacity: int):
    """DP tablosunu güzel formatlı yazdır."""
    n = len(weights)
    print(f"\n{'─'*60}")
    print(f"  DP TABLOSU (Satır=Nesne 0..{n}, Sütun=Kapasite 0..{capacity})")
    print(f"{'─'*60}")

    # Header
    header = "       " + "".join(f"W={w:3d}" for w in range(min(capacity + 1, 16)))
    print(header)

    for i in range(min(n + 1, 8)):
        label = f"i={i:2d}  " if i > 0 else "Base  "
        row = label + "".join(f"  {dp[i][w]:3d}" for w in range(min(capacity + 1, 16)))
        print(row)

    if capacity > 15 or n > 7:
        print("  ... (tablo büyük, kısaltıldı)")


def benchmark_comparison(weights: list, values: list, capacity: int):
    """2D vs 1D DP performans karşılaştırması."""
    print(f"\n{'═'*50}")
    print("  ⏱️  PERFORMANS KARŞILAŞTIRMASI")
    print(f"{'═'*50}")

    # 2D DP
    t0 = time.perf_counter()
    val_2d, _ = knapsack_2d(weights, values, capacity)
    t1 = time.perf_counter()
    time_2d = (t1 - t0) * 1000

    # 1D DP
    t0 = time.perf_counter()
    val_1d = knapsack_1d_optimized(weights, values, capacity)
    t1 = time.perf_counter()
    time_1d = (t1 - t0) * 1000

    print(f"  2D DP (izleme dahil) : {time_2d:.4f} ms  →  Değer: {val_2d}")
    print(f"  1D DP (optimize)     : {time_1d:.4f} ms  →  Değer: {val_1d}")
    print(f"  Uzay Kazanımı        : O(n*W) → O(W)  ({len(weights)*(capacity+1)} → {capacity+1} hücre)")


def run_demo():
    """Temel demo: ders kitabı örneği."""
    print("=" * 60)
    print("  🎒  0-1 KNAPSACK — DİNAMİK PROGRAMLAMA")
    print("=" * 60)

    # --- Küçük Örnek (el ile izlenebilir) ---
    print("\n[ÖRNEK 1] Ders Kitabı Örneği:")
    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 6]
    capacity = 8
    n = len(weights)

    print(f"  Nesneler: {n} adet")
    print(f"  Ağırlıklar: {weights}")
    print(f"  Değerler  : {values}")
    print(f"  Kapasite  : {capacity}")

    # 2D çözüm için tablo
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                pick = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], pick)

    print_dp_table(dp, weights, values, capacity)

    max_val, selected = knapsack_2d(weights, values, capacity)
    total_weight = sum(weights[i] for i in selected)

    print(f"\n  ✅ Optimal Değer : {max_val}")
    print(f"  📦 Seçilen Nesneler: {[i+1 for i in selected]} (1-indexed)")
    print(f"  ⚖️  Toplam Ağırlık : {total_weight} / {capacity}")

    # --- Büyük Örnek (benchmark) ---
    print("\n[ÖRNEK 2] Büyük Problem (n=20, W=50):")
    import random
    random.seed(42)
    n2 = 20
    w2 = [random.randint(1, 10) for _ in range(n2)]
    v2 = [random.randint(1, 20) for _ in range(n2)]
    cap2 = 50

    max_val2, sel2 = knapsack_2d(w2, v2, cap2)
    print(f"  Optimal Değer   : {max_val2}")
    print(f"  Seçilen Nesne # : {[i+1 for i in sel2]}")
    print(f"  Toplam Ağırlık  : {sum(w2[i] for i in sel2)} / {cap2}")

    benchmark_comparison(w2, v2, cap2)

    print("\n" + "=" * 60)
    print("  Farklı problem için weights/values/capacity değerlerini")
    print("  kod içinden düzenleyebilirsiniz.")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
