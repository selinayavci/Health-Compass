# 🛠️ Teknoloji Yığını: Health Compass

## Mimari Karar: Neden Bu Yapı?

Health Compass için **hafif, hızlı geliştirilebilir ve deploy edilmesi kolay** bir mimari seçilmiştir.

Proje iki katmandan oluşur:

```
[KULLANICI TARAYICISI]
        |
        | HTTP İstekleri (JSON)
        v
[BACKEND — Python + Flask]
        |
        | API Çağrısı
        v
[GOOGLE GEMİNİ API]
```

Neden karmaşık bir mimari (mikroservis, veritabanı, authentication vb.) tercih edilmedi?

- Proje, tek bir görev odaklıdır: semptom al → analiz et → göster
- Kullanıcı verisi saklanmayacak → veritabanı gerekmez
- Hız ve basitlik, maintainability açısından en uygun seçimdir
- Bireysel buildathon projesinde aşırı karmaşıklık zaman kaybıdır

---

## 1. Frontend — Kullanıcının Gördüğü Katman

### Teknoloji: Vanilla JS + Modern CSS3 (Glassmorphism & Animasyonlar)

**React, Vue, Angular gibi framework'ler neden seçilmedi?**

| Kriter | Framework (React vb.) | Vanilla JS |
|---|---|---|
| Öğrenme eğrisi | Yüksek | Düşük |
| Kurulum karmaşıklığı | `npm`, `node_modules`, build süreci gerektirir | Hiçbir şey gerekmez |
| Deploy kolaylığı | Build adımı zorunlu | HTML dosyasını direkt yükle |
| Smooth Scroll kontrolü | Framework overhead'i var | ✅ `window.scrollTo` ile tam kontrol |
| DOM manipülasyonu | Virtual DOM — bu proje için gereksiz | ✅ Direkt ve hızlı |
| Render.com uyumu | Ek yapılandırma gerekir | ✅ Direkt çalışır |

**Vanilla JS'in bu projede üstlendiği kritik görevler:**
- **Smooth Scroll:** "Bu Uzmanı Bul" butonuyla uzman formuna animasyonlu kaydırma (`window.scrollTo({ behavior: 'smooth' })`)
- **Otomatik Form Doldurma (Pusula):** Triage sonucundan gelen `uzman_turu` verisini uzman arama formuna DOM manipülasyonuyla otomatik yaz
- **Dinamik Kart Render:** Gemini'den gelen JSON verisini triage kartı ve uzman listesi olarak ekrana bas
- **Glassmorphism Animasyonlar:** CSS sınıflarını JS ile toggle ederek giriş/çıkış animasyonlarını yönet

### Frontend Dosya Yapısı

```
features/
├── static/
│   ├── css/
│   │   └── style.css          # Tüm görsel tasarım
│   └── js/
│       └── (JS dosyaları)
└── templates/
    └── index.html             # Tek sayfalık uygulama (SPA benzeri — JS ile bölümler gösterilip gizlenir)
```

### CSS Yaklaşımı: Modern CSS3 + Glassmorphism

Framework kullanılmaz (Bootstrap, Tailwind vb. tercih edilmez). El yazısı CSS ile iki temel tasarım dili uygulanır:

**Glassmorphism Efekti** — Karşılama ekranı ve kart bileşenlerinde:
```css
.glass-card {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
}
```

**Animasyonlar** — Kart geçişleri ve yükleme efektleri:
```css
.kart-giris {
  animation: slideInDown 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideInDown {
  from { opacity: 0; transform: translateY(-20px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

CSS değişkenleri (`:root`) ile tutarlı renk ve tipografi sistemi kurulur:

```css
:root {
  /* Renk Sistemi — Triage Seviyeleri */
  --renk-acil: #DC2626;         /* Kırmızı — ACİL */
  --renk-bugun: #D97706;        /* Turuncu — BUGÜN */
  --renk-bekleyebilir: #2563EB; /* Mavi — YARINa bırakılabilir */
  --renk-ev-takibi: #16A34A;    /* Yeşil — EV TAKİBİ */

  /* Tipografi */
  --yazi-ana: 'IBM Plex Sans', sans-serif;  /* Tıbbi/profesyonel his */
  --yazi-baslik: 'Syne', sans-serif;        /* Modern, güçlü başlıklar */

  /* Aralıklar */
  --bosluk-s: 8px;
  --bosluk-m: 16px;
  --bosluk-l: 32px;
  --bosluk-xl: 64px;
}
```

### JavaScript Yaklaşımı

Vanilla JS ile yapılacaklar:

```javascript
// 1. Sayfa geçişleri (SPA benzeri davranış — sayfa yenilemeden geçiş)
function sayfayiGoster(sayfaId) { ... }

// 2. Semptom formunu Flask backend'e gönderme
async function semptomuGonder(semptomMetni) {
  const yanit = await fetch('/api/analiz', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ semptom: semptomMetni })
  });
  const veri = await yanit.json();
  triageSonucunuGoster(veri);
}

// 3. Triage sonucunu dinamik olarak ekrana yaz
function triageSonucunuGoster(veri) {
  document.getElementById('aciliyet-seviyesi').textContent = veri.aciliyet;
  // ...
}
```

---

## 2. Backend — Sunucu Katmanı

### Teknoloji: Python & Flask

**Neden Python?**

- Google Gemini API'nin en olgunlaşmış resmi kütüphanesi Python için mevcuttur (`google-generativeai`)
- Yapay zeka / ML ekosisteminin dili Python'dur — ileride genişletme kolaylaşır
- Sözdizimi sade ve okunabilirdir

**Neden Flask ve FastAPI değil?**

| Kriter | Flask | FastAPI |
|---|---|---|
| Öğrenme eğrisi | Çok düşük | Orta |
| Kurulum | `pip install flask` | Ek bağımlılıklar gerekir |
| Bu proje için yeterlilik | ✅ Tam yeterli | Fazla güçlü (overkill) |
| Dokümantasyon | Çok zengin, Türkçe kaynak bol | İngilizce ağırlıklı |
| Asenkron destek | Temel düzeyde | Güçlü — ama bu projede kritik değil |

Flask, bu projenin ihtiyaçları için mükemmeldir. FastAPI'nin asenkron ve otomatik dokümantasyon avantajları Health Compass'ın kapsamında anlamsız karmaşıklık yaratır.

### Backend Dosya Yapısı

```
health-compass/
├── features/
│   ├── app.py              # Flask uygulamasının kalbi — tüm route'lar burada
│   ├── gemini_service.py   # Gemini API ile konuşan modül
│   └── prompt_templates.py # AI'a gönderilen prompt şablonları
├── gemini_service.py       # Kök dizinde de mevcut (import uyumluluğu için)
├── prompt_templates.py     # Kök dizinde de mevcut
├── requirements.txt        # Bağımlılıklar
└── .env                    # API anahtarı (Git'e yüklenmez!)
```

### `app.py` — Flask Route Tasarımı

```python
from flask import Flask, request, jsonify, render_template
from gemini_service import semptomu_analiz_et, uzman_bul

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def anasayfa():
    return render_template('index.html')

# Semptom analizi endpoint'i
@app.route('/api/analiz', methods=['POST'])
def semptomu_analiz_et_endpoint():
    veri = request.get_json()
    semptom = veri.get('semptom', '')
    ek_bilgi = veri.get('ek_bilgi', {})
    sonuc = semptomu_analiz_et(semptom, ek_bilgi)
    return jsonify(sonuc)

# Uzman bulma endpoint'i
@app.route('/api/uzman-bul', methods=['POST'])
def uzman_bul_endpoint():
    veri = request.get_json()
    uzman_turu = veri.get('uzman_turu')
    sehir = veri.get('sehir')
    uzmanlar = uzman_bul(uzman_turu, sehir)
    return jsonify(uzmanlar)
```

### `gemini_service.py` — AI Entegrasyon Modülü

```python
import google.generativeai as genai
import os, json
from prompt_templates import TRIAGE_PROMPT, UZMAN_PROMPT

genai.configure(api_key=os.environ['GEMINI_API_KEY'])
# Model öncelik sırası: gemini-2.5-flash → 2.0-flash → 1.5-flash (fallback)
GEMINI_PRIMARY_MODEL   = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_FALLBACK_MODELS = ["gemini-2.0-flash", "gemini-1.5-flash"]
model = genai.GenerativeModel(GEMINI_PRIMARY_MODEL)

def semptomu_analiz_et(semptom: str, ek_bilgi: dict) -> dict:
    prompt = TRIAGE_PROMPT.format(
        semptom=semptom,
        yas=ek_bilgi.get('yas', 'Belirtilmedi'),
        kronik=ek_bilgi.get('kronik_hastalik', 'Hayır'),
        sure=ek_bilgi.get('semptom_suresi', 'Belirtilmedi')
    )
    yanit = model.generate_content(prompt)
    return json.loads(yanit.text)

def uzman_bul(uzman_turu: str, sehir: str) -> dict:
    prompt = UZMAN_PROMPT.format(uzman_turu=uzman_turu, sehir=sehir)
    yanit = model.generate_content(prompt)
    return json.loads(yanit.text)
```

### `prompt_templates.py` — AI Prompt Tasarımı

Bu dosya, Gemini'ye ne söyleneceğini belirler. Prompt kalitesi = uygulama kalitesi.

---

## 3. Yapay Zeka Katmanı

### Teknoloji: Google Gemini 2.5 Flash — Hızlı Analiz, JSON Yapılandırma ve Akıllı Fallback

**Neden Gemini ve OpenAI (ChatGPT) değil?**

| Kriter | Gemini 2.5 Flash | GPT-4o Mini |
|---|---|---|
| Türkçe anlama kalitesi | ✅ Çok güçlü | İyi |
| Ücretsiz kullanım kotası | ✅ Yüksek (buildathon için ideal) | Sınırlı |
| Yanıt hızı | ✅ Çok hızlı | Orta |
| JSON çıktı güvenilirliği | ✅ `response_mime_type` ile garantili | Değişken |
| Fallback model ekosistemi | ✅ 2.5 → 2.0 → 1.5 zinciri | Sınırlı |

**Neden "Flash" modeli, "Pro" değil?**

- Flash, Pro'dan çok daha hızlı yanıt verir
- Maliyet açısından çok daha ekonomiktir
- Triage yönlendirme görevi için Flash'ın kapasitesi fazlasıyla yeterlidir
- Pro modeli; akademik makale analizi, çok adımlı karmaşık akıl yürütme gibi görevler için gereklidir

**Akıllı Fallback ve 429 Kota Yönetimi:**

```
Gemini 2.5 Flash (birincil)
    ↓ timeout / geçici hata
Gemini 2.0 Flash (birinci yedek)
    ↓ timeout / geçici hata
Gemini 1.5 Flash (ikinci yedek)
    ↓ 429 Kota Hatası (herhangi bir adımda)
Fallback ATLANIR → Kullanıcıya bilgilendirici mesaj
```

> 429 hatasında fallback atlanmasının sebebi: tüm Gemini modelleri aynı Google Cloud proje kotasını paylaşır. Kota dolduğunda sıradaki modele istek atmak boşa gider ve ek kota tüketir. Bu mekanizma, kaynakların verimli kullanılmasını sağlar.

---

## 4. Deployment (Yayınlama) — Render.com (Tek Platform)

### Neden Lovable veya Netlify değil?

Buildathon brief'inde Lovable ve Netlify örnek platform olarak verilmiştir. Ancak bu platformlar **yalnızca statik frontend** barındırabilir. Health Compass'ın mimarisi Python/Flask tabanlı bir backend içerdiğinden bu platformlar tek başına yeterli değildir:

| Platform | Desteklediği | Desteklemediği |
|---|---|---|
| Lovable | React tabanlı statik siteler | Python/Flask backend |
| Netlify | Statik HTML/JS/CSS | Python/Flask backend (sunucu tarafı kod) |
| **Render.com** | ✅ Python/Flask uygulamaları | — |

Bu nedenle **hem backend hem frontend Render.com üzerinden** yayınlanmaktadır. Flask uygulaması hem API endpoint'lerini hem de `index.html` arayüzünü aynı sunucudan sunar — ayrı bir frontend hosting'e gerek kalmaz.

| Katman | Platform | Görevi |
|---|---|---|
| **Backend + Frontend** | Render.com | Flask hem API'yi hem HTML arayüzünü sunar |

```
Kullanıcı → https://health-compass-qfnk.onrender.com
                  |
            Flask uygulaması
            ├── GET /               → index.html (arayüz)
            ├── POST /api/analiz    → Gemini analizi
            └── POST /api/uzman-bul → Uzman listesi
                  |
            Gemini 2.5 Flash API
```

### Deploy Adımları

```
GitHub'a push et → Render otomatik deploy eder → Uygulama canlıda
```

- Ücretsiz katman mevcut (750 saat/ay — buildathon için yeterli)
- `GEMINI_API_KEY` Environment Variables bölümüne eklenir, kaynak koda yazılmaz
- Başlatma komutu: `gunicorn features.app:app`

**Canlı Link:**
```
https://health-compass-qfnk.onrender.com
```

> **Not:** Render'ın ücretsiz katmanında sunucu 15 dakika hareketsiz kalırsa uyku moduna girer. İlk istek 30-60 saniye gecikebilir — bu normaldir.

---

## 5. Geliştirme Ortamı

### Gerekli Kurulumlar

```bash
# 1. Python kontrolü
python --version   # 3.9+ olmalı

# 2. Bağımlılıkları yükle
pip install -r requirements.txt

# 3. API anahtarını ayarla (.env dosyası oluştur)
echo "GEMINI_API_KEY=buraya_anahtarini_yaz" > .env

# 4. Uygulamayı başlat
python features/app.py

# Tarayıcıda aç: http://localhost:5000
```

### `requirements.txt`

```
flask==3.0.3
google-generativeai==0.8.6
python-dotenv==1.0.1
flask-limiter==3.5.0
requests==2.31.0
gunicorn==21.2.0
flask-cors==4.0.0
```

> `google-generativeai==0.8.6` — Gemini 2.5 Flash'ı destekleyen minimum versiyon.
> `gunicorn` — Production deploy için gerekli WSGI sunucusu.
> `flask-cors==4.0.0` — Cross-Origin Resource Sharing desteği.

---

## 6. Güvenlik Kararları

| Risk | Çözüm |
|---|---|
| API anahtarının sızması | `.env` dosyasına saklanır, `.gitignore`'a eklenir — asla kaynak koduna yazılmaz |
| Kullanıcı verisi gizliliği | Hiçbir semptom verisi veritabanına kaydedilmez |
| Yanlış tıbbi bilgi riski | Her yanıtta zorunlu uyarı: *"Bu uygulama tıbbi tanı koymaz"* |
| Kötüye kullanım (spam) | Flask'ta rate limiting — günde 200, dakikada 10 istek (flask-limiter) |

---

## Özet Tablo

| Katman | Teknoloji | Görev |
|---|---|---|
| AI Modeli (Birincil) | Google Gemini 2.5 Flash | Hızlı semptom analizi ve garantili JSON yapılandırma |
| AI Modeli (Yedek) | Gemini 2.0 Flash → 1.5 Flash | Birincil modelin hata vermesi durumunda devreye girer |
| Kota Yönetimi | Akıllı 429 Fallback | Kota hatasında gereksiz istek atılmaz |
| Frontend | Vanilla JS | Smooth Scroll ve DOM manipülasyonu (Pusula özelliği) |
| Frontend | Modern CSS3 | Glassmorphism efektleri ve kart animasyonları |
| Backend | Python & Flask | Sunucu, API endpoint'leri, Gemini entegrasyonu |
| Güvenlik | flask-limiter | Rate limiting (200/gün, 10/dakika) |
| CORS | flask-cors | Cross-origin istek desteği |
| Frontend + Backend Deploy | Render.com | Tek platform, ücretsiz, gunicorn ile |
| Ortam Yönetimi | python-dotenv | API anahtarı güvenliği, çoklu yol desteği |
