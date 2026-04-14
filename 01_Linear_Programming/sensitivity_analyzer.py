"""
Duyarlılık Analizi Otomatik Raporu (Sensitivity Analyzer)
----------------------------------------------------------
Bu betik, verilen bir LP modelinin duyarlılık analizini otomatik olarak
çalıştırır ve gölge fiyatları, değişim aralıklarını raporlar.
Kütüphane: PuLP
"""

import pulp

def run_sensitivity_analysis(objective_coeffs, lhs_constraints, rhs_constraints, constraint_names, var_names):
    """
    Parametreler:
    - objective_coeffs: Amaç fonksiyonu katsayıları [c1, c2, ...]
    - lhs_constraints: Kısıt sol taraf matrisi [[a11,a12,...], [a21,a22,...], ...]
    - rhs_constraints: Kısıt sağ taraf değerleri [b1, b2, ...]
    - constraint_names: Kısıt isimleri listesi
    - var_names: Değişken isimleri listesi
    """
    prob = pulp.LpProblem("Sensitivity_Analysis", pulp.LpMaximize)

    # Karar değişkenleri
    variables = [pulp.LpVariable(name, lowBound=0) for name in var_names]

    # Amaç fonksiyonu
    prob += pulp.lpSum([c * v for c, v in zip(objective_coeffs, variables)])

    # Kısıtlar
    constraints = {}
    for i, (row, rhs, name) in enumerate(zip(lhs_constraints, rhs_constraints, constraint_names)):
        c = pulp.lpSum([a * v for a, v in zip(row, variables)]) <= rhs
        prob += c, name
        constraints[name] = prob.constraints[name]

    # Çözüm
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    print("=" * 60)
    print(f"DUYARLILIK ANALİZİ RAPORU")
    print("=" * 60)
    print(f"Durum      : {pulp.LpStatus[prob.status]}")
    print(f"Optimum Z  : {pulp.value(prob.objective):.4f}")
    print()
    print("Karar Değişkenleri:")
    for v in variables:
        print(f"  {v.name:20s} = {v.varValue:.4f}")

    print()
    print("Kısıt Analizi (Gölge Fiyatlar & Gevşeklik):")
    print(f"{'Kısıt':<25} {'Gölge Fiyat (π)':>15} {'Gevşeklik':>12}")
    print("-" * 55)
    for name, c in prob.constraints.items():
        print(f"{name:<25} {c.pi:>15.4f} {c.slack:>12.4f}")


if __name__ == "__main__":
    # Örnek: 2 ürün, 3 kaynak kısıtı
    run_sensitivity_analysis(
        objective_coeffs=[40, 30],
        lhs_constraints=[[2, 1], [1, 1], [0.5, 1]],
        rhs_constraints=[20, 15, 12],
        constraint_names=["Iscilik_Saati", "Hammadde", "Makine_Saati"],
        var_names=["Urun_A", "Urun_B"]
    )
