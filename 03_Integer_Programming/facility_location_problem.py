"""
Tesis Yer Seçimi Problemi (Facility Location Problem) Çözücü
-----------------------------------------------------------
Bu betik, belirli müşteri noktalarına hizmet verecek tesislerin lokasyonlarını 
ve hangi müşterinin hangi tesisten hizmet alacağını optimize eder.

Problem: Fixed-Charge Facility Location Problem (FCFLP)
Kütüphane: PuLP
"""

import pulp

def solve_facility_location():
    # 1. Veri Tanımlama
    # Tesis lokasyonları ve sabit kurulum maliyetleri
    facilities = ['Depo_1', 'Depo_2', 'Depo_3']
    setup_cost = {'Depo_1': 1000, 'Depo_2': 1200, 'Depo_3': 1100}

    # Müşteri noktaları ve talepleri
    customers = ['Musteri_A', 'Musteri_B', 'Musteri_C', 'Musteri_D']
    
    # Taşıma maliyetleri (Tesis -> Müşteri)
    shipping_costs = {
        'Depo_1': {'Musteri_A': 4, 'Musteri_B': 5, 'Musteri_C': 6, 'Musteri_D': 8},
        'Depo_2': {'Musteri_A': 6, 'Musteri_B': 4, 'Musteri_C': 3, 'Musteri_D': 5},
        'Depo_3': {'Musteri_A': 8, 'Musteri_B': 6, 'Musteri_C': 5, 'Musteri_D': 2}
    }

    # 2. Problem Tanımlama
    prob = pulp.LpProblem("Facility_Location_Problem", pulp.LpMinimize)

    # 3. Karar Değişkenleri
    # y[i]: i tesisi açılırsa 1, açılmazsa 0 (Binary)
    use_facility = pulp.LpVariable.dicts("UseFacility", facilities, 0, 1, pulp.LpBinary)

    # x[i][j]: j müşterisi i tesisinden hizmet alırsa 1 (Binary)
    assign = pulp.LpVariable.dicts("Assign", (facilities, customers), 0, 1, pulp.LpBinary)

    # 4. Amaç Fonksiyonu
    # Toplam Maliyet = Sabit Kurulum Maliyetleri + Değişken Taşıma Maliyetleri
    prob += pulp.lpSum([setup_cost[i] * use_facility[i] for i in facilities]) + \
            pulp.lpSum([shipping_costs[i][j] * assign[i][j] for i in facilities for j in customers])

    # 5. Kısıtlar
    # Her müşteri mutlaka bir (ve sadece bir) tesise atanmalıdır
    for j in customers:
        prob += pulp.lpSum([assign[i][j] for i in facilities]) == 1

    # Bir tesise müşteri atanabilmesi için o tesisin açık olması gerekir
    for i in facilities:
        for j in customers:
            prob += assign[i][j] <= use_facility[i]

    # 6. Çözüm
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    # 7. Sonuçları Yazdırma
    print(f"Durum: {pulp.LpStatus[prob.status]}")
    print(f"Minimum Toplam Maliyet: {pulp.value(prob.objective)}")
    
    print("\nAçılan Tesisler:")
    for i in facilities:
        if pulp.value(use_facility[i]) > 0.5:
            print(f"- {i}")

    print("\nMüşteri Atamaları:")
    for i in facilities:
        for j in customers:
            if pulp.value(assign[i][j]) > 0.5:
                print(f"- {j} -> {i} üzerinden hizmet alıyor.")

if __name__ == "__main__":
    solve_facility_location()
