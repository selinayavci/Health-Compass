# 🧭 Health Compass

> **Yapay Zeka Destekli Kişisel Sağlık Pusulanız.**

---

## 🔗 Bağlantılar

| | Link |
|---|---|
| 🌐 **Yayın Linki** | [health-compass-qfnk.onrender.com](https://health-compass-qfnk.onrender.com) |
| 🎥 **Demo Videosu** | [Demo Videosu](https://youtu.be/Vd1AhjDMEiE) |
---

## 📌 Proje Hakkında

**Health Compass**, bireylerin sağlık semptomlarını değerlendirmelerine ve doğru uzmana ulaşmalarına yardımcı olan yapay zeka destekli bir web uygulamasıdır. UpSchool bünyesindeki "Birbirini Geliştiren Kadınlar" programı kapsamındaki AI Buildathon için geliştirilmiştir.

### Çözülen Problem

Türkiye'de ve dünyada milyonlarca insan iki kritik sorunla karşı karşıyadır:

1. **Aciliyet Belirsizliği:** Semptomların ne kadar acil olduğunu bilememe — insanlar gereksiz yere acil servisleri meşgul ediyor ya da gerçekten acil vakaları hafife alıyor.
2. **Uzmanlık Eşitsizliği:** Özellikle karmaşık vakalarda doğru ve deneyimli uzmana nasıl ulaşılacağını bilememe. Doğru bilgiye erişim hâlâ büyük ölçüde kişisel ilişkilere veya şansa bağlı.

### Çözüm

Health Compass, kullanıcıya **4 adımlı kesintisiz bir deneyim** sunar:

| Adım | Ne Olur? |
|---|---|
| 1️⃣ **Giriş** | Glassmorphism arayüzüyle karşılama |
| 2️⃣ **Analiz** | Semptomlar Gemini 2.5 Flash ile işlenir |
| 3️⃣ **Sonuç** | Renk kodlu triage kartı (🔴 ACİL / 🟡 BUGÜN / 🟢 EV TAKİBİ) |
| 4️⃣ **Aksiyon** | "Bu Uzmanı Bul" → Smooth Scroll + Otomatik Form Doldurma (Pusula) |

### Öne Çıkan Özellikler

- 🤖 **Gemini 2.5 Flash** — Türkçe semptom analizi ve garantili JSON yapılandırma
- 🔄 **Akıllı Fallback** — 2.5 → 2.0 → 1.5 model zinciri; 429 kota hatasında akıllı atlama
- 🏥 **3 Uzman Arama Modu** — Şehir bazlı / Türkiye geneli / En yakın kurum
- ⚖️ **Kurum Tercihi** — Kamu / Özel / Fark Etmez filtresi
- 🧭 **Pusula Özelliği** — Triage'dan uzman formuna sıfır sürtünmeli geçiş
- 🛡️ **Rate Limiting** — 200 istek/gün, 10 istek/dakika güvenlik sınırı

---

## 🛠️ Teknoloji Yığını

| Katman | Teknoloji |
|---|---|
| AI | Google Gemini 2.5 Flash (+ 2.0 / 1.5 fallback) |
| Backend | Python 3.11 + Flask 3.x |
| Frontend | HTML5 + CSS3 (Glassmorphism) + Vanilla JS |
| Deploy | Render.com (backend + frontend) |

---

## 🚀 Kurulum (Installation)

### Gereksinimler

- Python 3.9+
- Modern bir web tarayıcısı (Chrome, Firefox, Safari)
- Gemini API anahtarı — [aistudio.google.com](https://aistudio.google.com) adresinden **ücretsiz** alınabilir

### Adımlar

**1.** Projeyi klonlayın:
```bash
git clone https://github.com/selinayavci/health-compass.git
cd health-compass
```

**2.** `.env` dosyası oluşturun ve API anahtarınızı ekleyin:
```bash
echo "GEMINI_API_KEY=buraya_api_anahtarinizi_yazin" > .env
```

**3.** Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

**4.** Uygulamayı başlatın:
```bash
python features/app.py
```

Tarayıcınızda `http://localhost:5000` adresini açın.

---

## 📁 Proje Yapısı

```
health-compass/
├── features/
│   ├── app.py                  # Flask sunucu ve API endpoint'leri
│   ├── gemini_service.py       # Gemini entegrasyonu + fallback yönetimi
│   ├── prompt_templates.py     # AI prompt şablonları (Triage + 3 Uzman modu)
│   ├── static/
│   │   ├── css/style.css       # Glassmorphism tasarım
│   │   └── js/                 # Vanilla JS (Smooth Scroll, Pusula)
│   └── templates/
│       └── index.html          # Tek sayfalık uygulama
├── .env.example                # API anahtarı örnek şablonu
├── .gitignore
├── requirements.txt
├── README.md
├── idea.md
├── user-flow.md
├── prd.md
├── tasks.md
└── tech-stack.md
```

---

## 📄 Dokümantasyon

| Dosya | İçerik |
|---|---|
| [`idea.md`](idea.md) | Problem tanımı, kullanıcı profili, AI'ın rolü |
| [`user-flow.md`](user-flow.md) | 4 adımlı kullanıcı akışı ve Pusula özelliği |
| [`tech-stack.md`](tech-stack.md) | Teknoloji kararları ve gerekçeleri |
| [`prd.md`](prd.md) | Ürün gereksinimleri dokümanı |
| [`tasks.md`](tasks.md) | Görev listesi ve ilerleme durumu |

---

## 👤 Geliştirici

**Selinay AVCI**
AI Buildathon 2025 — UpSchool "Birbirini Geliştiren Kadınlar" Programı Mezunu

---

## ⚠️ Yasal Uyarı

Health Compass bir tıbbi tanı aracı **değildir**. Sunulan bilgiler yalnızca genel yönlendirme amaçlıdır. Sağlık kararlarınız için mutlaka bir sağlık profesyoneliyle görüşünüz.
