# Yöneylem Ders Notları 🎯 : Kapsamlı Optimizasyon ve Karar Bilimi Arşivi

[![Discipline: Operations Research](https://img.shields.io/badge/Discipline-Operations%20Research-blue.svg)]()
[![Field: Industrial Engineering](https://img.shields.io/badge/Field-Industrial%20Engineering-darkred.svg)]()
[![Complexity: Advanced](https://img.shields.io/badge/Complexity-Advanced-purple.svg)]()
[![Status: Maintained](https://img.shields.io/badge/Status-Maintained-success.svg)]()

> "Optimizasyon, sadece en iyiyi bulmak değil; karmaşanın içindeki gizli düzeni matematiksel bir zarafetle ortaya çıkarmaktır."

## 📜 Manifesto ve Amacımız
Bu depo, **Yöneylem Araştırması (Operations Research - OR)** disiplininin teorik temellerini, matematiksel ispatlarını ve modern yazılım araçlarıyla (Python çözücüleri) endüstriyel uygulamalarını bir araya getiren açık kaynaklı bir külliyattır. Amacımız; deterministik ve stokastik sistemleri modelleme, kısıtlı kaynakları en verimli şekilde tahsis etme ve sezgileri geride bırakıp kanıta dayalı (data-driven) karar mimarileri inşa etmek üzere tasarlanmıştır.

Bu dokümantasyon; standart bir lisans müfredatından başlayarak, yüksek lisans seviyesindeki karmaşık sistem tasarımlarına kadar uzanan geniş bir yelpazeyi kapsar.

---

## 🕰️ Kısa Tarihçe: Çaresizlikten Doğan "Hayatta Kalma" Matematiği
Yöneylem Araştırması, fildişi kulelerdeki teorik bir uğraş değil; savaşların, krizlerin ve endüstriyel darboğazların ortasında doğmuş bir "kriz çözme" bilimidir. Bu depo, kodlara dökülen şu devasa mirasın üzerinde yükselir:

* **1. Kıvılcımlar (1900'ler):** A.K. Erlang'ın telefon santrallerindeki beklemeleri çözmek için **Kuyruk Teorisini** icat etmesi ve F.W. Lanchester'ın askeri çatışmaları diferansiyel denklemlere dökmesiyle ilk adımlar atıldı.
* **2. Doğuş - "Blackett'in Sirki" (II. Dünya Savaşı):** Disiplin, adını ve ruhunu İngiltere'de aldı. Radar verilerini işlemek ve Alman U-Bot denizaltılarına karşı gemi konvoylarını korumak için fizikçi Patrick Blackett liderliğinde çok disiplinli bir bilim ekibi kuruldu. Geliştirdikleri olasılık modelleri, tek kurşun atmadan savaşın seyrini değiştirdi.
* **3. Altın Çağ ve Simpleks (1947):** Savaş sonrası ABD ordusunun lojistik ağını optimize etmek için **George Dantzig**, tüm zamanların en büyük algoritmalarından birini, **Simpleks Algoritmasını** (Simplex Method) icat etti. John von Neumann'ın "Dualite" katkısıyla alan tamamen matematiksel bir zemine oturdu.
* **4. Bilgisayar Devrimi (Günümüz):** Havayolu şirketlerini iflastan kurtaran algoritmalardan (Yield Management), Amazon'un lojistik rotalarına, Uber'in fiyatlandırma motorundan yüksek frekanslı borsa algoritmalarına (HFT) kadar modern dünyanın görünmez mimarisi haline geldi.

---

## 📐 Matematiksel Temel (Kanonik Form)
Her yöneylem modeli belirli bir matematiksel disipline dayanır. Genel bir Doğrusal Programlama (LP) probleminin standart matris formu şu şekildedir:

**Amaç Fonksiyonu:**
$$\max (\text{veya } \min) \quad Z = \mathbf{c}^T \mathbf{x}$$

**Kısıtlar (Sistemin Sınırları):**
$$\mathbf{A}\mathbf{x} \leq \mathbf{b}$$
$$\mathbf{x} \geq \mathbf{0}$$

*(Burada $\mathbf{x}$ karar değişkenleri vektörünü, $\mathbf{c}$ maliyet/kar katsayılarını, $\mathbf{A}$ teknoloji matrisini ve $\mathbf{b}$ sağ taraf sabitlerini/kaynak kapasitelerini temsil eder.)*

---

## 📚 Kapsamlı Müfredat ve Modül Mimarisi

### 🏗️ FAZ 1: Deterministik Modeller ve Doğrusal Programlama (LP)
Kesin bilinen parametreler altında sistem optimizasyonu.
* **1.1. Model Kurma Sanatı:** Karar uzayını tanımlama, sürekli ve kesikli değişkenler, kısıtların cebirsel inşası.
* **1.2. Çözüm Uzayı Analizi:** 2D ve 3D uzayda grafiksel çözüm, Dışbükey (Convex) setler ve Köşe Noktası (Extreme Point) teoremleri.
* **1.3. Simpleks Algoritması (Derinlemesine):**
  * Temel ve Temel Olmayan değişkenler matrisi.
  * Simpleks tablosu iterasyonları ve pivotlama.
  * Suni Değişken Teknikleri: Büyük-M (Big-M) ve İki Aşamalı (Two-Phase) Yöntemler.
* **1.4. Dualite Teorisi:** Primal-Dual dönüştürme mekanizmaları, Zayıf ve Güçlü Dualite Teoremleri.
* **1.5. Duyarlılık (Sensitivity) ve Parametrik Analiz:** Gölge Fiyatı (Shadow Price), katsayı ($\mathbf{c}$) ve kaynak ($\mathbf{b}$) değişim aralıkları.

### 🕸️ FAZ 2: Özel Algoritmalar ve Ağ (Network) Modelleri
Özel yapılı matrisler için geliştirilmiş hızlandırılmış optimizasyon teknikleri.
* **2.1. Ulaştırma ve Aktarma Modelleri:** Kuzeybatı Köşesi, Vogel Yaklaşım Metodu (VAM), Ulaştırma Simpleksi.
* **2.2. Atama Problemleri:** Macar Algoritması (Hungarian Method).
* **2.3. Ağ Optimizasyonu (Network Flow):** Dijkstra (En Kısa Yol), Kruskal/Prim (Minimum Yayılan Ağaç), Ford-Fulkerson (Maksimum Akış), CPM/PERT (Proje Yönetimi).

### 🔢 FAZ 3: Karmaşıklığı Yönetmek (MILP ve NLP)
* **3.1. Tamsayılı Programlama (Integer Programming):** Dal ve Sınır Algoritması (Branch and Bound), Kesme Düzlemleri (Gomory Cuts).
* **3.2. Hedef Programlama (Goal Programming):** Çelişen çoklu amaçların önceliklendirilmesi.
* **3.3. Doğrusal Olmayan Programlama (NLP):** Kısıtlı NLP ve Karush-Kuhn-Tucker (KKT) Şartları.

### 🎲 FAZ 4: Stokastik Süreçler ve Dinamik Modeller
Belirsizlik, olasılık ve zamanın sisteme dahil edilmesi.
* **4.1. Markov Zincirleri:** Durum geçiş matrisleri ve kararlı durum olasılıkları.
* **4.2. Kuyruk Teorisi (Queueing Systems):** Kendall Notasyonu, M/M/1 ve M/M/c kuyruk modellerinin performans analizi.
* **4.3. Dinamik Programlama:** Bellman'ın Optimallik Prensibi.
* **4.4. Oyun Teorisi:** Sıfır toplamlı oyunlar, Minimax stratejisi ve Nash Dengesi.

---

## 🛠️ Kullanılan Teknolojiler ve Yazılım Stoku
Teorik modelleri pratiğe dökmek için depo içerisinde aşağıdaki endüstri standardı araçlar kullanılmaktadır:

* **Modelleme Arayüzleri:** `Pyomo` (Karmaşık modeller), `PuLP` (LP ve ILP), `Google OR-Tools` (Kısıt programlama).
* **Çözücüler (Solvers):** *Açık Kaynak:* CBC, GLPK. *Ticari:* Gurobi, CPLEX.
* **Veri İşleme ve Görselleştirme:** `Pandas`, `NumPy`, `Matplotlib`, `NetworkX`.

---

## 📂 Depo Hiyerarşisi (Tree)

```text
Yoneylem-Ders-Notlari/
├── 01_Linear_Programming/
│   ├── theory_notes.md
│   ├── simplex_algorithm_step_by_step.ipynb
│   └── sensitivity_analysis.ipynb
├── 02_Network_Optimization/
│   ├── transportation_and_assignment/
│   └── graph_algorithms/
├── 03_Integer_Programming/
│   ├── branch_and_bound_visualization.ipynb
│   └── facility_location_problem.py
├── 04_Stochastic_Models/
│   ├── markov_chains_transition.ipynb
│   └── queuing_theory_simulation.py
├── data/                    # Örnek problem veri setleri (.csv, .dat)
├── requirements.txt         # Gerekli Python kütüphaneleri
└── README.md
```

---

## 📖 Referanslar ve İleri Okuma (Bibliography)
Bu notların oluşturulmasında temel alınan başvuru kaynakları:
1. *Taha, H. A. (2017).* Operations Research: An Introduction.
2. *Winston, W. L. (2003).* Operations Research: Applications and Algorithms.
3. *Hillier, F. S., & Lieberman, G. J. (2014).* Introduction to Operations Research.

---
*Bilim, karmaşayı basit denklemlere indirgeme sanatıdır. İyi optimizasyonlar!*
