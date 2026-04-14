"""
📈 Yoneylem-Ders-Notlari: Nonlinear Tool
Gradient Descent Optimizer for Unconstrained Functions
"""

import numpy as np

def f(x):
    """Objective function: f(x1, x2) = x1^2 + x2^2 + 5"""
    return x[0]**2 + x[1]**2 + 5

def gradient_f(x):
    """Gradient of f: df/dx1 = 2*x1, df/dx2 = 2*x2"""
    return np.array([2*x[0], 2*x[1]])

class GradientDescent:
    def __init__(self, learning_rate=0.1, max_iter=100, tol=1e-6):
        self.lr = learning_rate
        self.max_iter = max_iter
        self.tol = tol

    def optimize(self, start_x):
        x = np.array(start_x, dtype=float)
        history = [x.copy()]
        
        for i in range(self.max_iter):
            grad = gradient_f(x)
            
            # Update step: x_new = x - learning_rate * gradient
            new_x = x - self.lr * grad
            
            # Check convergence
            if np.linalg.norm(new_x - x) < self.tol:
                x = new_x
                history.append(x.copy())
                break
                
            x = new_x
            history.append(x.copy())
            
        return x, len(history), history

def main():
    print("--- ⚙️ Yöneylem Araştırması: Gradyan İnişi (Gradient Descent) ---")
    
    start_point = [4, 4]
    gd = GradientDescent(learning_rate=0.1)
    
    best_x, iters, history = gd.optimize(start_point)
    
    print(f"\n✅ Optimizasyon Tamamlandı:")
    print(f"🔹 Başlangıç Noktası: {start_point}")
    print(f"🔹 Bulunan Minimum Nokta: {best_x}")
    print(f"🔹 Minimum Fonksiyon Değeri f(x,y): {f(best_x):.4f}")
    print(f"🔹 İterasyon Sayısı: {iters}")
    print("-" * 50)
    print("📈 Not: Gradyan her zaman en dik artış yönünü gösterir, terse gitmek minimuma ulaştırır.")

if __name__ == "__main__":
    main()
