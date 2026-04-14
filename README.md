# ⚙️ Yöneylem Araştırması — Karar Mühendisliğinin Zirve Arşivi

<div align="center">

[![Discipline: Operations Research](https://img.shields.io/badge/Disiplin-Yöneylem%20Araştırması-0A0A2E?style=for-the-badge&logo=mathworks&logoColor=white)](https://en.wikipedia.org/wiki/Operations_research)
[![Field: Industrial Engineering](https://img.shields.io/badge/Alan-Endüstri%20Mühendisliği-1A1A4E?style=for-the-badge&logo=engineering&logoColor=cyan)](https://en.wikipedia.org/wiki/Industrial_engineering)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge)](LICENSE)
[![Modules: 8](https://img.shields.io/badge/Modül-8%20Faz-purple?style=for-the-badge)](#)
[![Status: Active](https://img.shields.io/badge/Durum-Aktif%20Geliştirme-brightgreen?style=for-the-badge)](#)

```
██╗   ██╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗     ███████╗███╗   ███╗
╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██║     ██╔════╝████╗ ████║
 ╚████╔╝ ██║   ██║██╔██╗ ██║█████╗   ╚████╔╝ ██║     █████╗  ██╔████╔██║
  ╚██╔╝  ██║   ██║██║╚██╗██║██╔══╝    ╚██╔╝  ██║     ██╔══╝  ██║╚██╔╝██║
   ██║   ╚██████╔╝██║ ╚████║███████╗   ██║   ███████╗███████╗██║ ╚═╝ ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝
  ─────────── ARAŞTIRMASI · OPTIMIZASYON · KARAR MATEMATİĞİ ───────────
```

> *"Optimizasyon, sadece en iyiyi bulmak değil; karmaşanın içindeki gizli düzeni matematiksel bir zarafetle ortaya çıkarmaktır."*

**8 Faz · 50+ Algoritma · Production-Ready Python Kodu · LaTeX Destekli Teori**

</div>

---

## 📜 Doktrin Manifestosu

Bu depo, **Yöneylem Araştırması (Operations Research — OR)** disiplininin teorik temellerini, matematiksel ispatlarını ve modern yazılım araçlarıyla **endüstriyel karar sistemleri** inşa etmeyi hedefleyen açık kaynaklı bir külliyattır.

Burada inşa edilen bilgi mimarisi üç temel eksen üzerine kuruludur:

| Eksen | Tanım | Araç |
|-------|-------|------|
| 🧠 **Teori** | İspat seviyesi matematiksel temeller | LaTeX, Markdown |
| ⚙️ **Algoritma** | Adım adım çalışan, yorumlanabilir kod | Python, NumPy |
| 🏭 **Endüstri** | Gerçek sektör uygulamaları ve vaka analizi | PuLP, Pyomo, SimPy |

---

## 🕰️ Tarihsel Kökenler — Savaştan Doğan Bilim

Yöneylem Araştırması, fildişi kulelerdeki teorik bir uğraş değil; savaşların, krizlerin ve endüstriyel darboğazların ortasında doğmuş bir **kriz çözme bilimidir.**

```
1909  ─▶  A.K. Erlang    ── Kuyruk Teorisi (telefon santralleri)
1916  ─▶  F.W. Lanchester ── Askeri çatışma diferansiyel denklemleri
1939  ─▶  Kantorovich     ── Doğrusal Programlama (nakliye optimizasyonu)
1941  ─▶  P. Blackett     ── "Blackett's Circus" — denizaltı savaşı OR modelleri
1947  ─▶  G. Dantzig      ── Simpleks Algoritması (ABD Hava Kuvvetleri)
1950  ─▶  J. Nash         ── Nash Dengesi, Oyun Teorisi
1953  ─▶  R. Bellman      ── Dinamik Programlama — Optimallik Prensibi
1957  ─▶  Ford & Fulkerson ── Maksimum Akış Algoritması
1975  ─▶  Khachian        ── Elipsoid Algoritması (Polinom LP)
1984  ─▶  Karmarkar       ── İç Nokta Yöntemi (Interior Point)
2000+ ─▶  AI/ML Füzyonu   ── Reinforcement Learning + OR hibrid sistemler
```

---

## 📐 Matematiksel Temel — Kanonik Formlar

### Genel LP (Standart Matris Formu)

$$\max \quad Z = \mathbf{c}^T \mathbf{x}$$
$$\text{s.t.} \quad \mathbf{A}\mathbf{x} \leq \mathbf{b}, \quad \mathbf{x} \geq \mathbf{0}$$

### Integer Programming (MILP)

$$\min \quad \mathbf{c}^T \mathbf{x} + \mathbf{d}^T \mathbf{y}$$
$$\text{s.t.} \quad \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{y} \leq \mathbf{b}, \quad \mathbf{x} \in \mathbb{R}^n_+, \quad \mathbf{y} \in \{0,1\}^m$$

### Genel NLP (KKT Şartları)

$$\min f(\mathbf{x}) \quad \text{s.t.} \quad g_i(\mathbf{x}) \leq 0, \quad h_j(\mathbf{x}) = 0$$
$$\nabla f(\mathbf{x}^*) + \sum_i \lambda_i \nabla g_i(\mathbf{x}^*) + \sum_j \mu_j \nabla h_j(\mathbf{x}^*) = 0$$

### Bellman Optimallik Denklemi (DP)

$$V^*(s) = \max_{a \in \mathcal{A}} \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) \cdot V^*(s') \right]$$

### M/M/c Kuyruk Sistemi (Steady-State)

$$L_q = \frac{P_0 (\lambda/\mu)^c \rho}{c!(1-\rho)^2}, \qquad W = L/\lambda \quad \text{(Little's Law)}$$

---

## 📚 Modül Mimarisi — 8 Faz Doktrini

### ━━━ FAZ 1 · Doğrusal Programlama (LP) ━━━━━━━━━━━━━━━━━━━━━━━

Kesin bilinen parametreler altında sürekli karar sistemleri.

| Konu | İçerik | Dosya |
|------|--------|-------|
| 1.1 Model Kurma | Karar uzayı, kısıtlar, amaç fonksiyonu | `theory_notes.md` |
| 1.2 Grafiksel Çözüm | 2D/3D feasible region, köşe noktası | `simplex_algorithm_step_by_step.ipynb` |
| 1.3 Simpleks | Pivot işlemi, tablo iterasyonları, Big-M | `simplex_algorithm_step_by_step.ipynb` |
| 1.4 Dualite | Primal-Dual dönüşüm, Güçlü Dualite Teoremi | `dual_problem_generator.py` |
| 1.5 Duyarlılık | Gölge Fiyatı, parametre aralıkları | `sensitivity_analysis.ipynb` |

**Temel Kavramlar:**
- Dışbükey (Convex) Küme ve Köşe Noktası Teoremi
- Dejenere Çözümler ve Anti-Cycling kuralları (Bland's Rule)
- Büyük-M (Big-M) ve İki Aşamalı (Two-Phase) Yöntemler
- Tamamlayıcı Gevşeklik (Complementary Slackness) Teoremi

---

### ━━━ FAZ 2 · Ağ Optimizasyonu (Network Models) ━━━━━━━━━━━━━━━━

Özel yapılı seyrek matrisler için hızlandırılmış optimizasyon algoritmaları.

| Algoritma | Karmaşıklık | Uygulama |
|-----------|------------|----------|
| Kuzey-Batı Köşesi | O(m+n) | Başlangıç çözümü |
| Vogel Yaklaşımı | O(m·n) | Daha iyi başlangıç |
| Ulaştırma Simpleksi | O(m·n·(m+n)) | Optimal ulaştırma |
| Macar Algoritması | O(n³) | Atama problemi |
| Dijkstra | O((V+E)log V) | En kısa yol |
| Bellman-Ford | O(V·E) | Negatif kenar |
| Floyd-Warshall | O(V³) | Tüm çiftler |
| Kruskal/Prim | O(E log E) | Minimum Yayılan Ağaç |
| Ford-Fulkerson | O(E · max_flow) | Maksimum Akış |
| CPM/PERT | O(V+E) | Kritik Yol Analizi |

---

### ━━━ FAZ 3 · Tamsayılı & Karma Programlama (MILP) ━━━━━━━━━━━━━

NP-Hard problemler için tam ve yaklaşık çözüm metodolojileri.

| Konu | Yöntem |
|------|--------|
| Dal ve Sınır | Ağaç araması, sınır hesabı, budama |
| Gomory Kesmeleri | LP relaxation + kesme düzlemleri |
| Benders Ayrışımı | Master + alt problem dekomposizyonu |
| Teslimat Yer Seçimi | Facility Location (p-medyan) modeli |
| Seyahat Satıcı (TSP) | ILP formülasyonu + heuristik |
| Çanta Problemi | 0-1 knapsack, bounded, unbounded |

---

### ━━━ FAZ 4 · Stokastik Modeller ve Rastlantısallık ━━━━━━━━━━━━━━

Belirsizlik, olasılık ve zamanın sisteme dahil edilmesi.

**Markov Zincirleri:**
- Homojen / Homojen Olmayan Zincirler
- Durum geçiş matrisi $\mathbf{P}$, ergodiklik şartları
- Kararlı Durum Analizi: $\boldsymbol{\pi} = \boldsymbol{\pi}\mathbf{P}$
- Emici Markov Zincirleri ve beklenen emilim süreleri

**Kuyruk Sistemleri (Kendall: A/B/c/K/N/D):**

| Model | $L_q$ Formülü | Uygulama |
|-------|--------------|----------|
| M/M/1 | $\rho^2/(1-\rho)$ | Tek gişeli banka |
| M/M/c | Erlang-C | Çağrı merkezi |
| M/D/1 | $\rho^2/(2(1-\rho))$ | Sabit servis ATM |
| M/G/1 | Pollaczek-Khinchine | Genel dağılım |
| M/M/1/K | Sonlu kapasite | Üretim tamponu |

---

### ━━━ FAZ 5 · Dinamik Programlama ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bellman'ın Optimallik Prensibi ile çok evreli karar problemleri.

**Temel Kavramlar:**
- Örtüşen Alt Problemler (Overlapping Subproblems)
- Optimal Alt Yapı (Optimal Substructure)
- Bottom-Up (Tabulation) vs. Top-Down (Memoization)

**Klasik DP Problemleri:**

| Problem | Boyut | Karmaşıklık |
|---------|-------|-------------|
| Çanta (Knapsack) | $O(nW)$ | Pseudo-polynomial |
| En Uzun Ortak Dizi (LCS) | $O(mn)$ | Polynomial |
| Matris Zinciri Çarpımı | $O(n^3)$ | Polynomial |
| Stok Yönetimi (Inventory DP) | $O(T \cdot S^2)$ | Polynomial |
| En Kısa Yol (DP formu) | $O(V^2)$ | Polynomial |
| Üretim Planlama | $O(T \cdot n)$ | Polynomial |

---

### ━━━ FAZ 6 · Metasezgisel Algoritmalar ━━━━━━━━━━━━━━━━━━━━━━━━

Büyük ölçekli NP-Hard problemler için doğadan ilham alan optimizasyon.

| Algoritma | İlham | Güçlü Olduğu Alan |
|-----------|-------|-------------------|
| Genetik Algoritma (GA) | Evrim | TSP, Job-Shop |
| Tavlama Benzetimi (SA) | Metallurji | Combinatorial |
| Parçacık Sürüsü (PSO) | Kuş sürüsü | Sürekli optimizasyon |
| Karınca Kolonisi (ACO) | Karınca davranışı | Rotalama (VRP) |
| Tabu Arama | Hafıza mekanizması | Yerel minimum kaçınma |
| Diferansiyel Evrim | Popülasyon bazlı | NLP |

**Uygulama:** `genetic_algorithm_tsp.py` — Gezgin Satıcı Problemi (TSP) için tam GA implementasyonu *(seçim, çaprazlama, mutasyon, elitizm)*

---

### ━━━ FAZ 7 · Doğrusal Olmayan Programlama (NLP) ━━━━━━━━━━━━━━━━

Gerçek dünyanın kırık, eğimli, karmaşık yüzeylerinde optimizasyon.

**Koşulsuz Optimizasyon:**
- Gradient Descent (Sabit, line-search, momentum adımları)
- Newton-Raphson ve Quasi-Newton (BFGS, L-BFGS)
- Eşlenik Gradyan Yöntemi

**Kısıtlı NLP:**
- Karush-Kuhn-Tucker (KKT) Birinci Mertebe Koşulları
- Lagrange Çarpanları Yöntemi
- Ceza Fonksiyonu (Penalty/Barrier) Yaklaşımları
- Sequential Quadratic Programming (SQP)

**Dışbükeylik Analizi:**
- Hessian Matrisi pozitif yarı-tanımlılık testi
- Genel dışbükey vs. quasi-convex fonksiyonlar
- SOCP (Second-Order Cone Programming)

---

### ━━━ FAZ 8 · Oyun Teorisi & Çok Amaçlı Optimizasyon ━━━━━━━━━━━

Çelişen çıkarların matematiksel modellenmesi ve denge analizi.

**Oyun Teorisi:**
- Sıfır Toplamlı Oyunlar — Minimax Teoremi (von Neumann, 1928)
- Nash Dengesi — Ekzistans İspatı
- Karma Strateji Hesabı — LP Formulasyonu
- Tekrarlayan Oyunlar — Folk Teoremi
- Mekanizma Tasarımı — Vickrey Açık Artırması

**Çok Amaçlı Optimizasyon (MOO):**
- Pareto Cephesi (Pareto Front) ve Dominans
- ε-kısıt Yöntemi
- Ağırlıklı Toplam Skalarizasyon
- NSGA-II Algoritması (Çok Amaçlı GA)
- Hedef Programlama (Goal Programming) — Lexicographic

---

## 🛠️ Teknoloji ve Yazılım Stoku

```python
# Optimizasyon Çerçeveleri
import pulp          # LP & ILP — hızlı prototipleme
import pyomo         # Büyük ölçekli, karmaşık modeller
from ortools.linear_solver import pywraplp  # Google OR-Tools

# Grafiksel & Ağ Analizi
import networkx      # Graf yapıları, ağ akışı
import matplotlib    # Sonuç görselleştirme

# Stokastik & Simülasyon
import simpy         # Discrete-Event Simulation (DES)
import scipy.stats   # Olasılık dağılımları

# Sayısal Hesaplama
import numpy as np   # Matris işlemleri
import pandas as pd  # Veri yönetimi
import scipy.optimize as opt  # NLP çözücüleri (SLSQP, COBYLA)
```

**Çözücüler (Solvers):**

| Çözücü | Tip | Lisans | Kullanım |
|--------|-----|--------|----------|
| CBC | LP/MILP | Açık Kaynak | Genel amaç |
| GLPK | LP/MILP | GNU | Küçük/orta |
| IPOPT | NLP | Eclipse | İç nokta NLP |
| Gurobi | LP/MILP/QP | Ticari | Endüstri standardı |
| CPLEX | LP/MILP | Ticari | IBM enterprise |
| SCIP | MILP/NLP | ZIB | Araştırma |

---

## 📂 Depo Ağaç Yapısı (v2.0)

```
Yoneylem-Ders-Notlari/
│
├── 📁 01_Linear_Programming/
│   ├── theory_notes.md                    ← Teorik temel & LP geometrisi
│   ├── simplex_algorithm_step_by_step.ipynb  ← Adım adım Simpleks
│   ├── sensitivity_analysis.ipynb         ← Duyarlılık analizi & parametrik
│   ├── dual_problem_generator.py          ← Primal→Dual dönüştürücü
│   └── sensitivity_analyzer.py            ← Otomatik SA raporu
│
├── 📁 02_Network_Optimization/
│   ├── README.md
│   ├── transportation_and_assignment/
│   │   ├── transportation_solver.py       ← VAM + Ulaştırma Simpleksi
│   │   └── hungarian_algorithm.py         ← Macar Algoritması (tam)
│   └── graph_algorithms/
│       ├── dijkstra_visualizer.py         ← En kısa yol + görselleştirme
│       ├── max_flow_ford_fulkerson.py      ← Ford-Fulkerson
│       └── mst_kruskal.py                 ← Minimum Yayılan Ağaç
│
├── 📁 03_Integer_Programming/
│   ├── README.md
│   ├── branch_and_bound_visualization.ipynb  ← B&B ağaç görselleştirme
│   ├── facility_location_problem.py       ← p-Medyan & kapasiteli FLP
│   └── knapsack_solver.py                 ← 0-1, Bounded, Unbounded knapsack
│
├── 📁 04_Stochastic_Models/
│   ├── README.md
│   ├── markov_chain_analyzer.py           ← Geçiş matrisi & kararlı durum
│   ├── markov_chains_transition.ipynb     ← Interaktif Markov analizi
│   ├── queuing_theory_simulation.py       ← M/M/1, M/M/c, M/G/1 simülasyonu
│   └── monte_carlo_integration.py         ← Monte Carlo & Risk analizi
│
├── 📁 05_Dynamic_Programming/
│   ├── README.md                          ← DP doktrini ve metodoloji
│   ├── knapsack_dp.py                     ← 0-1 Knapsack — tabulation & memo
│   ├── inventory_dp.py                    ← Stok Yönetimi DP modeli
│   └── shortest_path_dp.py               ← Bellman-Ford DP yaklaşımı
│
├── 📁 06_Metaheuristics/
│   ├── README.md
│   ├── genetic_algorithm_tsp.py           ← GA ile TSP çözümü
│   └── simulated_annealing_solver.py      ← SA kombinatoryal optimizasyon
│
├── 📁 07_Nonlinear_Programming/
│   ├── README.md
│   └── gradient_descent_optimizer.py      ← GD variants (SGD, Adam, Momentum)
│
├── 📁 08_Game_Theory/
│   ├── README.md                          ← Oyun teorisi doktrini
│   ├── zero_sum_game_solver.py            ← Minimax + LP formulasyonu
│   └── nash_equilibrium_finder.py         ← Karma strateji Nash dengesi
│
├── 📁 data/
│   ├── transportation_benchmark.csv       ← Ulaştırma problem veri seti
│   ├── facility_locations.csv             ← Tesis yeri seçim verisi
│   └── queueing_arrival_data.csv          ← Kuyruk simülasyonu input
│
├── or_engine.py                           ← Ana OR CLI motoru
├── requirements.txt                       ← Python bağımlılıkları
└── README.md                              ← Bu dosya
```

---

## 🚀 Hızlı Başlangıç

```bash
# 1. Depoyu klonla
git clone https://github.com/<kullanici>/Yoneylem-Ders-Notlari.git
cd Yoneylem-Ders-Notlari

# 2. Bağımlılıkları yükle
pip install -r requirements.txt

# 3. OR Engine'i çalıştır
python or_engine.py

# 4. Spesifik modül örneği
python 01_Linear_Programming/dual_problem_generator.py
python 04_Stochastic_Models/queuing_theory_simulation.py
python 06_Metaheuristics/genetic_algorithm_tsp.py
python 08_Game_Theory/zero_sum_game_solver.py
```

---

## 📖 Başvuru Kaynakları ve Akademik Arşiv

| Kaynak | Kapsam |
|--------|--------|
| *Taha, H.A. (2017) — Operations Research: An Introduction* | LP, IP, Ağ, Kuyruk |
| *Winston, W.L. (2003) — OR: Applications and Algorithms* | Geniş kapsam, uygulamalar |
| *Hillier & Lieberman (2014) — Intro to Operations Research* | Teori + endüstri |
| *Nocedal & Wright (2006) — Numerical Optimization* | NLP, Metot teorisi |
| *Puterman (1994) — Markov Decision Processes* | MDP, DP, RL bağlantısı |
| *Osborne & Rubinstein (1994) — A Course in Game Theory* | Nash, mekanizma tasarımı |
| *Goldberg (1989) — Genetic Algorithms in Search, Optimization* | GA temelleri |

**Online Araçlar:**
- [NEOS Server](https://neos-server.org) — Çevrimiçi OR çözücüsü
- [Gurobi Academic](https://gurobi.com) — Ücretsiz akademik lisans
- [OR-Tools](https://developers.google.com/optimization) — Google'ın açık kaynak OR çerçevesi

---

<div align="center">

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  "Bir problemi çözememek, o problemi doğru formüle edememiş
   olmak demektir. Matematiksel zarafet, net Düşüncenin gölgesidir."
                                         — George Dantzig
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

*Bilim, karmaşayı basit denklemlere indirgeme sanatıdır. İyi optimizasyonlar!*

</div>
