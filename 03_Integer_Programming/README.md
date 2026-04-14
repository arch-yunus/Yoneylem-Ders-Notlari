# Modül 3: Tamsayılı Programlama (Integer Programming) 🔢

Tamsayılı Programlama, karar değişkenlerinden bazılarının veya tamamının tamsayı olması gerektiği özel bir LP türüdür. Gerçek dünya problemlerinde (Ör: Kaç adet araba üretilmeli?, Hangi lokasyona depo açılmalı?) değişkenler genellikle süreklilik göstermez.

## 📝 Teorik Temeller

### 1. Karar Değişkenleri Türleri
- **Saf Tamsayılı (Pure Integer):** Tüm değişkenler tamsayı.
- **Karışık Tamsayılı (Mixed Integer - MILP):** Bazı değişkenler tamsayı, bazıları sökrekli.
- **İkilik (Binary 0-1):** Değişkenler sadece 0 veya 1 değerini alabilir (Evet/Hayır kararları).

### 2. Çözüm Metotları
- **Dal ve Sınır (Branch and Bound):** Çözüm uzayını alt kümelere bölerek en iyi tamsayılı çözümü arar.
- **Kesme Düzlemleri (Cutting Planes - Gomory Cuts):** LP genişlemesini tamsayı olmayan bölgeleri kesecek şekilde daraltır.

## 🛠️ Dahili Araçlar

### [facility_location_problem.py](facility_location_problem.py)
Şehirler veya lokasyonlar arasından en düşük maliyetle servis verecek noktaların seçimini yapan binary bir modeldir.

### [knapsack_solver.py](knapsack_solver.py)
Sınırlı bir kapasiteye (hacim/ağırlık) sahip bir taşıyıcıya, toplam değeri maksimize edecek şekilde hangi eşyaların konulması gerektiğini çözen temel bir algoritmadır.

## 📚 Kaynakça
- *Wolsey, L. A.:* Integer Programming.
- *Schrijver, A.:* Theory of Linear and Integer Programming.
