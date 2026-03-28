# ✅ Görev Listesi — Health Compass
> `prd.md` belgesinden türetilmiştir. Her görev bağımsız olarak tamamlanabilir.

**Durum İşaretleri:**
`[ ]` Yapılmadı &nbsp;|&nbsp; `[x]` Tamamlandı &nbsp;|&nbsp; `[~]` Devam ediyor

---

## 🗂️ FAZA 0 — Proje Kurulumu

> Geliştirmeye başlamadan önce tamamlanması gereken altyapı adımları.

- [ ] **T-00.1** GitHub'da `health-compass` adında yeni bir repository oluştur
- [ ] **T-00.2** Yerel bilgisayarda proje klasörünü oluştur ve GitHub'a bağla
- [ ] **T-00.3** Aşağıdaki klasör ve dosya yapısını oluştur:
  ```
  health-compass/
  ├── .env
  ├── .env.example
  ├── .gitignore
  ├── requirements.txt
  ├── gemini_service.py       # kök dizin (import uyumu için)
  ├── prompt_templates.py     # kök dizin (import uyumu için)
  └── features/
      ├── app.py              # Flask uygulaması buradan çalışır
      ├── gemini_service.py
      ├── prompt_templates.py
      ├── static/
      │   ├── css/style.css
      │   └── js/
      └── templates/
          └── index.html      # Tek sayfa — tüm akış burada
  ```
- [ ] **T-00.4** `.gitignore` dosyasına `.env` satırını ekle (API anahtarının GitHub'a yüklenmemesi için)
- [ ] **T-00.5** `requirements.txt` dosyasını oluştur ve şu paketleri yaz:
  ```
  flask==3.0.3
  google-generativeai==0.8.6
  python-dotenv==1.0.1
  flask-limiter==3.5.0
  requests==2.31.0
  gunicorn==21.2.0
  ```
- [ ] **T-00.6** Terminal'de `pip install -r requirements.txt` komutunu çalıştır
- [ ] **T-00.7** [aistudio.google.com](https://aistudio.google.com) adresinden Gemini API anahtarı al
- [ ] **T-00.8** `.env` dosyasına `GEMINI_API_KEY=aldigin_anahtar` satırını yaz
- [ ] **T-00.9** `README.md`, `idea.md`, `user-flow.md`, `tech-stack.md`, `prd.md` dosyalarını projeye ekle

---

## 🐍 FAZA 1 — Backend: Flask Sunucusu

> Python + Flask ile uygulamanın sunucu tarafı kurulur.

### 1A — Temel Flask Uygulaması

- [ ] **T-01.1** `app.py` dosyasında Flask uygulamasını başlat
- [ ] **T-01.2** Ana sayfa route'unu ekle: `GET /` → `index.html` döndür
- [ ] **T-01.3** `python features/app.py` komutuyla sunucunun `http://localhost:5000` adresinde çalıştığını doğrula

### 1B — Gemini API Entegrasyonu

- [ ] **T-01.4** `gemini_service.py` dosyasında Gemini API bağlantısını kur (`genai.configure`)
- [ ] **T-01.5** `gemini-1.5-flash` modelini seçerek model nesnesini oluştur
- [ ] **T-01.6** `semptomu_analiz_et(semptom, ek_bilgi)` fonksiyonunu yaz
- [ ] **T-01.7** `uzman_bul(uzman_turu, sehir)` fonksiyonunu yaz
- [ ] **T-01.8** Her iki fonksiyonun da Gemini'den dönen metni JSON olarak parse ettiğini doğrula

### 1C — Prompt Şablonları

- [ ] **T-01.9** `prompt_templates.py` dosyasında `TRIAGE_PROMPT` şablonunu yaz
  - Şablon şu alanları içermeli: `{semptom}`, `{yas}`, `{kronik}`, `{sure}`
  - Gemini'den yalnızca JSON döndürmesini iste
  - Beklenen JSON yapısı: `aciliyet`, `aciliyet_gerekce`, `uzman_turu`, `onerilen_adimlar`, `uyari`
- [ ] **T-01.10** `UZMAN_PROMPT` şablonunu yaz
  - Şablon şu alanları içermeli: `{uzman_turu}`, `{sehir}`
  - Beklenen JSON yapısı: `uzmanlar` listesi (ad, uzmanlik, kurum, sehir, randevu)

### 1D — API Endpoint'leri

- [ ] **T-01.11** `POST /api/analiz` endpoint'ini yaz
  - Gelen JSON'dan `semptom` ve `ek_bilgi` alanlarını al
  - `semptomu_analiz_et()` fonksiyonunu çağır
  - Sonucu JSON olarak döndür
- [ ] **T-01.12** `POST /api/uzman-bul` endpoint'ini yaz
  - Gelen JSON'dan `uzman_turu`, `sehir`, `tercih` alanlarını al
  - `uzman_bul()` fonksiyonunu çağır
  - Sonucu JSON olarak döndür

### 1E — Hata Yönetimi

- [ ] **T-01.13** Gemini API'den yanıt gelmezse (timeout) hata mesajı döndür
- [ ] **T-01.14** Geçersiz JSON yanıtı gelirse hata mesajı döndür
- [ ] **T-01.15** Boş semptom girişi gelirse hata mesajı döndür
- [ ] **T-01.16** `flask-limiter` ile rate limiting ekle (IP başına dakikada 10 istek)

---

## 🎨 FAZA 2 — Frontend: Tek Sayfa Uygulama (index.html)

> Tüm kullanıcı deneyimi **tek bir `index.html`** dosyasında yönetilir. Ayrı sayfa yok — JS ile bölümler gösterilip gizlenir.

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

### 2C — Ek Bilgi Formu Bölümü (aynı sayfada, accordion ile açılır)

- [x] **T-02.9** "▼ Ek Bilgi Ekle (Daha Doğru Sonuç İçin)" accordion başlığını ekle
- [x] **T-02.10** Yaş aralığı dropdown'ı ekle (0–15 / 16–25 / 26–45 / 46–65 / 65+)
- [x] **T-02.11** Cinsiyet dropdown'ı ekle (Belirtilmedi / Kadın / Erkek)
- [x] **T-02.12** Semptom süresi dropdown'ı ekle
- [x] **T-02.13** Kronik hastalık radio butonu ekle (Hayır / Evet / Bilmiyorum)

### 2D — Triage Sonuç Bölümü (inline — ayrı sayfa yok)

- [x] **T-02.14** Triage sonuç kartını semptom formunun hemen altında göster
- [x] **T-02.15** Aciliyet seviyesini büyük ikon + yazı ile göster (🚨 BUGÜN vb.)
- [x] **T-02.16** Aciliyet kartının rengini dinamik olarak ata (Kırmızı/Mavi/Yeşil)
- [x] **T-02.17** Aciliyet gerekçesi ve önerilen adımları göster
- [x] **T-02.18** "Önerilen Branş:" etiketiyle uzman türünü göster
- [x] **T-02.19** **"Bu Uzmanı Bul →"** butonunu ekle (Pusula özelliğini tetikler)
- [x] **T-02.20** Yasal uyarı metnini kartın altına ekle

### 2E — Uzman Arama Bölümü

- [x] **T-02.21** "Uzman & Sağlık Kuruluşu Ara" başlığını ekle
- [x] **T-02.22** Semptom serbest metin alanı ekle (isteğe bağlı)
- [x] **T-02.23** Arama türü radio: "📍 Konuma Göre" / "📋 Uzmanlığa Göre" ekle
- [x] **T-02.24** "📍 Konumumu Kullan" butonu ekle (tarayıcı konum izni ister)
- [x] **T-02.25** Şehir/bölge metin giriş alanı ekle
- [x] **T-02.26** Uzmanlık alanı metin giriş alanı ekle (Pusula'dan otomatik dolabilir)
- [x] **T-02.27** **Kurum Tercihi** radio: Kamu / Özel / Fark Etmez ekle
- [x] **T-02.28** "Ara" butonu ekle
- [x] **T-02.29** "Bulunan Uzmanlar" listesini dinamik render et
- [x] **T-02.30** Uzman bulunamazsa MHRS yönlendirme mesajı göster

---

## 🎨 FAZA 3 — Frontend: CSS Tasarımı

> Uygulamanın görsel tasarımı tamamlanır. Temel estetik: **Glassmorphism + Animasyonlar.**

- [ ] **T-03.1** `style.css` dosyasında CSS değişkenlerini (`:root`) tanımla:
  - Triage renkleri (ACİL `#DC2626`, BUGÜN `#2563EB`, EV TAKİBİ `#16A34A`)
  - Font ailesi: `IBM Plex Sans` (ana metin) + `Syne` (başlıklar)
  - Boşluk değişkenleri (8px, 16px, 32px, 64px)
- [ ] **T-03.2** Temel sayfa düzenini (layout) oluştur
- [ ] **T-03.3** Buton stillerini tasarla
- [ ] **T-03.4** Form elemanlarını (input, dropdown, radio) stillendir
- [ ] **T-03.5** **Glassmorphism kart stilini** yaz:
  ```css
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  ```
- [ ] **T-03.6** Kart giriş **animasyonunu** CSS ile yaz (`slideInDown`, `cubic-bezier`)
- [ ] **T-03.7** Triage sonuç kartını stillendir (Glassmorphism + renkli arka plan + büyük başlık)
- [ ] **T-03.8** Uzman listesi kartlarını stillendir
- [ ] **T-03.9** Yükleme animasyonunu CSS ile yaz (spinner veya pulse)
- [ ] **T-03.10** Responsive (mobil uyumlu) tasarımı ekle — tüm ekranlarda çalışsın
- [ ] **T-03.11** Minimum 14px font boyutunu tüm metinlerde kontrol et
- [ ] **T-03.12** Yasal uyarı metninin her sayfada görünür olduğunu doğrula

---

## ⚙️ FAZA 4 — Frontend: JavaScript

> Sayfa etkileşimleri ve API bağlantıları. Tüm JS tek sayfada çalışır.

### 4A — Genel Sayfa Yönetimi

- [x] **T-04.1** Bölümleri göster/gizle fonksiyonlarını yaz (ana sayfa ↔ semptom formu ↔ uzman arama)
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
- [x] **T-04.12** Triage'dan gelen `uzman_turu`'nu uzman formu uzmanlık alanına otomatik yaz

### 4D — Uzman Arama (3 Mod)

- [x] **T-04.13** Arama türü radio değişince (Konuma/Uzmanlığa Göre) ilgili form alanlarını göster/gizle
- [x] **T-04.14** "📍 Konumumu Kullan" butonuyla tarayıcı Geolocation API'sini kullan, şehri forma yaz
- [x] **T-04.15** Kurum Tercihi (Kamu/Özel/Fark Etmez) değerini form verisine ekle
- [x] **T-04.16** `POST /api/uzman-bul` endpoint'ine doğru parametrelerle gönder (`turkiye_geneli`, `konum_yakin`, `tercih`)
- [x] **T-04.17** Gelen uzman listesini kartlar halinde render et
- [x] **T-04.18** Uzman bulunamazsa MHRS yönlendirme mesajı göster

---

## 🧪 FAZA 5 — Test

> Her özelliğin doğru çalıştığı doğrulanır.

### 5A — Backend Testleri

- [ ] **T-05.1** `POST /api/analiz` endpoint'ini test et — geçerli semptom gir, doğru JSON dön
- [ ] **T-05.2** `POST /api/analiz` endpoint'ini boş semptomla test et — hata mesajı dönmeli
- [ ] **T-05.3** `POST /api/uzman-bul` endpoint'ini test et — şehir + uzman türü gir, liste dön
- [ ] **T-05.4** Gemini'nin her 4 aciliyet seviyesini de dönebildiğini doğrula (ACİL / BUGÜN / YARIN / EV_TAKİBİ)
- [ ] **T-05.5** Rate limiting'in çalıştığını test et (dakikada 10'dan fazla istek gönder)

### 5B — Frontend Testleri

- [ ] **T-05.6** Ana sayfadan → Semptom girişi → Triage sonucu akışını baştan sona test et
- [ ] **T-05.7** Ek bilgi formu tüm alanları boş bırakılarak analiz edildiğinde çalıştığını doğrula
- [ ] **T-05.8** Cinsiyet ve yaş alanlarının API'ye doğru iletildiğini doğrula
- [ ] **T-05.9** **"Bu Uzmanı Bul →"** butonunun Smooth Scroll'u ve otomatik form doldurmayı tetiklediğini doğrula
- [ ] **T-05.10** "Konuma Göre" modunda konum girildiğinde doğru uzmanların listelendiğini doğrula
- [ ] **T-05.11** "Uzmanlığa Göre" modunda uzmanlık alanı girildiğinde doğru uzmanların listelendiğini doğrula
- [ ] **T-05.12** Kurum Tercihi (Kamu/Özel/Fark Etmez) filtresinin API'ye iletildiğini doğrula
- [ ] **T-05.13** Yasal uyarı metninin triage sonuç kartında göründüğünü doğrula

### 5C — Görsel ve Erişilebilirlik Testleri

- [ ] **T-05.11** Mobil ekranda (375px genişlik) uygulamanın düzgün göründüğünü kontrol et
- [ ] **T-05.12** Glassmorphism efektinin (`backdrop-filter: blur`) modern tarayıcılarda çalıştığını doğrula
- [ ] **T-05.13** Kart animasyonunun (slideInDown) akıcı göründüğünü kontrol et
- [ ] **T-05.14** Tüm butonların klavye (Tab) ile erişilebildiğini doğrula
- [ ] **T-05.15** Minimum 14px font boyutunun tüm metinlerde uygulandığını doğrula
- [ ] **T-05.16** Her aciliyet seviyesinin hem renkle hem ikonla gösterildiğini kontrol et

---

## 🚀 FAZA 6 — Deploy (Yayınlama)

> Uygulama internete alınır.

### 6A — Backend Deploy (Render.com)

- [ ] **T-06.1** [render.com](https://render.com) adresinde ücretsiz hesap aç
- [ ] **T-06.2** GitHub repository'sini Render'a bağla
- [ ] **T-06.3** "Web Service" oluştur, başlangıç komutu olarak `gunicorn features.app:app` gir
- [ ] **T-06.4** Render'ın Environment Variables bölümüne `GEMINI_API_KEY` değerini ekle
- [ ] **T-06.5** Deploy'un başarılı olduğunu ve Flask API'nin canlıda çalıştığını doğrula
- [ ] **T-06.6** Canlı URL'yi not al (örn: `https://health-compass.onrender.com`)

### 6B — Frontend Deploy (Netlify)

- [ ] **T-06.7** [netlify.com](https://netlify.com) adresinde ücretsiz hesap aç
- [ ] **T-06.8** GitHub repository'sini Netlify'a bağla
- [ ] **T-06.9** `features/` klasörünü yayınlama dizini olarak ayarla
- [ ] **T-06.10** Deploy'un başarılı olduğunu ve ana sayfanın açıldığını doğrula
- [ ] **T-06.11** Frontend'deki API çağrılarının Render URL'sine işaret ettiğini doğrula
- [ ] **T-06.12** Canlı URL'yi `README.md` dosyasına ekle

---

## 🎬 FAZA 7 — Teslim Hazırlığı

> Buildathon teslimi için gerekli son adımlar.

- [ ] **T-07.1** Uygulamanın canlı linkini (`yayin-linki`) `README.md`'ye ekle
- [ ] **T-07.2** Demo videosu çek (Loom veya YouTube) — uygulamanın baştan sona kullanımını göster
- [ ] **T-07.3** Demo video linkini `README.md`'ye ekle
- [ ] **T-07.4** Tüm zorunlu dosyaların mevcut olduğunu kontrol et:
  - [ ] `README.md` ✅
  - [ ] `idea.md` ✅
  - [ ] `user-flow.md` ✅
  - [ ] `tech-stack.md` ✅
  - [ ] `prd.md` ✅
  - [ ] `features/` klasörü (kaynak kodlar)
- [ ] **T-07.5** GitHub repository'sinin herkese açık (public) olduğunu doğrula
- [ ] **T-07.6** `.env` dosyasının GitHub'a yüklenmediğini doğrula (`.gitignore` kontrolü)

---

## 📊 İlerleme Özeti

| Faz | Görev Sayısı | Tamamlanan |
|---|---|---|
| Faz 0 — Proje Kurulumu | 9 | 9 ✅ |
| Faz 1 — Backend | 16 | 16 ✅ |
| Faz 2 — Frontend (Tek Sayfa) | 30 | 30 ✅ |
| Faz 3 — CSS + Glassmorphism | 12 | 12 ✅ |
| Faz 4 — JavaScript + Pusula | 18 | 18 ✅ |
| Faz 5 — Test | 16 | 5 🔄 |
| Faz 6 — Deploy | 12 | 0 |
| Faz 7 — Teslim | 10 | 0 |
| **Toplam** | **123** | **90** |
