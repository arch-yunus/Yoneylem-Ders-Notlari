# Modül 5: Oyun Teorisi ve Stratejik Karar Verme ♟️

Oyun Teorisi, rasyonel karar vericilerin birbirleriyle etkileşim içinde olduğu durumların matematiksel modellerini inceler. Sadece kendi hamleniz değil, rakiplerin olası karşı hamleleri de hesaba katılır.

## 📝 Teorik Temeller

### 1. Karar Teorisi ve Belirsizlik
- **Maximin:** En kötü senaryodan en iyisini seçme (Kötümser).
- **Maximax:** En iyi senaryodan en iyisini seçme (İyimser).
- **Savage (Minimax Pişmanlık):** Fırsat kaybını minimize etme.

### 2. İki Kişilik Sıfır Toplamlı Oyunlar
Bir tarafın kazancının diğer tarafın kaybına eşit olduğu oyunlardır.
- **Eyer Noktası (Saddle Point):** Maximin == Minimax ise oyunun saf bir stratejisi vardır.
- **Karma Stratejiler:** Eğer eyer noktası yoksa, oyuncular hamlelerini olasılık dağılımlarına göre seçer.

### 3. Mahkumlar Dilemması (Prisoner's Dilemma)
Bireysel rasyonelliğin, grup için en iyi olmayan bir sonuç doğurduğu klasik oyun teorisi örneği.

## 🛠️ Dahili Araçlar

### [game_theory_solver.py](game_theory_solver.py)
Ödeme matrisini (payoff matrix) girdi olarak alarak eyer noktasını arayan ve baskın stratejileri (dominated strategies) belirleyen bir araçtır.

## 📚 Kaynakça
- *Von Neumann, J. & Morgenstern, O.:* Theory of Games and Economic Behavior.
- *Nash, J. F.:* Equilibrium Points in n-Person Games.
- *Dixit, A. K. & Nalebuff, B. J.:* Thinking Strategically.
