# Modül 6: Meta-Sezgisel Algoritmalar (Metaheuristics) 🧬

Meta-sezgiseller, karmaşık (NP-Zor) problemlerin "yeterince iyi" çözümlerini makul sürede bulmak için tasarlanmış üst düzey algoritmalardır. Kesin algoritmaların (Ör: Simpleks) çözemediği devasa arama uzaylarında etkilidirler.

## 📝 Teorik Temeller

### 1. Sezgisel vs Meta-Sezgisel
- **Sezgisel (Heuristic):** Belirli bir probleme özel geliştirilmiş çözüm yöntemi (Ör: Ulaştırma için Vogel metodu).
- **Meta-Sezgisel:** Birçok farklı probleme uygulanabilen genel algoritma çerçeveleri.

### 2. Keşif (Exploration) vs Faydalanma (Exploitation)
- **Keşif (Çeşitlendirme):** Arama uzayının yeni ve bilinmeyen bölgelerini tarama yeteneği.
- **Faydalanma (Yoğunlaşma):** Mevcut iyi bir çözümün etrafındaki daha iyi çözümleri bulma yeteneği.
- *İyi bir meta-sezgisel bu iki özellik arasında denge kurmalıdır.*

### 3. Popüler Algoritmalar
- **Genetik Algoritmalar (Genetic Algorithms):** Evrimsel süreçleri (çaprazlama, mutasyon) taklit eder.
- **Simüle Edilmiş Tavlama (Simulated Annealing):** Metalürjik tavlama sürecini taklit eder.
- **Tabu Arama (Tabu Search):** Hafıza mekanizması kullanarak yerel optimumlardan kaçar.
- **Karınca Kolonisi (Ant Colony):** Karıncaların feromon izi bırakma davranışını taklit eder.

## 🛠️ Dahili Araçlar

### [genetic_algorithm_tsp.py](genetic_algorithm_tsp.py)
Gezgin Satıcı Problemini (TSP) popülasyon bazlı evrimsel bir yaklaşımla çözen profesyonel bir araçtır.

### [simulated_annealing_solver.py](simulated_annealing_solver.py)
Fiziksel tavlama prensibiyle, yerel optimum çukurlarından kurtulup küresel optimumu arayan bir algoritmadır.

## 📚 Kaynakça
- *Glover, F. & Kochenberger, G. A.:* Handbook of Metaheuristics.
- *Talbi, E. G.:* Metaheuristics: From Design to Implementation.
- *Karaboğa, D.:* Yapay Zeka Optimizasyon Algoritmaları.
