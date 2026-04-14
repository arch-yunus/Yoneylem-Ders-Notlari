# Çizge (Ağ) Algoritmaları 🕸️

Ağ modelleri, düğümler (vnodes) ve yaylardan (arcs) oluşan yapılar üzerindeki optimizasyon problemlerini çözer.

## 1. En Kısa Yol Problemi (Shortest Path Problem)
Bir başlangıç noktasından bir varış noktasına kadar olan yolun toplam ağırlığının (mesafe, zaman, maliyet) minimize edilmesidir.

### Dijkstra Algoritması:
Kenarların ağırlıklarının negatif olmadığı durumlarda kullanılır. Açgözlü (greedy) bir yaklaşımla her adımda en yakın komşu düğümü seçer.

---

## 2. Maksimum Akış Problemi (Maximum Flow Problem)
Bir ağın kaynağından (source) lavabosuna (sink) kadar gönderilebilecek maksimum madde, veri veya trafik miktarını belirler.

### Ford-Fulkerson Algoritması:
Sürekli olarak "artık ağ" (residual network) üzerinde artırılabilir yollar (augmenting paths) bularak akışı artırır.

---

## 3. Minimum Yayılan Ağaç (Minimum Spanning Tree - MST)
Tüm düğümleri birbirine bağlayan ve toplam kenar ağırlığı en küçük olan ağacı bulur (döngü içermez).

### Prim ve Kruskal Algoritmaları:
- **Prim:** Bir düğümden başlayarak en ucuz kenarı ağaca ekler.
- **Kruskal:** Tüm kenarları sıralar ve döngü oluşturmayacak şekilde en küçükleri seçerek birleştirir.
