# 🔄 Kullanıcı Akışı: Health Compass

## Genel Bakış

Health Compass'da kullanıcı deneyimi **4 ana adımda** tamamlanır. Her adım bir öncekine sorunsuz bağlanır; kullanıcı hiçbir aşamada kaybolmaz.

---

## 4 Adımlı Ana Akış

### Adım 1 — 🏠 Giriş

```
[KARŞILAMA EKRANI]
  Modern Glassmorphism arayüzü
  — Yarı saydam kartlar, bulanık arka plan efekti
  — Health Compass logosu ve sloganı
  — "Yapay Zeka Destekli Kişisel Sağlık Pusulanız"
     |
     v
Kullanıcı "Semptomlarımı Analiz Et" butonuna tıklar
```

**Tasarım Notu:** Glassmorphism efekti (`backdrop-filter: blur`) ile oluşturulan yarı saydam panel, kullanıcıya profesyonel ve modern bir his verir. Karşılama ekranı herhangi bir kayıt veya giriş gerektirmez — tek tıkla analiz başlar.

---

### Adım 2 — 🔬 Analiz

```
[SEMPTOM GİRİŞ EKRANI]
  Kullanıcı semptomlarını serbest metin olarak yazar
  Opsiyonel: Yaş, kronik hastalık, semptom süresi
     |
     v
"Analiz Et" butonuna tıklanır
     |
     v
[YÜKLENİYOR — Animasyonlu geçiş ekranı]
  "Semptomlarınız Gemini 2.5 Flash ile işleniyor..."
     |
     | Gemini 2.5 Flash API çağrısı
     | → Semptom metni + ek bilgiler prompt'a eklenir
     | → JSON formatında yapılandırılmış yanıt alınır
     v
Yanıt parse edilir → Adım 3'e geçilir
```

**Teknik Not:** Gemini 2.5 Flash modeli kullanılır. Hızlı analiz süresi (≤10 saniye) ve güvenilir JSON yapılandırma kapasitesi bu adımın temelini oluşturur. Kota aşımı (429) durumunda Gemini 2.0 Flash → 1.5 Flash fallback zinciri devreye girer.

---

### Adım 3 — 🎯 Sonuç

```
[TRİAGE SONUÇ EKRANI]
  Renk kodlu aciliyet kartı gösterilir:
     |
     +---> 🔴 Kırmızı Kart — ACİL
     |         "Hemen Acil Servise Gidin"
     |         Aciliyet gerekçesi + önerilen adımlar
     |
     +---> 🟡 Mavi Kart — BUGÜN
     |         "Aynı Gün Doktora Başvurun"
     |         Hangi uzmanla görüşülmeli
     |
     +---> 🟢 Yeşil Kart — EV TAKİBİ
               "Şimdilik Evde Gözlemleyin"
               Evde takip önerileri + 48 saat hatırlatması
```

**Tasarım Notu:** Kartlar CSS animasyonuyla yukarıdan aşağıya süzülerek görünür. Renk körü kullanıcılar için aciliyet seviyesi hem renkle hem ikonla (🔴🟡🟢) gösterilir.

---

### Adım 4 — ⚡ Aksiyon (Pusula Özelliği)

```
[SONUÇ KARTI ALTINDA]
  "Bu Uzmanı Bul" butonu görünür
     |
     | Kullanıcı butona tıklar
     v
[OTOMATİK SMOOTH SCROLL]
  Sayfa, uzman arama formuna yumuşak kaydırmayla iner
  (window.scrollTo ile animasyonlu geçiş)
     |
     v
[OTOMATİK FORM DOLDURMA — Pusula Özelliği]
  Triage'dan gelen veriler forma otomatik yazılır:
  ✅ Uzman türü alanı → Gemini'nin önerdiği uzmanlık
  ✅ Şehir alanı → Kullanıcının daha önce girdiği konum (varsa)
  Kullanıcı yalnızca eksik alanları tamamlar ve "Ara" der
     |
     v
[UZMAN LİSTESİ]
  Gemini, ilgili şehirdeki uzmanları ve kurumları listeler
  Her kart: Ad, uzmanlık, kurum, randevu yöntemi
```

**Bu Adımın Önemi:** Diğer semptom uygulamaları analizi bitirip kullanıcıyı başıboş bırakır. Health Compass, **"Pusula" özelliğiyle** bir sonraki adımı otomatik olarak hazırlar. Kullanıcı hiçbir bilgiyi tekrar yazmak zorunda kalmaz.

---

## Akış Özeti (Tek Bakışta)

```
[Glassmorphism Karşılama]
         |
         v
   [Semptom Girişi]
         |
    Gemini 2.5 Flash
         |
         v
  [Renk Kodlu Sonuç Kartı]
  🔴 Kırmızı / 🟡 Mavi / 🟢 Yeşil
         |
    "Bu Uzmanı Bul"
         |
    Smooth Scroll ↓
         |
         v
[Otomatik Dolu Uzman Formu]
         |
         v
    [Uzman Listesi]
```

---

## Önemli UX Kararları

| Karar | Gerekçe |
|---|---|
| Glassmorphism arayüz | Modern, güven veren görsel dil; tıbbi uygulamalara yakışır profesyonellik |
| 4 adıma indirgeme | Kullanıcıyı bunaltmadan baştan sona rehberlik |
| Renk kodlu kart sistemi | Aciliyeti anında kavratır, okuma gerektirmez |
| Smooth Scroll + Otomatik Form | Sürtünmesiz UX; kullanıcı hiçbir şeyi iki kez yazmaz |
| Gemini 2.5 Flash | Hızlı yanıt süresi kullanıcıyı bekletmez |
| Kesin tanı YOK | Yasal ve etik sorumluluk; yapay zeka doktor değildir |
