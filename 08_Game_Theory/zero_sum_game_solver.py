"""
╔══════════════════════════════════════════════════════════════╗
║   SIFIR TOPLAMLI OYUN ÇÖZÜCÜsü — Minimax + LP               ║
║   Yöneylem Araştırması · FAZ 8: Oyun Teorisi                 ║
╚══════════════════════════════════════════════════════════════╝

Sıfır Toplamlı Oyun:
    İki oyunculu, Oyuncu 1'in kazancı Oyuncu 2'nin kaybıdır.
    Kazanç matrisi A[i][j]: Satır oyuncusu i, Sütun oyuncusu j seçerse
    Oyuncu 1'in kazancı.

Çözüm Yöntemi:
    1. Sadece saf strateji Nash dengesi ara (eyer noktası — saddle point)
    2. Saf denge yoksa → LP ile karma (mixed) strateji dengesi bul

LP Formülasyonu (Oyuncu 1):
    max  v
    s.t. sum_i (A[i][j] * p[i]) >= v   for all j
         sum_i p[i] = 1
         p[i] >= 0
"""


def find_saddle_point(A: list) -> tuple:
    """
    Eyer noktası (saddle point / pure strategy Nash equilibrium) arar.
    Eyer noktası: satır minimumlarının maksimumu = sütun maksimumlarının minimumu

    Returns:
        (row, col, value) veya None (eyer noktası yoksa)
    """
    m = len(A)
    n = len(A[0])

    # Her satırın minimumu
    row_mins = [min(A[i]) for i in range(m)]
    # Her sütunun maksimumu
    col_maxs = [max(A[i][j] for i in range(m)) for j in range(n)]

    maximin = max(row_mins)
    minimax = min(col_maxs)

    if abs(maximin - minimax) < 1e-9:
        # Eyer noktaları bul
        saddle_points = []
        for i in range(m):
            for j in range(n):
                if abs(A[i][j] - maximin) < 1e-9:
                    saddle_points.append((i, j, A[i][j]))
        return saddle_points
    return []


def solve_mixed_strategy_lp(A: list) -> dict:
    """
    LP ile karma strateji Nash dengesi çöz.
    PuLP kullanır; yoksa manuel iterasyon yöntemi.

    Returns:
        {
          'p': Oyuncu 1 karma stratejisi (satır olasılıkları),
          'q': Oyuncu 2 karma stratejisi (sütun olasılıkları),
          'value': Oyunun değeri
        }
    """
    m = len(A)
    n = len(A[0])

    try:
        import pulp

        # Oyuncu 1: max v  s.t. A^T p >= v, sum p = 1, p >= 0
        prob1 = pulp.LpProblem("ZeroSum_Player1", pulp.LpMaximize)
        p = [pulp.LpVariable(f"p{i}", lowBound=0) for i in range(m)]
        v = pulp.LpVariable("v", cat='Continuous')

        prob1 += v  # Amaç: max v

        for j in range(n):
            prob1 += pulp.lpSum(A[i][j] * p[i] for i in range(m)) >= v

        prob1 += pulp.lpSum(p) == 1
        prob1.solve(pulp.PULP_CBC_CMD(msg=0))

        p_vals  = [pulp.value(p[i]) for i in range(m)]
        game_val = pulp.value(v)

        # Oyuncu 2: min V  s.t. A q <= V, sum q = 1, q >= 0
        prob2 = pulp.LpProblem("ZeroSum_Player2", pulp.LpMinimize)
        q = [pulp.LpVariable(f"q{j}", lowBound=0) for j in range(n)]
        V = pulp.LpVariable("V", cat='Continuous')

        prob2 += V
        for i in range(m):
            prob2 += pulp.lpSum(A[i][j] * q[j] for j in range(n)) <= V

        prob2 += pulp.lpSum(q) == 1
        prob2.solve(pulp.PULP_CBC_CMD(msg=0))

        q_vals = [pulp.value(q[j]) for j in range(n)]

        return {'p': p_vals, 'q': q_vals, 'value': game_val, 'solver': 'PuLP'}

    except ImportError:
        # PuLP yoksa: 2x2 oyunlar için analitik çözüm
        if m == 2 and n == 2:
            return _solve_2x2_analytical(A)
        return {'error': 'PuLP kurulu değil ve oyun 2x2 değil.'}


def _solve_2x2_analytical(A: list) -> dict:
    """
    2x2 sıfır toplamlı oyun için analitik karma strateji çözümü.
    """
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    # p1 = P(Row 1), q1 = P(Col 1)
    denom_p = (a - b - c + d)
    denom_q = (a - b - c + d)

    if abs(denom_p) < 1e-12:
        return {'error': 'Payda sıfır — degenerate oyun'}

    p1 = (d - c) / denom_p
    q1 = (d - b) / denom_q
    value = (a * d - b * c) / denom_p

    return {
        'p': [max(0.0, min(1.0, p1)), 1 - max(0.0, min(1.0, p1))],
        'q': [max(0.0, min(1.0, q1)), 1 - max(0.0, min(1.0, q1))],
        'value': value,
        'solver': 'Analitik (2x2)'
    }


def dominance_reduction(A: list, verbose: bool = True) -> list:
    """
    Baskınlık (dominance) eliminasyonu ile matrisi küçült.
    Katı baskınlık: Strateji i'nin tüm j'lerde strateji k'dan iyi olması.
    """
    A_work = [row[:] for row in A]
    eliminated_rows = []
    eliminated_cols = []

    if verbose:
        print(f"\n  🔍 Baskınlık Eliminasyonu:")

    # Satır baskınlığı (Oyuncu 1 için strictly dominated satırları at)
    changed = True
    while changed:
        changed = False
        dominated_row = None
        for i in range(len(A_work)):
            for k in range(len(A_work)):
                if i == k:
                    continue
                if all(A_work[k][j] > A_work[i][j] for j in range(len(A_work[0]))):
                    dominated_row = i
                    break
            if dominated_row is not None:
                break

        if dominated_row is not None:
            if verbose:
                print(f"    Satır {dominated_row} baskın → kaldırıldı")
            A_work.pop(dominated_row)
            changed = True

    return A_work


def print_matrix(A: list, title: str = "Kazanç Matrisi",
                 row_labels: list = None, col_labels: list = None):
    """Kazanç matrisini güzel formatlı yazdır."""
    m = len(A)
    n = len(A[0])
    rows = row_labels or [f"Strateji R{i+1}" for i in range(m)]
    cols = col_labels or [f"C{j+1}" for j in range(n)]

    print(f"\n  ┌─ {title} ({'%dx%d' % (m,n)}) ──────────────")
    header = "           " + "  ".join(f"{c:>10}" for c in cols)
    print(f"  │ {header}")
    print(f"  │ {'─'*len(header)}")
    for i in range(m):
        row_str = "  ".join(f"{A[i][j]:>10.2f}" for j in range(n))
        print(f"  │ {rows[i]:>10}  {row_str}")
    print(f"  └{'─'*(len(header)+12)}")


def run_demo():
    print("=" * 65)
    print("  ♟️  SIFIR TOPLAMLI OYUN ÇÖZÜCÜsÜ — MİNİMAX + LP")
    print("=" * 65)

    # --- Örnek 1: Eyer noktası olan oyun ---
    print("\n[ÖRNEK 1] Eyer Noktası (Saf Strateji Nash Dengesi) Olan Oyun:")
    A1 = [
        [3, -2,  2],
        [-1,  0,  4],
        [-4,  5,  3]
    ]
    rows1 = ["Kuzey", "Merkez", "Güney"]
    cols1 = ["Sol", "Orta", "Sağ"]
    print_matrix(A1, "Rekabetçi Oyun #1", rows1, cols1)

    saddles = find_saddle_point(A1)
    if saddles:
        for r, c, val in saddles:
            print(f"\n  ✅ Eyer Noktası → ({rows1[r]}, {cols1[c]}) = {val}")
            print(f"  Maximin = Minimax = {val}")
            print(f"  → Saf Strateji Nash Dengesi mevcut!")
    else:
        print("\n  ⚠️ Eyer Noktası YOK → Karma strateji gerekli")

    # --- Örnek 2: Karma strateji gerektiren oyun ---
    print("\n\n[ÖRNEK 2] Karma Strateji Gerektiren Oyun (Taş-Kağıt-Makas):")
    A2 = [
        [ 0, -1,  1],
        [ 1,  0, -1],
        [-1,  1,  0]
    ]
    moves = ["Taş", "Kağıt", "Makas"]
    print_matrix(A2, "Taş-Kağıt-Makas", moves, moves)

    saddles2 = find_saddle_point(A2)
    print(f"\n  Eyer Noktası: {'Var' if saddles2 else 'YOK — Karma strateji gerekli'}")

    result2 = solve_mixed_strategy_lp(A2)
    if 'error' not in result2:
        print(f"\n  📊 Karma Strateji Çözümü ({result2['solver']}):")
        for i, p in enumerate(result2['p']):
            print(f"    Oyuncu 1 → {moves[i]}: {p:.4f} ({p*100:.1f}%)")
        print(f"  Oyunun Değeri V* = {result2['value']:.4f}")
        print(f"  → Simetrik oyun: V*=0, her strateji 1/3 olasılıkla ✅")

    # --- Örnek 3: Mahkum İkilemi (sıfır toplamlı değil ama analiz) ---
    print("\n\n[ÖRNEK 3] 2x2 Rekabetçi Oyun — Karma Strateji Hesabı:")
    A3 = [
        [ 4, -4],
        [-3,  9]
    ]
    rows3 = ["Saldır", "Geri Çekil"]
    cols3 = ["Savun", "Kaç"]
    print_matrix(A3, "Askeri Strateji Oyunu", rows3, cols3)

    saddles3 = find_saddle_point(A3)
    if not saddles3:
        result3 = solve_mixed_strategy_lp(A3)
        if 'error' not in result3:
            print(f"\n  📊 Analitik Karma Strateji ({result3['solver']}):")
            for i, prob in enumerate(result3['p']):
                print(f"    Oyuncu 1 → {rows3[i]}: p={prob:.4f}")
            for j, prob in enumerate(result3['q']):
                print(f"    Oyuncu 2 → {cols3[j]}: q={prob:.4f}")
            print(f"  Oyunun Değeri: {result3['value']:.4f}")

    # Baskınlık eliminasyonu
    print("\n\n[ÖRNEK 4] Baskınlık Eliminasyonu Örneği:")
    A4 = [
        [6, 3, 7],
        [5, 8, 2],
        [8, 4, 6]
    ]
    print_matrix(A4, "Orijinal Matris 3x3")
    reduced = dominance_reduction(A4, verbose=True)
    print_matrix(reduced, "Eliminasyon Sonrası")

    print("\n" + "=" * 65)
    print("  Kendi kazanç matrisinizi A değişkenine yazabilirsiniz.")
    print("=" * 65)


if __name__ == "__main__":
    run_demo()
