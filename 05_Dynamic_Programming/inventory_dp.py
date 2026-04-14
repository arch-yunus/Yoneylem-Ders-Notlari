"""
╔══════════════════════════════════════════════════════════════╗
║   STOK YÖNETİMİ — Dinamik Programlama (Wagner-Whitin)        ║
║   Yöneylem Araştırması · FAZ 5: Dinamik Programlama          ║
╚══════════════════════════════════════════════════════════════╝

Problem (Klasik Stok Yönetimi / Lot Sizing):
    T dönem boyunca d[t] talebi karşıla.
    Üretim (sipariş) maliyeti: setup maliyeti K + birim üretim c[t]
    Stok tutma maliyeti: h birim/dönem
    Başlangıç stoku: I0 = 0, son stok >= 0.

    Amaç: Toplam maliyeti minimize et.

Bellman Denklemi:
    C(t, I) = min_{x >= max(0, d[t]-I)} [
        K*delta(x) + c[t]*x + h*(I + x - d[t]) + C(t+1, I + x - d[t])
    ]

Wagner-Whitin'in Önemli Sonucu:
    Optimal çözümde sipariş verilen dönemde stok sıfırdır (Zero Inventory Property).
    Bu da tablonun yalnızca stok=0 noktalarında hesaplanmasına izin verir.
"""


def wagner_whitin(demands: list, setup_cost: float, holding_cost: float,
                  unit_cost: float = 0.0):
    """
    Wagner-Whitin eksakt algoritması.
    Zero Inventory Ordering Property kullanan O(T^2) DP.

    Args:
        demands      : d[t] — her dönemin talebi (T eleman)
        setup_cost   : K — sipariş (setup) sabit maliyeti
        holding_cost : h — birim başına stok tutma maliyeti/dönem
        unit_cost    : c — birim üretim/sipariş maliyeti

    Returns:
        (total_cost, order_periods, order_qtys)
    """
    T = len(demands)
    INF = float('inf')

    # c_ij: i döneminde sipariş ver, j..i dönemlerini karşıla
    # Maliyet = K + c*(d[j]+...+d[i]) + h*(dönem ağırlıklı stok)
    cost_matrix = [[0.0] * T for _ in range(T)]
    for i in range(T):      # sipariş dönemi
        cumulative_demand = 0
        holding = 0.0
        for j in range(i, T):  # karşılanan son dönem
            demand_j = demands[j]
            cumulative_demand += demand_j
            # Stok tutma: talep j-i dönem elde tutulur
            holding += holding_cost * demand_j * (j - i)
            cost_matrix[i][j] = setup_cost + unit_cost * cumulative_demand + holding

    # DP: f[t] = t dönemine kadar (dahil) minimum toplam maliyet
    f = [INF] * (T + 1)
    f[0] = 0.0
    pred = [-1] * (T + 1)   # geri izleme için

    for t in range(1, T + 1):
        for s in range(t):  # s döneminde sipariş ver → t'ye kadar karşıla
            cost = f[s] + cost_matrix[s][t - 1]
            if cost < f[t]:
                f[t] = cost
                pred[t] = s

    # Geri izleme: sipariş dönemleri
    order_periods = []
    t = T
    while t > 0:
        s = pred[t]
        order_periods.append(s)
        t = s
    order_periods.reverse()

    # Sipariş miktarları
    order_qtys = []
    for k, start in enumerate(order_periods):
        end = order_periods[k + 1] if k + 1 < len(order_periods) else T
        qty = sum(demands[start:end])
        order_qtys.append(qty)

    return f[T], order_periods, order_qtys


def simulate_inventory(demands: list, order_periods: list, order_qtys: list,
                       holding_cost: float, setup_cost: float, unit_cost: float = 0.0):
    """
    Verilen sipariş planını simüle eder ve dönem dönem rapor üretir.
    """
    T = len(demands)
    order_map = dict(zip(order_periods, order_qtys))

    print(f"\n{'─'*72}")
    print(f"{'Dönem':>6} {'Talep':>8} {'Sipariş':>9} {'Stok(Baş)':>10} "
          f"{'Stok(Son)':>10} {'Maliyet':>10}")
    print(f"{'─'*72}")

    inventory = 0
    total_cost = 0.0
    for t in range(T):
        order = order_map.get(t, 0)
        inv_before = inventory + order
        inv_after  = inv_before - demands[t]
        period_cost = (setup_cost if order > 0 else 0) + \
                      unit_cost * order + \
                      holding_cost * inv_after
        total_cost += period_cost

        print(f"  t={t+1:2d}   {demands[t]:7.0f}   {order:8.0f}   {inv_before:9.0f}   "
              f"{inv_after:9.0f}   {period_cost:9.2f}")
        inventory = inv_after

    print(f"{'─'*72}")
    print(f"{'TOPLAM MALİYET':>50}: {total_cost:10.2f}")
    return total_cost


def naive_lot_for_lot(demands: list, setup_cost: float,
                      holding_cost: float, unit_cost: float = 0.0):
    """
    Karşılaştırma için basit Lot-for-Lot politikası.
    Her dönem tam talep kadar sipariş ver.
    """
    total = sum(setup_cost + unit_cost * d for d in demands)
    # Lot-for-Lot'ta stok sıfır kalır
    return total


def run_demo():
    print("=" * 72)
    print("  📦  STOK YÖNETİMİ — WAGNER-WHİTİN DİNAMİK PROGRAMLAMA")
    print("=" * 72)

    # --- Örnek Problem (Hillier & Lieberman tarzı) ---
    demands       = [10, 62, 12, 130, 154, 129, 88, 52, 124, 160, 238, 41]
    setup_cost    = 85.0   # K
    holding_cost  = 1.0    # h (birim/dönem)
    unit_cost     = 0.0    # c (üretim birim maliyeti)

    T = len(demands)
    print(f"\n  Problem: {T} dönem, Talep = {demands}")
    print(f"  Setup Maliyeti (K) = {setup_cost}")
    print(f"  Stok Tutma  (h)    = {holding_cost}/birim/dönem")

    # Wagner-Whitin DP çözümü
    opt_cost, order_periods, order_qtys = wagner_whitin(
        demands, setup_cost, holding_cost, unit_cost
    )

    print(f"\n  🏆 WAGNER-WHİTİN OPTIMAL ÇÖZÜM:")
    print(f"  Sipariş Dönemleri : {[p+1 for p in order_periods]} (1-indexed)")
    print(f"  Sipariş Miktarları: {order_qtys}")
    print(f"  Toplam Optimal Maliyet: {opt_cost:.2f}")

    # Simülasyon
    print("\n  📊 DÖNEM BAZLI STOK SİMÜLASYONU:")
    simulate_inventory(demands, order_periods, order_qtys,
                       holding_cost, setup_cost, unit_cost)

    # Lot-for-Lot karşılaştırması
    lot_cost = naive_lot_for_lot(demands, setup_cost, holding_cost, unit_cost)
    savings  = lot_cost - opt_cost
    savings_pct = (savings / lot_cost) * 100

    print(f"\n  ⚡ KARŞILAŞTIRMA:")
    print(f"  Lot-for-Lot Maliyeti : {lot_cost:.2f}")
    print(f"  Wagner-Whitin        : {opt_cost:.2f}")
    print(f"  Tasarruf             : {savings:.2f} ({savings_pct:.1f}%)")

    print("\n" + "=" * 72)
    print("  Demands, setup_cost, holding_cost değerlerini değiştirerek")
    print("  kendi problemlerinizi çözebilirsiniz.")
    print("=" * 72)


if __name__ == "__main__":
    run_demo()
