# ♟️ FAZ 8 — Oyun Teorisi & Çok Amaçlı Optimizasyon

[![Theory: Game Theory](https://img.shields.io/badge/Teori-Oyun%20Teorisi-darkblue?style=flat-square)](#)
[![Nash: 1950](https://img.shields.io/badge/Nash-1950-gold?style=flat-square)](#)
[![von Neumann: 1928](https://img.shields.io/badge/von%20Neumann-1928-silver?style=flat-square)](#)

> *"Life is like a game, but the rules are written by those who understand the math."*
> — **John von Neumann**

---

## 🧠 Temel Kavramlar

Oyun teorisi, **rasyonel oyuncuların** çıkarlarının çakıştığı veya zıtlaştığı durumlarda **stratejik karar verme** süreçlerini matematiksel olarak modelleyen disiplindir.

### Oyun Anatomisi

| Bileşen | Sembol | Tanım |
|---------|--------|-------|
| Oyuncu Kümesi | $N = \{1, 2, \ldots, n\}$ | Kararlar alan rasyonel aktörler |
| Strateji Uzayı | $S_i$ | Oyuncu $i$'nin tüm olası hamleleri |
| Kazanç Fonksiyonu | $u_i: S \to \mathbb{R}$ | Strateji profiline göre fayda |
| Strateji Profili | $s = (s_1, \ldots, s_n)$ | Oyuncuların birleşik stratejisi |

---

## ⚔️ Sıfır Toplamlı Oyunlar (Zero-Sum Games)

İki oyunculu, toplam kazancın sıfır olduğu oyunlar: **Oyuncu 1'in kazancı = Oyuncu 2'nin kaybı**

### Minimax Teoremi (von Neumann, 1928)

$$\max_{p \in \Delta(S_1)} \min_{q \in \Delta(S_2)} \mathbf{p}^T A \mathbf{q} = \min_{q \in \Delta(S_2)} \max_{p \in \Delta(S_1)} \mathbf{p}^T A \mathbf{q} = V^*$$

Burada:
- $A$ → Kazanç matrisi (Oyuncu 1 perspektifi)
- $p, q$ → Karma (mixed) strateji olasılık vektörleri
- $V^*$ → Oyunun değeri (Game Value)

### LP Formülasyonu

**Oyuncu 1 (Maximin):**
$$\max V \quad \text{s.t.} \quad A^T p \geq V \mathbf{1}, \quad \sum p_i = 1, \quad p \geq 0$$

**Oyuncu 2 (Minimax):**
$$\min V \quad \text{s.t.} \quad A q \leq V \mathbf{1}, \quad \sum q_j = 1, \quad q \geq 0$$

---

## 🤝 Nash Dengesi (Nash Equilibrium)

**Tanım:** Hiçbir oyuncunun tek taraflı saparak faydasını artıramadığı strateji profili.

$$u_i(s_i^*, s_{-i}^*) \geq u_i(s_i, s_{-i}^*) \quad \forall s_i \in S_i, \quad \forall i \in N$$

### Nash'ın Varlık Teoremi (1950)

> *Her sonlu oyunda en az bir (karma stratejide) Nash dengesi mevcuttur.*

---

## 📦 Modül İçeriği

| Dosya | Problem | Yöntem |
|-------|---------|--------|
| `zero_sum_game_solver.py` | Sıfır toplamlı 2-kişilik oyunlar | Minimax + LP |
| `nash_equilibrium_finder.py` | Genel karma strateji Nash dengesi | LP formülasyonu |

---

## 🎯 Klasik Oyunlar Kataloğu

### Mahkum İkilemi (Prisoner's Dilemma)

|  | **B: İşbirliği** | **B: İhanet** |
|--|----------|---------|
| **A: İşbirliği** | (3, 3) | (0, 5) |
| **A: İhanet** | (5, 0) | (1, 1) |

- Tek Nash Dengesi: (İhanet, İhanet) = (1,1) — **Pareto-suboptimal!**
- Pareto Optimal: (İşbirliği, İşbirliği) = (3,3)

### Tavuk Oyunu (Chicken/Hawk-Dove)

|  | **B: Geri Dön** | **B: Devam** |
|--|------------|----------|
| **A: Geri Dön** | (0, 0) | (-1, +1) |
| **A: Devam** | (+1, -1) | (-10, -10) |

- 2 saf strateji Nash dengesi + 1 karma Nash dengesi

---

## 🔧 Hızlı Kullanım

```bash
python zero_sum_game_solver.py      # Minimax + saf/karma çözüm
python nash_equilibrium_finder.py   # 2x2 Nash dengesi analizi
```

---

*FAZ 7 → Doğrusal Olmayan Programlama | Tüm Modüller → README.md*
