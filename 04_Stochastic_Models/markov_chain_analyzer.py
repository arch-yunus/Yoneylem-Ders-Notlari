"""
Markov Zinciri Analizörü — Geçiş Matrisi & Kararlı Durum
---------------------------------------------------------
Bu modül, Markov zincirleri için geçiş matrisini analiz eder,
kararlı durum (steady-state) olasılıklarını hesaplar ve
n-adım geçiş olasılıklarını simüle eder.
Kütüphane: NumPy, Pandas
"""

import numpy as np
import pandas as pd


class MarkovChainAnalyzer:
    def __init__(self, transition_matrix: np.ndarray, state_names: list = None):
        """
        Parametreler:
            transition_matrix: Satır toplamı 1 olan kare matris (P)
            state_names: Durum isimleri listesi (opsiyonel)
        """
        self.P = np.array(transition_matrix, dtype=float)
        n = self.P.shape[0]
        self.n = n
        self.states = state_names if state_names else [f"S{i}" for i in range(n)]

        # Doğrulama
        if not np.allclose(self.P.sum(axis=1), 1.0):
            raise ValueError("Her satırın toplamı 1 olmalıdır!")

    def display_matrix(self):
        """Geçiş matrisini pandas DataFrame olarak gösterir."""
        df = pd.DataFrame(self.P, index=self.states, columns=self.states)
        print("Geçiş Matrisi P:")
        print(df.to_string(float_format='{:.4f}'.format))
        return df

    def n_step_matrix(self, n: int) -> np.ndarray:
        """n-adım geçiş matrisini hesaplar: P^n"""
        Pn = np.linalg.matrix_power(self.P, n)
        df = pd.DataFrame(Pn, index=self.states, columns=self.states)
        print(f"\n{n}-Adım Geçiş Matrisi (P^{n}):")
        print(df.to_string(float_format='{:.4f}'.format))
        return Pn

    def steady_state(self) -> np.ndarray:
        """Kararlı durum olasılıklarını hesaplar (π = πP)."""
        # Özvektör yöntemi
        vals, vecs = np.linalg.eig(self.P.T)
        # Özdeğeri 1 olan özvektörü bul
        idx = np.argmin(np.abs(vals - 1.0))
        pi = vecs[:, idx].real
        pi = np.abs(pi) / np.abs(pi).sum()

        print("\nKararlı Durum Olasılıkları (π):")
        for state, prob in zip(self.states, pi):
            print(f"  π({state}) = {prob:.6f}  ({prob*100:.2f}%)")
        return pi

    def simulate(self, initial_state: int, n_steps: int) -> list:
        """Monte Carlo ile zincir simülasyonu."""
        np.random.seed(42)
        trajectory = [self.states[initial_state]]
        current = initial_state

        for _ in range(n_steps):
            current = np.random.choice(self.n, p=self.P[current])
            trajectory.append(self.states[current])

        return trajectory

    def expected_return_time(self) -> dict:
        """Her durumun beklenen dönüş süresi = 1 / π_i"""
        pi = self.steady_state()
        print("\nBeklenen Dönüş Süreleri (μ_i = 1/π_i):")
        result = {}
        for state, prob in zip(self.states, pi):
            mu = 1.0 / prob if prob > 0 else float('inf')
            result[state] = mu
            print(f"  μ({state}) = {mu:.4f} adım")
        return result


if __name__ == "__main__":
    # Örnek: Hava durumu Markov zinciri
    P = [
        [0.70, 0.20, 0.10],  # Güneşli
        [0.30, 0.40, 0.30],  # Bulutlu
        [0.20, 0.30, 0.50]   # Yağmurlu
    ]
    states = ["Güneşli", "Bulutlu", "Yağmurlu"]

    print("=" * 55)
    print("MARKOV ZİNCİRİ ANALİZÖRÜ")
    print("Uygulama: Hava Durumu Tahmini")
    print("=" * 55)

    mc = MarkovChainAnalyzer(P, states)
    mc.display_matrix()
    mc.n_step_matrix(5)
    mc.steady_state()
    mc.expected_return_time()

    # 20 adımlık simülasyon
    print("\n20 Adımlık Simülasyon (Başlangıç: Güneşli):")
    trajectory = mc.simulate(0, 20)
    print(" → ".join(trajectory))
