# 🧩 FAZ 5 — Dinamik Programlama (Dynamic Programming)

[![Paradigm: DP](https://img.shields.io/badge/Paradigma-Dinamik%20Programlama-6A0DAD?style=flat-square)](#)
[![Complexity: Polynomial](https://img.shields.io/badge/Karmaşıklık-Polinom-blue?style=flat-square)](#)
[![Bellman: 1953](https://img.shields.io/badge/Bellman-1953-gold?style=flat-square)](#)

> *"An optimal policy has the property that whatever the initial state and initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision."*
> — **Richard Bellman**, 1953

---

## 🧠 Temel Prensip: Bellman'ın Optimallik İlkesi

Dinamik Programlama (DP), **çok evreli karar problemlerini** örtüşen alt problemlere bölen ve her alt problemin çözümünü yeniden kullanarak büyük problemleri verimli biçimde çözen bir **optimizasyon paradigmasıdır**.

### İki Temel Özellik

| Özellik | Açıklama |
|---------|----------|
| **Optimal Alt Yapı** | Problemin optimal çözümü, alt problemlerin optimal çözümlerini içerir |
| **Örtüşen Alt Problemler** | Aynı alt problem birden fazla kez ortaya çıkar (memoize et!) |

### Bellman Denkliği (Genel Form)

$$V^*(s) = \max_{a \in \mathcal{A}(s)} \left[ c(s, a) + V^*(T(s, a)) \right]$$

Burada:
- $s$ → Mevcut durum (state)
- $a$ → Alınan karar/aksiyon
- $c(s,a)$ → Anlık katkı (ödül)
- $T(s,a)$ → Geçiş fonksiyonu (sonraki durum)

---

## 🔄 Bottom-Up (Tabulation) vs. Top-Down (Memoization)

```
TOP-DOWN (Memoization)          BOTTOM-UP (Tabulation)
─────────────────────           ─────────────────────
+ Doğal, rekürsif               + Bellek verimli
+ Sadece gerekli adımlar        + Yığın overflow yok
- Rekürsif yığın maliyeti       - Tüm alt problemler hesaplanır
- Yığın taşması riski           + Genellikle daha hızlı pratikte
```

---

## 📦 Modül İçeriği

| Dosya | Problem | Yöntem |
|-------|---------|--------|
| `knapsack_dp.py` | 0-1 Sırt Çantası | Tabulation + Backtracking |
| `inventory_dp.py` | Dinamik Stok Yönetimi | Forward/Backward DP |
| `shortest_path_dp.py` | En Kısa Yol (DP) | Bellman-Ford DP yaklaşımı |

---

## 🎯 Klasik DP Problemleri ve Karmaşıklıkları

| Problem | Alt Problem Boyutu | Zaman | Uzay |
|---------|-------------------|-------|------|
| 0-1 Knapsack | $n \times W$ | $O(nW)$ | $O(nW)$ → $O(W)$ |
| Fibonacci | $n$ | $O(n)$ | $O(1)$ |
| LCS (En Uzun Ortak Dizi) | $m \times n$ | $O(mn)$ | $O(mn)$ |
| Edit Distance | $m \times n$ | $O(mn)$ | $O(mn)$ |
| Matris Zinciri Çarpımı | $n^2$ | $O(n^3)$ | $O(n^2)$ |
| Optimal BST | $n^2$ | $O(n^3)$ | $O(n^2)$ |
| Floyd-Warshall | $V^2$ | $O(V^3)$ | $O(V^2)$ |
| Stok Yönetimi (T dönem) | $T \times S$ | $O(T \cdot S^2)$ | $O(T \cdot S)$ |

---

## 🏭 Endüstriyel Uygulama: Üretim Planlaması

**Problem:** $T$ dönemde talep $d_t$ karşılanacak; üretim maliyeti $c_t$, stok tutma maliyeti $h$ ve stok kapasitesi $S_{max}$.

$$V_t(s) = \min_{x \geq 0} \left[ c_t \cdot x + h \cdot (s + x - d_t) + V_{t+1}(s + x - d_t) \right]$$

```bash
python knapsack_dp.py       # Sırt çantası (tabulation + izleme)
python inventory_dp.py      # Wagner-Whitin stok planlama
python shortest_path_dp.py  # Bellman-Ford DP formu
```

---

*FAZ 4 → Stokastik Modeller | FAZ 6 → Metasezgiseller*
