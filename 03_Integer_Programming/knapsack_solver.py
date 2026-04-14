"""
🔢 Yoneylem-Ders-Notlari: Integer Programming Tool
0-1 Knapsack Problem Solver (Dynamic Programming & ILP)
"""

from pulp import *

class KnapsackSolver:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(values)

    def solve_ilp(self):
        """
        Solve using Integer Linear Programming (PuLP)
        """
        prob = LpProblem("Knapsack_Problem", LpMaximize)
        
        # Decision variables x[i] = 1 if item i is selected, 0 otherwise
        item_vars = [LpVariable(f"Item_{i}", 0, 1, LpBinary) for i in range(self.n)]
        
        # Objective: Maximize total value
        prob += lpSum([self.values[i] * item_vars[i] for i in range(self.n)])
        
        # Constraint: Total weight <= capacity
        prob += lpSum([self.weights[i] * item_vars[i] for i in range(self.n)]) <= self.capacity
        
        prob.solve(PULP_CBC_CMD(msg=0))
        
        selected_items = [i for i in range(self.n) if value(item_vars[i]) == 1]
        return value(prob.objective), selected_items

def main():
    print("--- ⚙️ Yöneylem Araştırması: 0-1 Sırt Çantası (Knapsack) ---")
    
    values = [60, 100, 120]
    weights = [10, 20, 30]
    cap = 50
    
    solver = KnapsackSolver(weights, values, cap)
    opt_val, selected = solver.solve_ilp()
    
    print(f"\n✅ Optimizasyon Tamamlandı:")
    print(f"🔹 Toplam Maksimum Değer: {opt_val}")
    print(f"🔹 Seçilen Eşyalar (Index): {selected}")
    print(f"🔹 Toplam Ağırlık: {sum(weights[i] for i in selected)} / {cap}")

if __name__ == "__main__":
    main()
