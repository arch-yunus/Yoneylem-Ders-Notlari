"""
🎲 Yoneylem-Ders-Notlari: Stochastic Tool
Monte Carlo Simulation for Numerical Integration
"""

import numpy as np
import random

class MonteCarloIntegrator:
    def __init__(self, function, a, b, n_samples=100000):
        """
        Integrates function from a to b using Monte Carlo
        """
        self.func = function
        self.a = a
        self.b = b
        self.n = n_samples

    def integrate(self):
        # Generate random samples within [a, b]
        samples = np.random.uniform(self.a, self.b, self.n)
        
        # Calculate function values
        y_values = self.func(samples)
        
        # Area = (b-a) * average function value
        integral_estimate = (self.b - self.a) * np.mean(y_values)
        return integral_estimate

def example_func(x):
    """f(x) = sin(x) * e^(-x)"""
    return np.sin(x) * np.exp(-x)

def main():
    print("--- ⚙️ Yöneylem Araştırması: Monte Carlo Sayısal İntegral ---")
    
    a, b = 0, np.pi
    integrator = MonteCarloIntegrator(example_func, a, b, n_samples=500000)
    
    estimate = integrator.integrate()
    
    print(f"\n✅ Simülasyon Tamamlandı:")
    print(f"🔹 Aralık: [{a:.2f}, {b:.2f}]")
    print(f"🔹 Örneklem Sayısı: {integrator.n}")
    print(f"🔹 Tahmini İntegral Değeri: {estimate:.6f}")
    print("-" * 50)
    print("🎲 Not: Örneklem sayısı arttıkça tahminin hatası O(1/√n) oranında azalır.")

if __name__ == "__main__":
    main()
