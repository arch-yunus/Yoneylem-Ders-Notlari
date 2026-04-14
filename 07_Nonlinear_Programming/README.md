# Modül 7: Doğrusal Olmayan Programlama (Nonlinear Programming - NLP) 📈

Doğrusal olmayan programlama, amaç fonksiyonunun veya kısıtların (veya her ikisinin) doğrusal olmadığı optimizasyon problemlerini inceler. Gerçek dünyadaki fiziksel yasalar ve ekonomik modeller genellikle süreksiz veya eğriseldir.

## 📝 Teorik Temeller

### 1. Konveksite (Convexity)
Bir kümenin veya fonksiyonun dışbükey olması, yerel bir optimumun aynı zamanda küresel (global) optimum olduğunu garantiler. NLP'de konveksite analizi en kritik adımdır.

### 2. Kısıtsız Optimizasyon
Herhangi bir sınır olmaksızın fonksiyonun ekstremum noktalarını bulma işlemidir.
- **Gradyan İnişi (Gradient Descent):** Fonksiyonun eğiminin en dik olduğu yönün tersine giderek minimumu arar.
- **Newton-Raphson Metodu:** İkinci türev (Hessian matrisi) bilgisini kullanarak daha hızlı yakınsar.

### 3. Kısıtlı Optimizasyon
- **Lagrange Çarpanları:** Eşitlik kısıtları altındaki problemleri çözmek için kullanılır.
- **KKT (Karush-Kuhn-Tucker) Şartları:** Eşitsizlik kısıtları altındaki doğrusal olmayan problemler için optimallik şartlarını belirler.

## 🛠️ Dahili Araçlar

### [gradient_descent_optimizer.py](gradient_descent_optimizer.py)
Bir fonksiyonun minimum noktasına gradyan adımlarıyla nasıl ulaşıldığını simüle eden ve görselleştirme yeteneğine sahip bir temel NLP aracıdır.

## 📚 Kaynakça
- *Bazaraa, M. S., Sherali, H. D., & Shetty, C. M.:* Nonlinear Programming: Theory and Algorithms.
- *Bertsekas, D. P.:* Nonlinear Programming.
- *Nocedal, J. & Wright, S.:* Numerical Optimization.
