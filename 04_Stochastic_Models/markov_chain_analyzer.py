"""
🎲 Yoneylem-Ders-Notlari: Stochastic Tool
Markov Chain Steady-State Analyzer
"""

import numpy as np

class MarkovAnalyzer:
    def __init__(self, transition_matrix):
        """
        matrix: n x n transition probability matrix (sums to 1 row-wise)
        """
        self.P = np.array(transition_matrix)
        self.n = self.P.shape[0]

    def calculate_steady_state(self):
        """
        Solve pi * P = pi  subject to sum(pi) = 1
        Alternatively: pi * (P - I) = 0
        """
        # (P^T - I) * pi^T = 0
        A = self.P.T - np.eye(self.n)
        
        # Replace the last row with the normalization constraint sum(pi) = 1
        A[-1] = np.ones(self.n)
        B = np.zeros(self.n)
        B[-1] = 1
        
        try:
            pi = np.linalg.solve(A, B)
            return pi
        except np.linalg.LinAlgError:
            return None

def main():
    print("--- ⚙️ Yöneylem Araştırması: Markov Zinciri Dengesi ---")
    
    # 3-State Example: Market Share for Brand A, B, C
    # Row 1: Brand A loyalty
    # Row 2: Brand B loyalty
    # Row 3: Brand C loyalty
    matrix = [
        [0.8, 0.1, 0.1],
        [0.2, 0.7, 0.1],
        [0.1, 0.3, 0.6]
    ]
    
    analyzer = MarkovAnalyzer(matrix)
    pi = analyzer.calculate_steady_state()
    
    if pi is not None:
        print("\n📊 KARARLI DURUM OLASILIKLARI (Steady-State):")
        print("-" * 50)
        states = ["Durum A", "Durum B", "Durum C"]
        for i, prob in enumerate(pi):
            print(f"🔹 {states[i]}: %{prob*100:.2f}")
        print("-" * 50)
        print("✅ Not: Bu değerler sistemin uzun vadedeki beklenen pazar paylarını temsil eder.")
    else:
        print("🛑 Hata: Matris çözülemedi.")

if __name__ == "__main__":
    main()
