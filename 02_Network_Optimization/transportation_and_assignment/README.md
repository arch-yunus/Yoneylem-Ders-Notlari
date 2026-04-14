# Ulaştırma ve Atama Modelleri 🚚🤝

Ulaştırma ve Atama problemleri, Doğrusal Programlamanın özel bir alt sınıfıdır ve genellikle ağ yapısı üzerinde modellenirler.

## 1. Ulaştırma Problemi (Transportation Problem)
Amacımız, belirli kaynaklardan (fabrikalar) belirli varış noktalarına (depolar) ürün sevkiyatını, toplam taşıma maliyetini minimize edecek şekilde planlamaktır.

### Temel Kavramlar:
- **Kaynaklar (Supply):** Her kaynağın sunduğu kapasite.
- **Talepler (Demand):** Her varış noktasının ihtiyacı olan miktar.
- **Birim Maliyet ($c_{ij}$):** $i$ kaynağından $j$ varış noktasına bir birim taşımanın maliyeti.

### Başlangıç Çözüm Yöntemleri:
1.  **Kuzeybatı Köşesi Yöntemi (Northwest Corner Rule):** En basit ama genelde maliyeti yüksek yöntem.
2.  **En Düşük Maliyet Yöntemi (Least Cost Method):** Tablodaki en ucuz hücreye öncelik verir.
3.  **Vogel Yaklaşımlı Yöntemi (VAM):** Ceza maliyetlerini (fırsat maliyetleri) hesaplayarak daha kaliteli başlangıç çözümü üretir.

---

## 2. Atama Problemi (Assignment Problem)
$n$ adet işin $n$ adet kişiye, her işe bir kişi ve her kişiye bir iş gelecek şekilde, toplam maliyetin (veya sürenin) minimum olacağı şekilde atanmasıdır.

### Macar Algoritması (Hungarian Algorithm):
Atama problemlerini çözmek için kullanılan en etkili yöntemdir. Adımları:
1.  **Satır İndirgeme:** Her satırdan satırın en küçük değerini çıkar.
2.  **Sütun İndirgeme:** Her sütundan sütunun en küçük değerini çıkar.
3.  **Çizgi Kapsama:** Sıfırların üzerini en az sayıda çizgi ile kapatmaya çalış.
4.  **Atama:** Eğer çizgi sayısı $n$ ise atama yapılır. Değilse, açıkta kalanların en küçüğü ile matris güncellenir.
