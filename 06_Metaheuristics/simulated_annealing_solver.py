"""
🧬 Yoneylem-Ders-Notlari: Metaheuristic Tool
Simulated Annealing (SA) General Solver
"""

import numpy as np
import math
import random

def objective_function(x):
    """
    Example Non-convex function: f(x) = x^2 + 10*sin(x)
    Goal: Find global minimum
    """
    return x**2 + 10 * math.sin(x)

class SimulatedAnnealing:
    def __init__(self, start_temp, cooling_rate, min_temp):
        self.temp = start_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp

    def solve(self, start_x):
        current_x = start_x
        current_val = objective_function(current_x)
        
        best_x = current_x
        best_val = current_val

        while self.temp > self.min_temp:
            # 1. New Candidate (+/- 1.0 range)
            next_x = current_x + random.uniform(-1, 1)
            next_val = objective_function(next_x)

            # 2. Acceptance probability
            delta = next_val - current_val
            
            # If better, always accept. If worse, accept with probability p
            if delta < 0 or random.random() < math.exp(-delta / self.temp):
                current_x = next_x
                current_val = next_val
                
                # Update absolute best
                if current_val < best_val:
                    best_x = current_x
                    best_val = current_val

            # 3. Cooling
            self.temp *= self.cooling_rate

        return best_x, best_val

def main():
    print("--- ⚙️ Yöneylem Araştırması: Simüle Edilmiş Tavlama (Simulated Annealing) ---")
    
    sa = SimulatedAnnealing(start_temp=100, cooling_rate=0.99, min_temp=0.01)
    x_opt, val_opt = sa.solve(start_x=10.0) # Start from a poor point
    
    print(f"\n✅ Tavlama Süreci Tamamlandı:")
    print(f"🔹 Bulunan Optimum Nokta (x): {x_opt:.4f}")
    print(f"🔹 Minimum Fonksiyon Değeri f(x): {val_opt:.4f}")
    print("-" * 50)
    print("🧬 Not: SA, geçici olarak kötü çözümleri kabul ederek yerel minimumlardan kaçar.")

if __name__ == "__main__":
    main()
