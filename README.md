<div align="center">

بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ

</div>

---

# ⚙️ Yöneylem Araştırması — Karar Mühendisliğinin Zirve Arşivi

<div align="center">

[![Disiplin](https://img.shields.io/badge/Disiplin-Yöneylem%20Araştırması-0A0A2E?style=for-the-badge&logo=mathworks&logoColor=white)](https://en.wikipedia.org/wiki/Operations_research)
[![Alan](https://img.shields.io/badge/Alan-Endüstri%20Mühendisliği-1A1A4E?style=for-the-badge&logo=academia&logoColor=cyan)](#)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Lisans](https://img.shields.io/badge/Lisans-MIT-22C55E?style=for-the-badge)](#)
[![Modül](https://img.shields.io/badge/Modül-8%20Faz-7C3AED?style=for-the-badge)](#)
[![Durum](https://img.shields.io/badge/Durum-Aktif%20Geliştirme-16A34A?style=for-the-badge)](#)

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
1909  ─▶  A.K. Erlang     ── Kuyruk Teorisi (telefon santralleri)
1916  ─▶  F.W. Lanchester ── Askeri çatışma diferansiyel denklemleri
1939  ─▶  Kantorovich      ── Doğrusal Programlama (nakliye optimizasyonu)
1941  ─▶  P. Blackett      ── "Blackett's Circus" -- denizaltı savaşı OR modelleri
1947  ─▶  G. Dantzig       ── Simpleks Algoritması (ABD Hava Kuvvetleri)
1950  ─▶  J. Nash          ── Nash Dengesi, Oyun Teorisi
1953  ─▶  R. Bellman       ── Dinamik Programlama -- Optimallik Prensibi
1957  ─▶  Ford & Fulkerson ── Maksimum Akış Algoritması
1984  ─▶  Karmarkar        ── İç Nokta Yöntemi (Interior Point)
2000+ ─▶  AI/ML Füzyonu    ── Reinforcement Learning + OR hibrid sistemler
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
| 1.5 Duyarlılık | Gölge Fiyatı, parametre aralıkları | `sensitivity_analyzer.py` |

---

### ━━━ FAZ 2 · Ağ Optimizasyonu (Network Models) ━━━━━━━━━━━━━━━━

| Algoritma | Karmaşıklık | Uygulama |
|-----------|------------|----------|
| Kuzey-Batı Köşesi | O(m+n) | Başlangıç çözümü |
| Vogel Yaklaşımı | O(m·n) | Daha iyi başlangıç |
| Macar Algoritması | O(n³) | Atama problemi |
| Dijkstra | O((V+E)log V) | En kısa yol |
| Ford-Fulkerson | O(E · max_flow) | Maksimum Akış |
| CPM/PERT | O(V+E) | Kritik Yol Analizi |

---

### ━━━ FAZ 3 · Tamsayılı & Karma Programlama (MILP) ━━━━━━━━━━━━━

| Konu | Yöntem |
|------|--------|
| Dal ve Sınır | Ağaç araması, sınır hesabı, budama |
| Gomory Kesmeleri | LP relaxation + kesme düzlemleri |
| Teslimat Yer Seçimi | Facility Location (p-medyan) modeli |
| Çanta Problemi | 0-1 knapsack, bounded, unbounded |

---

### ━━━ FAZ 4 · Stokastik Modeller ve Rastlantısallık ━━━━━━━━━━━━━━

Belirsizlik, olasılık ve zamanın sisteme dahil edilmesi.

| Model | Formül | Uygulama |
|-------|--------|----------|
| M/M/1 | $\rho^2/(1-\rho)$ | Tek gişeli banka |
| M/M/c | Erlang-C | Çağrı merkezi |
| M/D/1 | $\rho^2/(2(1-\rho))$ | Sabit servis ATM |
| M/G/1 | Pollaczek-Khinchine | Genel dağılım |

---

### ━━━ FAZ 5 · Dinamik Programlama ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bellman'ın Optimallik Prensibi: $V^*(s) = \max_{a} [R(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')]$

---

### ━━━ FAZ 6 · Metasezgisel Algoritmalar ━━━━━━━━━━━━━━━━━━━━━━━━

| Algoritma | İlham | Güçlü Olduğu Alan |
|-----------|-------|-------------------|
| Genetik Algoritma (GA) | Evrim | TSP, Job-Shop |
| Tavlama Benzetimi (SA) | Metallurji | Kombinatoryal |
| Karınca Kolonisi (ACO) | Karınca davranışı | Rotalama (VRP) |
| Tabu Arama | Hafıza mekanizması | Yerel minimum kaçınma |

---

### ━━━ FAZ 7 · Doğrusal Olmayan Programlama (NLP) ━━━━━━━━━━━━━━━━

- **Gradient Descent** (SGD, Momentum, Adam)
- **KKT Şartları** ve Lagrange Çarpanları
- **Hessian Matrisi** ile konveksite analizi

---

### ━━━ FAZ 8 · Oyun Teorisi & Çok Amaçlı Optimizasyon ━━━━━━━━━━━━

- **Nash Dengesi**: Karma Strateji Hesabı (LP Formulasyonu)
- **Minimax Teoremi**: Von Neumann, 1928
- **Pareto Cephesi**: Çok amaçlı optimizasyon
- **Hedef Programlama**: Lexicographic önceliklendirme

---

## 🛠️ Teknoloji ve Yazılım Stoku

```python
import pulp          # LP & ILP
import pyomo         # Büyük ölçekli modeller
import networkx      # Graf yapıları, ağ akışı
import simpy         # Discrete-Event Simulation
import scipy.optimize as opt  # NLP çözücüleri
import numpy as np   # Matris işlemleri
import pandas as pd  # Veri yönetimi
```

**Çözücüler:** CBC · GLPK · IPOPT · Gurobi · CPLEX · SCIP

---

## 📂 Depo Ağaç Yapısı (v2.0)

```
Yoneylem-Ders-Notlari/
├── 01_Linear_Programming/
├── 02_Network_Optimization/
├── 03_Integer_Programming/
├── 04_Stochastic_Models/
├── 05_Dynamic_Programming/
├── 06_Metaheuristics/
├── 07_Nonlinear_Programming/
├── 08_Game_Theory/
├── data/
├── or_engine.py
├── requirements.txt
└── README.md
```

---

## 🚀 Hızlı Başlangıç

```bash
git clone https://github.com/arch-yunus/Yoneylem-Ders-Notlari.git
cd Yoneylem-Ders-Notlari
pip install -r requirements.txt
python or_engine.py
```

---

## 📖 Başvuru Kaynakları

| Kaynak | Kapsam |
|--------|--------|
| *Taha, H.A. — Operations Research: An Introduction* | LP, IP, Ağ, Kuyruk |
| *Winston, W.L. — OR: Applications and Algorithms* | Geniş kapsam |
| *Hillier & Lieberman — Intro to Operations Research* | Teori + endüstri |
| *Nocedal & Wright — Numerical Optimization* | NLP, Metot teorisi |
| *Osborne & Rubinstein — A Course in Game Theory* | Nash, mekanizma |

---

<div align="center">

> *"Bir problemi çözememek, o problemi doğru formüle edememiş olmak demektir."*
> — **George Dantzig**

**Yöneylem Araştırması Arşivi — arch-yunus**

</div>
