"""
╔══════════════════════════════════════════════════════════════╗
║   NASH DENGESİ BULUCU — Karma Strateji (2-Kişilik)           ║
║   Yöneylem Araştırması · FAZ 8: Oyun Teorisi                 ║
╚══════════════════════════════════════════════════════════════╝

Nash Dengesi:
    Strateji profili (p*, q*) öyle ki:
    u1(p*, q*) >= u1(p, q*)   ∀p ∈ Δ(S1)   ← Oyuncu 1 en iyi yanıt
    u2(p*, q*) >= u2(p*, q)   ∀q ∈ Δ(S2)   ← Oyuncu 2 en iyi yanıt

Algoritma (2-Kişilik Genel Toplam Oyun):
    1. Saf strateji Nash dengelerini bul (iterated elimination + best response check)
    2. Karma strateji Nash dengesini LP/analitik yöntemle bul
    3. Destekleyici (support) strateji belirleme
"""

from itertools import product


def find_pure_nash(R: list, C: list) -> list:
    """
    Saf Strateji Nash Dengelerini bul.
    R[i][j] = Oyuncu 1'in kazancı, C[i][j] = Oyuncu 2'nin kazancı.

    Nash Dengesi koşulu:
        - i* = argmax_i R[i][j*]  (Oyuncu 2, j* seçolduğunda O1'in en iyi yanıtı)
        - j* = argmax_j C[i*][j]  (Oyuncu 1, i* seçtiğinde O2'nin en iyi yanıtı)
    """
    m = len(R)
    n = len(R[0])
    nash_equilibria = []

    for i, j in product(range(m), range(n)):
        # Oyuncu 1 en iyi yanıt kontrolü: R[i][j] >= R[k][j] for all k
        is_br1 = all(R[i][j] >= R[k][j] for k in range(m))
        # Oyuncu 2 en iyi yanıt kontrolü: C[i][j] >= C[i][l] for all l
        is_br2 = all(C[i][j] >= C[i][l] for l in range(n))

        if is_br1 and is_br2:
            nash_equilibria.append((i, j, R[i][j], C[i][j]))

    return nash_equilibria


def find_mixed_nash_2x2(R: list, C: list) -> dict:
    """
    2x2 genel toplam oyun için analitik karma strateji Nash dengesi.

    Oyuncu 2, Oyuncu 1'i indifferent bırakacak q'yu seçer:
        R[0][0]*q + R[0][1]*(1-q) = R[1][0]*q + R[1][1]*(1-q)

    Oyuncu 1, Oyuncu 2'yi indifferent bırakacak p'yi seçer:
        C[0][0]*p + C[1][0]*(1-p) = C[0][1]*p + C[1][1]*(1-p)
    """
    # p: Oyuncu 1'in Strateji 1 seçme olasılığı
    denom_p = (C[0][0] - C[1][0] - C[0][1] + C[1][1])
    # q: Oyuncu 2'nin Strateji 1 seçme olasılığı
    denom_q = (R[0][0] - R[0][1] - R[1][0] + R[1][1])

    result = {}

    if abs(denom_p) > 1e-12:
        p = (C[1][1] - C[0][1]) / denom_p
        p = max(0.0, min(1.0, p))
        result['p'] = [p, 1 - p]

        # Oyuncu 1'in beklenen kazancı
        u1_mixed = (R[0][0] * p * (1 - 0) + R[0][1] * p * 0 +
                    R[1][0] * (1-p) * 1 + R[1][1] * (1-p) * 0)
    else:
        result['p'] = None  # Oyuncu 1 indifferent değil

    if abs(denom_q) > 1e-12:
        q = (R[1][1] - R[0][1]) / denom_q

        # Actually: q makes Player 1 indifferent
        # Doğru formül:
        # R00*q + R01*(1-q) = R10*q + R11*(1-q)
        # q*(R00 - R01 - R10 + R11) = R11 - R01
        q = (R[1][1] - R[0][1]) / denom_q if denom_q != 0 else 0.5
        q = max(0.0, min(1.0, q))
        result['q'] = [q, 1 - q]
    else:
        result['q'] = None

    # Beklenen kazançlar
    if result.get('p') and result.get('q'):
        p_val = result['p'][0]
        q_val = result['q'][0]
        eu1 = (R[0][0]*p_val*q_val + R[0][1]*p_val*(1-q_val) +
               R[1][0]*(1-p_val)*q_val + R[1][1]*(1-p_val)*(1-q_val))
        eu2 = (C[0][0]*p_val*q_val + C[0][1]*p_val*(1-q_val) +
               C[1][0]*(1-p_val)*q_val + C[1][1]*(1-p_val)*(1-q_val))
        result['eu1'] = eu1
        result['eu2'] = eu2

    return result


def pareto_analysis(R: list, C: list,
                    row_labels: list = None, col_labels: list = None) -> list:
    """
    Pareto Optimum sonuç profillerini bul.
    (i*,j*) Pareto optimal ← Başka hiçbir (i,j) her iki oyuncuyu da daha iyi yapamaz.
    """
    m = len(R)
    n = len(R[0])
    outcomes = [(i, j, R[i][j], C[i][j]) for i in range(m) for j in range(n)]

    rows = row_labels or [f"S{i+1}" for i in range(m)]
    cols = col_labels or [f"C{j+1}" for j in range(n)]

    pareto_optimal = []
    for (i, j, r, c) in outcomes:
        dominated = False
        for (i2, j2, r2, c2) in outcomes:
            if (i2, j2) != (i, j) and r2 >= r and c2 >= c and (r2 > r or c2 > c):
                dominated = True
                break
        if not dominated:
            pareto_optimal.append((i, j, r, c))

    return pareto_optimal


def print_bimatrix(R: list, C: list, title: str = "Bi-Matris Oyunu",
                   row_labels: list = None, col_labels: list = None):
    """Bi-matris (R, C) oyununu güzel formatlı yazdır."""
    m = len(R)
    n = len(R[0])
    rows = row_labels or [f"R{i+1}" for i in range(m)]
    cols = col_labels or [f"C{j+1}" for j in range(n)]

    print(f"\n  ╔─ {title} ─────────────────────────────")
    header = "                " + "".join(f"{c:>15}" for c in cols)
    print(f"  ║ {header}")
    print(f"  ║ {'─'*len(header)}")
    for i in range(m):
        cells = "".join(f"  ({R[i][j]:4.1f}, {C[i][j]:4.1f})" for j in range(n))
        print(f"  ║ {rows[i]:>12}  {cells}")
    print(f"  ╚{'═'*(len(header)+14)}")
    print(f"           Format: (Oyuncu1 Kazancı, Oyuncu2 Kazancı)")


def run_demo():
    print("=" * 65)
    print("  🤝  NASH DENGESİ BULUCU — KARMA & SAF STRATEJİ ANALİZİ")
    print("=" * 65)

    # --- Örnek 1: Mahkum İkilemi ---
    print("\n[ÖRNEK 1] Mahkum İkilemi (Prisoner's Dilemma):")
    R1 = [[3, 0], [5, 1]]  # Oyuncu 1
    C1 = [[3, 5], [0, 1]]  # Oyuncu 2
    strats1 = ["İşbirliği", "İhanet"]

    print_bimatrix(R1, C1, "Mahkum İkilemi", strats1, strats1)

    nash1 = find_pure_nash(R1, C1)
    print(f"\n  SAF STRATEJİ NASH DENGELERİ:")
    for (i, j, r, c) in nash1:
        print(f"    ★ ({strats1[i]}, {strats1[j]}) → Kazançlar: ({r}, {c})")

    pareto1 = pareto_analysis(R1, C1, strats1, strats1)
    print(f"\n  PARETO OPTIMAL SONUÇLAR:")
    for (i, j, r, c) in pareto1:
        print(f"    ◆ ({strats1[i]}, {strats1[j]}) → ({r}, {c})")

    print(f"\n  ⚠️  Nash ≠ Pareto Optimum → Sosyal ikilem!")

    # --- Örnek 2: Cinsiyet Savaşı (Battle of the Sexes) ---
    print("\n\n[ÖRNEK 2] Cinsiyet Savaşı (Battle of the Sexes):")
    R2 = [[2, 0], [0, 1]]
    C2 = [[1, 0], [0, 2]]
    strats2_r = ["Opera", "Futbol"]
    strats2_c = ["Opera", "Futbol"]

    print_bimatrix(R2, C2, "Battle of the Sexes", strats2_r, strats2_c)

    nash2 = find_pure_nash(R2, C2)
    print(f"\n  SAF NASH DENGELERİ ({len(nash2)} adet):")
    for (i, j, r, c) in nash2:
        print(f"    ★ ({strats2_r[i]}, {strats2_c[j]}) → ({r}, {c})")

    mixed2 = find_mixed_nash_2x2(R2, C2)
    print(f"\n  KARMA STRATEJI NASH DENGESİ:")
    if mixed2.get('p'):
        print(f"    Oyuncu 1: Opera={mixed2['p'][0]:.3f}, Futbol={mixed2['p'][1]:.3f}")
    if mixed2.get('q'):
        print(f"    Oyuncu 2: Opera={mixed2['q'][0]:.3f}, Futbol={mixed2['q'][1]:.3f}")
    if 'eu1' in mixed2:
        print(f"    Beklenen Kazanç: O1={mixed2['eu1']:.3f}, O2={mixed2['eu2']:.3f}")

    # --- Örnek 3: Tavuk Oyunu (Chicken) ---
    print("\n\n[ÖRNEK 3] Tavuk Oyunu (Chicken / Hawk-Dove):")
    R3 = [[0, -1], [1, -10]]
    C3 = [[0, 1], [-1, -10]]
    strats3 = ["Geri Dön", "Devam"]

    print_bimatrix(R3, C3, "Tavuk Oyunu", strats3, strats3)

    nash3 = find_pure_nash(R3, C3)
    print(f"\n  SAF NASH DENGELERİ ({len(nash3)} adet):")
    for (i, j, r, c) in nash3:
        print(f"    ★ ({strats3[i]}, {strats3[j]}) → ({r}, {c})")

    mixed3 = find_mixed_nash_2x2(R3, C3)
    print(f"\n  KARMA STRATEJI NASH DENGESİ:")
    if mixed3.get('p'):
        print(f"    Oyuncu 1: Geri Dön={mixed3['p'][0]:.4f}, Devam={mixed3['p'][1]:.4f}")
    if mixed3.get('q'):
        print(f"    Oyuncu 2: Geri Dön={mixed3['q'][0]:.4f}, Devam={mixed3['q'][1]:.4f}")

    print("\n" + "=" * 65)
    print("  3 Nash dengesi türü:")
    print("   1. Saf strateji NE   → belirli hamle seç")
    print("   2. Karma strateji NE → olasılığa göre rastgele seç")
    print("   3. Karma destek (support) NE → alt kümede karma")
    print("=" * 65)


if __name__ == "__main__":
    run_demo()
