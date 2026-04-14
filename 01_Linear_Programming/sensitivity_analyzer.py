"""
⚙️ Yoneylem-Ders-Notlari: Linear Programming Tool
Post-Optimality / Sensitivity Analyzer
"""

from scipy.optimize import linprog
import numpy as np

class SensitivityAnalyzer:
    def __init__(self, c, A, b):
        self.c = np.array(c)
        self.A = np.array(A)
        self.b = np.array(b)

    def analyze_resource_change(self, resource_idx, delta):
        """
        Analyzes how a change in resource b[idx] affects the optimal value.
        """
        b_new = self.b.copy()
        b_new[resource_idx] += delta
        
        res = linprog(-self.c, A_ub=self.A, b_ub=b_new, method='highs')
        return -res.fun if res.success else None

def main():
    print("--- ⚙️ Yöneylem Araştırması: Duyarlılık Analizi ---")
    
    # Max Z = 4x1 + 3x2
    # s.t. 2x1 + 1x2 <= 40
    #      1x1 + 2x2 <= 50
    c = [4, 3]
    A = [[2, 1], [1, 2]]
    b = [40, 50]
    
    analyzer = SensitivityAnalyzer(c, A, b)
    
    # Original Solution
    original_z = analyzer.analyze_resource_change(0, 0)
    print(f"🔹 Orijinal Maksimum Kar: {original_z:.2f}")
    
    print("\n📊 KAYNAK DEĞİŞİM ANALİZİ (Gölge Fiyat İncelemesi):")
    print("-" * 50)
    for i in range(len(b)):
        new_z = analyzer.analyze_resource_change(i, 1) # Increase resource by 1 unit
        shadow_price = new_z - original_z
        print(f"🔹 Kaynak {i+1} için Gölge Fiyatı: {shadow_price:.2f}")
    print("-" * 50)
    print("✅ Not: Gölge fiyat, ilgili kaynağın 1 birim artışının amaç fonksiyonundaki toplam artışıdır.")

if __name__ == "__main__":
    main()
