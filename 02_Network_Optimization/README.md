# Modül 2: Ağ (Network) Optimizasyonu 🕸️

Ağ modelleri, düğümler (nodes) ve yaylar (arcs) arasındaki fiziksel veya mantıksal ilişkileri optimize etmek için kullanılır. Lojistik, telekomünikasyon ve proje yönetimi alanlarında vazgeçilmezdir.

## 📝 Teorik Temeller

### 1. En Kısa Yol Problemi (Shortest Path)
Bir ağ üzerindeki başlangıç düğümünden hedef düğüme, toplam maliyeti veya süreyi minimize eden yolun bulunmasıdır.
- **Dijkstra Algoritması:** Negatif kenar ağırlığı olmayan ağlar için standart çözümdür.
- **Floyd-Warshall:** Tüm düğüm çiftleri arasındaki en kısa yolları bulur.

### 2. Maksimum Akış Problemi (Maximum Flow)
Bir kaynaktan (source) bir hedefe (sink), yayların kapasite kısıtları altında gönderilebilecek maksimum akış miktarını belirler.
- **Ford-Fulkerson Metodu:** Artık ağ (residual network) üzerinden geliştirme yolları (augmenting paths) arar.

### 3. Taşıma ve Atama Modelleri
Özel bir ağ yapısına sahip olan bu modeller, arz ve talebi en düşük maliyetle eşleştirmeyi hedefler.

## 🛠️ Dahili Araçlar

### [shortest_path_explorer.py](graph_algorithms/shortest_path_explorer.py)
Dijkstra algoritmasını kullanarak karmaşık ağ rotalamalarını çözer.

### [max_flow_solver.py](graph_algorithms/max_flow_solver.py)
Ağ kapasite analizlerini yapan ve darboğazları belirleyen bir araçtır.

## 📚 Kaynakça
- *Ahuja, R. K., Magnanti, T. L., & Orlin, J. B.:* Network Flows: Theory, Algorithms, and Applications.
- *Bazaraa, M. S., Jarvis, J. J., & Sherali, H. D.:* Linear Programming and Network Flows.
