# Modül 4: Stokastik Modeller ve Olasılıksal Süreçler 🎲

Gerçek dünyadaki sistemler her zaman deterministik (kesin) değildir. Bu modül, belirsizlik altındaki sistemleri olasılık kuralları ile modellemeye odaklanır.

## 📝 Teorik Temeller

### 1. Markov Zincirleri (Markov Chains)
Gelecekteki durumun sadece şimdiki duruma bağlı olduğu (geçmişten bağımsız) süreçlerdir.
- **Geçiş Matrisi (P):** Bir durumdan diğerine geçme olasılıklarını gösterir.
- **Kararlı Durum (Steady State):** Sistemin uzun vadedeki denge durumudur ($\pi P = \pi$).

### 2. Kuyruk Teorisi (Queueing Theory)
Bekleme hatlarının analizi.
- **Little Yasası:** $L = \lambda W$.
- **M/M/1:** Poisson varışlı, Üssel servis süreli tek kanallı kuyruk.

## 🛠️ Dahili Araçlar

### [queuing_theory_simulation.py](queuing_theory_simulation.py)
Bir banka veya fabrikadaki kuyruk performansını (ortalama bekleme süresi, kuyruk uzunluğu) simüle eden bir araçtır.

### [markov_chain_analyzer.py](markov_chain_analyzer.py)
Verilen geçiş matrisinden sistemin uzun vadeli pazar paylarını veya denge durumlarını hesaplar.

## 📚 Kaynakça
- *Ross, S. M.:* Introduction to Probability Models.
- *Gross, D. & Harris, C. M.:* Fundamentals of Queueing Theory.
