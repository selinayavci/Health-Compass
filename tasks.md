# ✅ Görev Listesi — Health Compass
> `prd.md` belgesinden türetilmiştir. Her görev bağımsız olarak tamamlanabilir.

**Durum İşaretleri:**
`[ ]` Yapılmadı &nbsp;|&nbsp; `[x]` Tamamlandı &nbsp;|&nbsp; `[~]` Devam ediyor

---

## 🗂️ FAZA 0 — Proje Kurulumu

- [x] **T-00.1** GitHub'da `health-compass` adında yeni bir repository oluştur
- [x] **T-00.2** Yerel bilgisayarda proje klasörünü oluştur ve GitHub'a bağla
- [x] **T-00.3** Klasör ve dosya yapısını oluştur
- [x] **T-00.4** `.gitignore` dosyasına `.env` satırını ekle
- [x] **T-00.5** `requirements.txt` dosyasını oluştur
- [x] **T-00.6** `pip install -r requirements.txt` komutunu çalıştır
- [x] **T-00.7** Gemini API anahtarı al
- [x] **T-00.8** `.env` dosyasına `GEMINI_API_KEY` satırını yaz
- [x] **T-00.9** Tüm dokümantasyon dosyalarını projeye ekle

---

## 🐍 FAZA 1 — Backend: Flask Sunucusu

### 1A — Temel Flask Uygulaması

- [x] **T-01.1** `app.py` dosyasında Flask uygulamasını başlat
- [x] **T-01.2** Ana sayfa route'unu ekle: `GET /` → `index.html` döndür
- [x] **T-01.3** Sunucunun `http://localhost:5000` adresinde çalıştığını doğrula

### 1B — Gemini API Entegrasyonu

- [x] **T-01.4** `gemini_service.py` dosyasında Gemini API bağlantısını kur
- [x] **T-01.5** `gemini-2.5-flash` modelini seçerek model nesnesini oluştur
- [x] **T-01.6** `semptomu_analiz_et(semptom, ek_bilgi)` fonksiyonunu yaz
- [x] **T-01.7** `uzman_bul(uzman_turu, sehir)` fonksiyonunu yaz
- [x] **T-01.8** Fonksiyonların Gemini yanıtını JSON olarak parse ettiğini doğrula

### 1C — Prompt Şablonları

- [x] **T-01.9** `TRIAGE_PROMPT` şablonunu yaz (aciliyet, uzman_turu, onerilen_adimlar, uyari)
- [x] **T-01.10** `UZMAN_PROMPT`, `UZMAN_PROMPT_TURKIYE`, `UZMAN_PROMPT_YAKIN` şablonlarını yaz

### 1D — API Endpoint'leri

- [x] **T-01.11** `POST /api/analiz` endpoint'ini yaz
- [x] **T-01.12** `POST /api/uzman-bul` endpoint'ini yaz (turkiye_geneli, konum_yakin, tercih desteğiyle)

### 1E — Hata Yönetimi

- [x] **T-01.13** Gemini API timeout durumunda hata mesajı döndür
- [x] **T-01.14** Geçersiz JSON yanıtı gelirse hata mesajı döndür
- [x] **T-01.15** Boş semptom girişi (< 10 karakter) için hata mesajı döndür
- [x] **T-01.16** `flask-limiter` ile rate limiting ekle (IP başına dakikada 10 istek)

---

## 🎨 FAZA 2 — Frontend: Tek Sayfa Uygulama (index.html)

### 2A — Ana Sayfa Bölümü

- [x] **T-02.1** Health Compass logo ve başlık alanını ekle
- [x] **T-02.2** Slogan: "Yapay Zeka Destekli Kişisel Sağlık Pusulanız" metnini ekle
- [x] **T-02.3** "Semptomlarımı Analiz Et" ana CTA butonu ekle
- [x] **T-02.4** "Uzman Bul" ikincil butonu ekle

### 2B — Semptom Giriş Bölümü

- [x] **T-02.5** Serbest metin giriş alanı ekle (min 10 / max 1000 karakter, karakter sayacı ile)
- [x] **T-02.6** "Belirtilerinizi detaylı yazın..." placeholder ekle
- [x] **T-02.7** "Analiz Et" butonu ekle
- [x] **T-02.8** Boş / çok kısa form gönderiminde uyarı mesajı göster

### 2C — Ek Bilgi Formu Bölümü

- [x] **T-02.9** "▼ Ek Bilgi Ekle" accordion başlığını ekle
- [x] **T-02.10** Yaş aralığı dropdown'ı ekle
- [x] **T-02.11** Cinsiyet dropdown'ı ekle
- [x] **T-02.12** Semptom süresi dropdown'ı ekle
- [x] **T-02.13** Kronik hastalık radio butonu ekle

### 2D — Triage Sonuç Bölümü

- [x] **T-02.14** Triage sonuç kartını semptom formunun hemen altında göster
- [x] **T-02.15** Aciliyet seviyesini büyük ikon + yazı ile göster
- [x] **T-02.16** Aciliyet kartının rengini dinamik olarak ata
- [x] **T-02.17** Aciliyet gerekçesi ve önerilen adımları göster
- [x] **T-02.18** "Önerilen Branş:" etiketiyle uzman türünü göster
- [x] **T-02.19** **"Bu Uzmanı Bul →"** butonunu ekle
- [x] **T-02.20** Yasal uyarı metnini kartın altına ekle

### 2E — Uzman Arama Bölümü

- [x] **T-02.21** "Uzman & Sağlık Kuruluşu Ara" başlığını ekle
- [x] **T-02.22** Semptom serbest metin alanı ekle (isteğe bağlı)
- [x] **T-02.23** Arama türü radio: "📍 Konuma Göre" / "📋 Uzmanlığa Göre" ekle
- [x] **T-02.24** "📍 Konumumu Kullan" butonu ekle
- [x] **T-02.25** Şehir/bölge metin giriş alanı ekle
- [x] **T-02.26** Uzmanlık alanı metin giriş alanı ekle
- [x] **T-02.27** **Kurum Tercihi** radio: Kamu / Özel / Fark Etmez ekle
- [x] **T-02.28** "Ara" butonu ekle
- [x] **T-02.29** "Bulunan Uzmanlar" listesini dinamik render et
- [x] **T-02.30** Uzman bulunamazsa MHRS yönlendirme mesajı göster

---

## 🎨 FAZA 3 — Frontend: CSS Tasarımı

- [x] **T-03.1** CSS değişkenlerini (`:root`) tanımla (triage renkleri, fontlar, boşluklar)
- [x] **T-03.2** Temel sayfa düzenini (layout) oluştur
- [x] **T-03.3** Buton stillerini tasarla
- [x] **T-03.4** Form elemanlarını stillendir
- [x] **T-03.5** Glassmorphism kart stilini yaz (`backdrop-filter: blur(12px)`)
- [x] **T-03.6** Kart giriş animasyonunu CSS ile yaz (`slideInDown`, `cubic-bezier`)
- [x] **T-03.7** Triage sonuç kartını stillendir
- [x] **T-03.8** Uzman listesi kartlarını stillendir
- [x] **T-03.9** Yükleme animasyonunu CSS ile yaz
- [x] **T-03.10** Responsive (mobil uyumlu) tasarımı ekle
- [x] **T-03.11** Minimum 14px font boyutunu tüm metinlerde kontrol et
- [x] **T-03.12** Yasal uyarı metninin görünür olduğunu doğrula

---

## ⚙️ FAZA 4 — Frontend: JavaScript

### 4A — Genel Sayfa Yönetimi

- [x] **T-04.1** Bölümleri göster/gizle fonksiyonlarını yaz
- [x] **T-04.2** "← Geri" butonlarının doğru çalıştığını sağla
- [x] **T-04.3** Yükleme göstergesini göster/gizle fonksiyonlarını yaz

### 4B — Semptom Formu ve Triage

- [x] **T-04.4** Karakter sayacını gerçek zamanlı güncelle (0/1000)
- [x] **T-04.5** "Analiz Et" butonuna tıklandığında tüm form alanlarını topla
- [x] **T-04.6** Boş/kısa semptom kontrolü yap
- [x] **T-04.7** `POST /api/analiz` endpoint'ine `fetch` ile gönder
- [x] **T-04.8** Yanıt gelince triage sonuç kartını inline render et
- [x] **T-04.9** Aciliyet seviyesine göre dinamik renk ve ikon ata

### 4C — Pusula Özelliği

- [x] **T-04.10** **"Bu Uzmanı Bul →"** butonuna event listener ekle
- [x] **T-04.11** Smooth Scroll ile uzman arama bölümüne kaydır
- [x] **T-04.12** Triage'dan gelen `uzman_turu`'nu uzman formuna otomatik yaz

### 4D — Uzman Arama (3 Mod)

- [x] **T-04.13** Arama türü radio değişince form alanlarını göster/gizle
- [x] **T-04.14** "📍 Konumumu Kullan" butonuyla Geolocation API'sini kullan
- [x] **T-04.15** Kurum Tercihi değerini form verisine ekle
- [x] **T-04.16** `POST /api/uzman-bul` endpoint'ine doğru parametrelerle gönder
- [x] **T-04.17** Gelen uzman listesini kartlar halinde render et
- [x] **T-04.18** Uzman bulunamazsa MHRS yönlendirme mesajı göster

---

## 🧪 FAZA 5 — Test

### 5A — Backend Testleri

- [ ] **T-05.1** `POST /api/analiz` endpoint'ini test et — geçerli semptom, doğru JSON dön
- [ ] **T-05.2** `POST /api/analiz` endpoint'ini boş semptomla test et — hata mesajı dönmeli
- [ ] **T-05.3** `POST /api/uzman-bul` endpoint'ini test et
- [x] **T-05.4** Gemini'nin her 4 aciliyet seviyesini dönebildiğini doğrula
- [ ] **T-05.5** Rate limiting'in çalıştığını test et

### 5B — Frontend Testleri

- [x] **T-05.6** Ana sayfadan → Semptom girişi → Triage sonucu akışını test et
- [x] **T-05.7** Ek bilgi formu boş bırakılarak analiz yapıldığında çalıştığını doğrula
- [ ] **T-05.8** Cinsiyet ve yaş alanlarının API'ye doğru iletildiğini doğrula
- [x] **T-05.9** Pusula özelliğinin (Smooth Scroll + otomatik form doldurma) çalıştığını doğrula
- [x] **T-05.10** "Konuma Göre" modunun doğru çalıştığını doğrula
- [x] **T-05.11** "Uzmanlığa Göre" modunun doğru çalıştığını doğrula
- [x] **T-05.12** Kurum Tercihi filtresinin API'ye iletildiğini doğrula
- [ ] **T-05.13** Yasal uyarı metninin göründüğünü doğrula

### 5C — Görsel ve Erişilebilirlik Testleri

- [ ] **T-05.14** Mobil ekranda (375px genişlik) uygulamanın düzgün göründüğünü kontrol et
- [ ] **T-05.15** Glassmorphism efektinin modern tarayıcılarda çalıştığını doğrula
- [x] **T-05.16** Kart animasyonunun akıcı göründüğünü kontrol et
- [ ] **T-05.17** Tüm butonların klavye (Tab) ile erişilebildiğini doğrula
- [ ] **T-05.18** Minimum 14px font boyutunun uygulandığını doğrula
- [x] **T-05.19** Her aciliyet seviyesinin hem renkle hem ikonla gösterildiğini kontrol et

---

## 🚀 FAZA 6 — Deploy (Yayınlama)

### 6A — Render.com Deploy

- [x] **T-06.1** [render.com](https://render.com) adresinde ücretsiz hesap aç
- [x] **T-06.2** GitHub repository'sini Render'a bağla
- [x] **T-06.3** "Web Service" oluştur — başlangıç komutu: `gunicorn features.app:app`
- [x] **T-06.4** Render'ın Environment Variables bölümüne `GEMINI_API_KEY` değerini ekle
- [x] **T-06.5** Deploy'un başarılı olduğunu ve Flask API'nin canlıda çalıştığını doğrula
- [x] **T-06.6** Canlı URL: `https://health-compass-qfnk.onrender.com`
- [x] **T-06.7** Canlı URL'yi `README.md` dosyasına ekle 

> **Not:** Render'ın ücretsiz katmanında sunucu 15 dakika hareketsiz kalırsa uyku moduna girer. İlk istek 30-60 saniye gecikebilir — bu normaldir.

---

## 🎬 FAZA 7 — Teslim Hazırlığı

- [x] **T-07.1** Demo videosu çek (Zoom / Loom / YouTube)
- [x] **T-07.2** Demo video linkini `README.md`'ye ekle
- [x] **T-07.3** Tüm zorunlu dosyaların mevcut olduğunu kontrol et ✅
- [x] **T-07.4** GitHub repository'sinin herkese açık (public) olduğunu doğrula
- [x] **T-07.5** `.env` dosyasının GitHub'a yüklenmediğini doğrula

---

## 📊 İlerleme Özeti

| Faz | Görev Sayısı | Tamamlanan |
|---|---|---|
| Faz 0 — Proje Kurulumu | 9 | 9 ✅ |
| Faz 1 — Backend | 16 | 16 ✅ |
| Faz 2 — Frontend (Tek Sayfa) | 30 | 30 ✅ |
| Faz 3 — CSS + Glassmorphism | 12 | 12 ✅ |
| Faz 4 — JavaScript + Pusula | 18 | 18 ✅ |
| Faz 5 — Test | 19 | 0 |
| Faz 6 — Deploy | 7 | 6 ✅ |
| Faz 7 — Teslim | 5 | 3 ✅ |
| **Toplam** | **116** | **94** |
