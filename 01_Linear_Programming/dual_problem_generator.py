"""
⚙️ Yoneylem-Ders-Notlari: Linear Programming Tool
Dual Problem Generator and Solver
"""

from scipy.optimize import linprog
import numpy as np

class DualGenerator:
    def __init__(self, c, A, b, sense='max'):
        """
        Primal Problem:
        sense Z = c^T * x
        subject to: A * x <= b
        """
        self.c = np.array(c)
        self.A = np.array(A)
        self.b = np.array(b)
        self.sense = sense

    def solve_primal(self):
        # linprog minimizes by default
        coeffs = -self.c if self.sense == 'max' else self.c
        res = linprog(coeffs, A_ub=self.A, b_ub=self.b, method='highs')
        return res

    def get_dual_params(self):
        """
        Dual Problem:
        min (or max) W = b^T * y
        subject to: A^T * y >= c
        """
        dual_c = self.b
        dual_A = -self.A.T # converting >= to <= for linprog
        dual_b = -self.c
        dual_sense = 'min' if self.sense == 'max' else 'max'
        return dual_c, dual_A, dual_b, dual_sense

    def solve_dual(self):
        dc, dA, db, ds = self.get_dual_params()
        coeffs = dc if ds == 'min' else -dc
        res = linprog(coeffs, A_ub=dA, b_ub=db, method='highs')
        return res

def main():
    print("--- ⚙️ Yöneylem Araştırması: Primal-Dual Analizi ---")
    
    # Primal: Max Z = 3x1 + 5x2
    # s.t. 1x1 + 0x2 <= 4
    #      0x1 + 2x2 <= 12
    #      3x1 + 2x2 <= 18
    c = [3, 5]
    A = [[1, 0], [0, 2], [3, 2]]
    b = [4, 12, 18]
    
    generator = DualGenerator(c, A, b, sense='max')
    
    primal_res = generator.solve_primal()
    dual_res = generator.solve_dual()
    
    print("\n📦 PRIMAL SONUÇLARI:")
    print(f"🔹 Durum: {primal_res.message}")
    print(f"🔹 Optimal Değer Z: {-primal_res.fun:.2f}")
    print(f"🔹 Karar Değişkenleri x: {primal_res.x}")
    
    print("\n📦 DUAL SONUÇLARI:")
    print(f"🔹 Durum: {dual_res.message}")
    print(f"🔹 Optimal Değer W: {dual_res.fun:.2f}")
    print(f"🔹 Dual Değişkenler (Gölge Fiyatlar) y: {dual_res.x}")
    
    print("\n✅ Güçlü Dualite Kontrolü: Z == W" if abs(-primal_res.fun - dual_res.fun) < 1e-6 else "❌ Hata!")

if __name__ == "__main__":
    main()
