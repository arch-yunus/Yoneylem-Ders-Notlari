# FAZ 1: Deterministik Modeller ve Doğrusal Programlama (LP) 📈

Doğrusal Programlama, kısıtlı kaynakların (zaman, hammadde, bütçe) belirli bir amaç fonksiyonunu (kar maksimizasyonu veya maliyet minimizasyonu) optimize edecek şekilde tahsis edilmesini sağlayan matematiksel bir tekniktir.

## 1. Model Kurma Sanatı (Modeling)
Bir Yöneylem Araştırması modelinin üç temel bileşeni vardır:

1.  **Karar Değişkenleri ($x_1, x_2, \dots, x_n$):** Kontrol edebildiğimiz ve değerini bulmaya çalıştığımız nicelikler.
2.  **Amaç Fonksiyonu ($max/min \ Z = c_1x_1 + c_2x_2 + \dots + c_nx_n$):** Optimize etmek istediğimiz performans kriteri.
3.  **Kısıtlar ($\sum a_{ij}x_j \leq b_i$):** Fiziksel, ekonomik veya teknik sınırlamalar.

---

## 2. Grafiksel Çözüm Yöntemi
Sadece 2 karar değişkeni içeren ($x_1$ ve $x_2$) problemler için kullanılır.
- **Uygun Çözüm Uzayı:** Tüm kısıtların aynı anda sağlandığı bölge.
- **Köşe Noktası Teoremi:** Optimum çözüm, eğer varsa, mutlaka uygun çözüm uzayının bir köşe noktasındadır.

---

## 3. Simpleks Algoritması (The Simplex Method)
George Dantzig tarafından geliştirilen bu algoritma, uygun çözüm uzayının köşeleri arasında akıllıca hareket ederek optimuma ulaşır.

### Standart Form Gereksinimleri:
- Tüm kararlar negatif olmamalıdır ($x_j \geq 0$).
- Kısıtların sağ taraf değerleri negatif olmamalıdır ($b_i \geq 0$).
- Eşitsizlikler, **aylak (slack)** veya **artık (surplus)** değişkenler eklenerek eşitliğe dönüştürülmelidir.

### Pivotlama İşlemi:
1.  **Giren Değişken:** Amaç fonksiyonunu en çok iyileştiren (en negatif $C_j - Z_j$ değeri - maksimizasyon için) değişken.
2.  **Çıkan Değişken:** En küçük oran testini ($\theta = \frac{b_i}{a_{ij}}$) sağlayan temel değişken.

---

## 4. Duyarlılık (Duyarlılık) Analizi
Model parametrelerindeki değişimlerin optimum çözümü nasıl etkilediğinin incelenmesidir.
- Sağ taraf değerlerindeki değişimler ($b_i$).
- Amaç fonksiyonu katsayılarındaki değişimler ($c_j$).
- Yeni bir kısıt veya değişken eklenmesi.

> [!TIP]
> Gerçek dünya problemlerinde veriler asla statik değildir. Duyarlılık analizi, çözümün ne kadar "sağlam" (robust) olduğunu gösterir.
