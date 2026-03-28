# 📋 Ürün Gereksinim Belgesi (PRD)
# Health Compass

| Alan | Bilgi |
|---|---|
| **Ürün Adı** | Health Compass |
| **Belge Versiyonu** | v1.1 |
| **Tarih** | Mart 2025 |
| **Kapsam** | AI Buildathon — MVP |
| **Durum** | Taslak |

---

## 1. Ürün Vizyonu

### 1.1 Misyon

Health Compass, yapay zeka destekli semptom analizi ve uzman hekim yönlendirmesi aracılığıyla sağlık hizmetlerine erişimdeki bilgi boşluğunu kapatmayı hedefleyen bir mini web uygulamasıdır. YGA'nın sosyal fayda misyonu ve UpSchool'un kapsayıcılık ilkelerinden ilham alınarak geliştirilmiştir.

### 1.2 Vizyon Cümlesi

> "Herkes, nerede yaşadığından veya sosyal çevresinden bağımsız olarak, sağlıkla ilgili kararlarında doğru yönlendirmeye anında erişebilmelidir."

### 1.3 Temel Değer Önerisi

**"Yapay Zeka Destekli Kişisel Sağlık Pusulanız."**

Health Compass, piyasadaki genel semptom kontrol uygulamalarından farklı olarak **"ne hastalığın var?"** sorusuna değil, **"şimdi ne yapmalısın?"** sorusuna yanıt verir. Üstelik bununla kalmaz: **Pusula özelliğiyle** kullanıcıyı uygulama içindeki uzman arama formuna otomatik yönlendirir ve alanları doldurur. Bu yaklaşım uygulamayı bir tıbbi bilgi bankası değil, uçtan uca bir karar rehberi haline getirir.

---

## 2. Problem Tanımı

### 2.1 Sorun 1 — Aciliyet Belirsizliği (Triage Boşluğu)

Bireyler günlük semptomlar karşısında durumun aciliyetini doğru değerlendirememektedir. İnsanlar ne kadar acil olduğunu bilmedikleri için acil servisleri gereksiz meşgul ediyor. Bu durum hem bireysel sağlık riskine hem de sistemik kaynak israfına yol açmaktadır. Bu belirsizlik iki kritik sonuç doğurur:

- **Aşırı başvuru:** Acil olmayan vakalar acil servislere yığılır, gerçek acil hastalara müdahale gecikmesi yaşanır.
- **Geç başvuru:** Gerçekten acil olan vakalar hafife alınır ve ciddi sağlık kayıplarına yol açar.

### 2.2 Sorun 2 — Uzmanlık Eşitsizliği (Yönlendirme Boşluğu)

Karmaşık ya da nadir bir hastalık söz konusu olduğunda bireyler ilgili alanda deneyimli uzmana nasıl ulaşacaklarını bilememektedir. Doğru uzmana erişim büyük ölçüde kişisel ilişkilere veya şansa bağlıdır; bu durum sosyoekonomik eşitsizliği derinleştirir.

### 2.3 Etkilenen Kullanıcı Grupları

| Grup | Sorun |
|---|---|
| Şehir merkezindeki ortalama birey | Hangi semptomu ciddiye alacağını bilemiyor |
| Kırsal/küçük şehir sakini | Uzmana ulaşma yolunu bilemiyor |
| Hasta yakını | Sevdiklerini doğru yönlendiremiyor |
| Yurtdışındaki Türk vatandaşı | Türkiye sağlık sistemine yabancı |

---

## 3. Hedef Kullanıcılar

### 3.1 Birincil Kullanıcı (Primary Persona)

**"Kaygılı Aile Ferdi"**

- Yaş aralığı: 25–55
- Dijital araçlara temel düzeyde erişimi olan
- Semptom yaşayan ya da hasta yakını olan
- Tıbbi konularda profesyonel yönlendirmeden yoksun
- Acil mi değil mi kararını vermekte zorlanan herkes

### 3.2 İkincil Kullanıcı (Secondary Persona)

**"Uzak Şehirdeki Hasta"**

- Küçük şehir veya kırsal alanda yaşayan
- İlgili uzmana şehrinde ulaşamayan
- Hangi şehre, hangi hastaneye gideceğini bilemeyen

---

## 4. Ürün Kapsamı (Scope)

### 4.1 MVP Kapsamında OLAN Özellikler

| # | Özellik | Açıklama | Öncelik |
|---|---|---|---|
| F-01 | Semptom Girişi | Kullanıcı semptomlarını yazılı olarak girer | 🔴 Zorunlu |
| F-02 | Ek Bilgi Formu | Yaş, cinsiyet, kronik hastalık, semptom süresi | 🔴 Zorunlu |
| F-03 | AI Triage Analizi | Gemini 2.5 Flash ile aciliyet seviyesi ve JSON yapılandırma | 🔴 Zorunlu |
| F-04 | Triage Sonuç Kartı | Glassmorphism + renk kodlu (Kırmızı/Mavi/Yeşil) aciliyet kartı | 🔴 Zorunlu |
| F-05 | Uzman Yönlendirme | Uzmanlık alanı önerisi | 🔴 Zorunlu |
| F-06 | Uzman Arama | Konuma Göre / Uzmanlığa Göre / Türkiye Geneli — 3 arama modu | 🔴 Zorunlu |
| F-07 | Yasal Uyarı | Her sonuçta "tanı değildir" uyarısı | 🔴 Zorunlu |
| F-08 | Pusula Özelliği | "Bu Uzmanı Bul" ile Smooth Scroll + otomatik form doldurma | 🔴 Zorunlu |

### 4.2 MVP Kapsamında OLMAYAN Özellikler

| Özellik | Gerekçe |
|---|---|
| Kullanıcı hesabı / giriş sistemi | Kapsam dışı, veri saklanmayacak |
| Randevu alma entegrasyonu | MHRS API entegrasyonu zaman alır |
| Sesli giriş | Opsiyonel — ileriki versiyona bırakıldı |
| Çoklu dil desteği | MVP tek dil (Türkçe) |
| Mobil uygulama (iOS/Android) | Web uygulaması öncelikli |
| Tıbbi görüntü analizi | Kapsam dışı |

---

## 5. Fonksiyonel Gereksinimler

### 5.1 F-01 — Semptom Girişi

**Açıklama:** Kullanıcı yaşadığı semptomları serbest metin olarak sisteme girer.

**Kabul Kriterleri:**
- Metin alanı minimum 10, maksimum 1000 karakter kabul eder
- Boş form gönderildiğinde uyarı mesajı gösterilir
- Giriş alanı Türkçe karakter destekler
- Kullanıcı "Analiz Et" butonuna tıkladığında F-02'ye geçilir

### 5.2 F-02 — Ek Bilgi Formu

**Açıklama:** Triage kalitesini artırmak için kısa bir ek bilgi formu sunulur. Tüm bu alanlar semptom giriş ekranıyla aynı sayfada (single-page) yer alır — ayrı bir sayfa açılmaz.

**Alanlar:**

| Alan | Tip | Seçenekler | Zorunlu mu? |
|---|---|---|---|
| Yaş aralığı | Dropdown | 0–15 / 16–25 / 26–45 / 46–65 / 65+ | Hayır |
| Cinsiyet | Dropdown | Kadın / Erkek / Belirtilmedi | Hayır |
| Semptom süresi | Dropdown | Bugün / 2–3 gündür / 1 haftadan fazla | Hayır |
| Kronik hastalık | Radio | Hayır / Evet / Bilmiyorum | Hayır |

**Kabul Kriterleri:**
- Form atlanabilir; tüm alanlar boş bırakılırsa "Belirtilmedi" olarak API'ye iletilir
- Doldurulan alanlar Gemini prompt'una eklenerek triage doğruluğu artırılır
- Cinsiyet bilgisi özellikle kadın sağlığı (gebelik şüphesi vb.) senaryolarında triage kalitesini yükseltir

### 5.3 F-03 — AI Triage Analizi

**Açıklama:** Kullanıcı girdisi Gemini API'ye gönderilir, yapılandırılmış JSON yanıt alınır.

**Sistem Davranışı:**
- İstek gönderildiğinde yükleme animasyonu gösterilir
- Gemini'den yanıt 10 saniye içinde gelmezse hata mesajı gösterilir
- Yanıt JSON formatında parse edilir

**Gemini'ye Gönderilen Veri Yapısı:**
```
semptom: [kullanıcı metni]
yas: [seçilen aralık veya "Belirtilmedi"]
kronik_hastalik: [Evet/Hayır/Belirtilmedi]
semptom_suresi: [seçilen süre veya "Belirtilmedi"]
```

**Gemini'den Beklenen Yanıt Yapısı:**
```json
{
  "aciliyet": "ACİL | BUGÜN | YARIN | EV_TAKİBİ",
  "aciliyet_gerekce": "string",
  "uzman_turu": "string",
  "onerilen_adimlar": ["string"],
  "uyari": "string"
}
```

### 5.4 F-04 — Triage Sonuç Kartı

**Açıklama:** Analiz sonucu kullanıcıya Glassmorphism tasarımlı, renk kodlu kart olarak sunulur.

**Tasarım:** Kartlar `backdrop-filter: blur(12px)` efektiyle yarı saydam görünür. CSS animasyonuyla yukarıdan aşağıya süzülerek ekrana gelir.

**Aciliyet Seviyeleri:**

| Seviye | Renk | Mesaj | Kullanıcı Aksiyonu |
|---|---|---|---|
| 🔴 ACİL | #DC2626 Kırmızı | "Hemen Acil Servise Gidin" | "Bu Uzmanı Bul" butonu → Smooth Scroll + Otomatik Form |
| 🟡 BUGÜN | #2563EB Mavi | "Aynı Gün Doktora Başvurun" | "Bu Uzmanı Bul" butonu → Smooth Scroll + Otomatik Form |
| 🟢 EV TAKİBİ | #16A34A Yeşil | "Şimdilik Evde Gözlemleyin" | Evde takip önerileri + 48 saat hatırlatması |

**Kabul Kriterleri:**
- Aciliyet seviyesi büyük, okunaklı şekilde gösterilir
- Gerekçe kısa açıklama olarak gösterilir
- Önerilen adımlar liste halinde sıralanır
- Renk körü kullanıcılar için ikon (🔴🟡🟢) her kartla birlikte gösterilir
- Her kartın altında yasal uyarı metni bulunur

### 5.5 F-05 — Uzman Yönlendirme

**Açıklama:** Triage sonucunda kullanıcıya hangi uzmanlık alanına başvurması gerektiği belirtilir.

**Kabul Kriterleri:**
- Uzmanlık alanı Türkçe ve anlaşılır biçimde yazılır (örn: "Kardiyoloji (Kalp)")
- "Bu Uzmanı Bul" butonu F-08 (Pusula) özelliğini tetikler
- Uzman türü otomatik olarak F-06 arama formuna aktarılır

### 5.6 F-06 — Uzman Arama (3 Mod)

**Açıklama:** Kullanıcı, ihtiyacına göre üç farklı arama modundan birini seçerek uzman ve sağlık kuruluşu bulur.

**Arama Modları:**

| Mod | Nasıl Tetiklenir | Gemini'ye Giden Prompt | Çıktı |
|---|---|---|---|
| **Konuma Göre** | "Konuma Göre" radio seçili + şehir girilir | `UZMAN_PROMPT_YAKIN` | Seçilen şehirdeki en yakın kuruluşlar |
| **Uzmanlığa Göre** | "Uzmanlığa Göre" radio seçili + uzmanlık alanı girilir | `UZMAN_PROMPT` | Türkiye genelinde ilgili uzmanlar |
| **Türkiye Geneli** | (Arka planda, konum girilmeden tetiklenir) | `UZMAN_PROMPT_TURKIYE` | Konumdan bağımsız, ülke geneli referans uzmanlar |

**Form Alanları:**

| Alan | Tip | Zorunlu mu? |
|---|---|---|
| Semptomlar (isteğe bağlı) | Serbest metin | Hayır |
| Arama türü | Radio: Konuma Göre / Uzmanlığa Göre | Evet |
| Konum | Metin (+ "Konumumu Kullan" butonu) | Konuma Göre modunda Evet |
| Uzmanlık alanı | Metin (Pusula ile otomatik gelir, düzenlenebilir) | Uzmanlığa Göre modunda Evet |
| Kurum Tercihi | Radio: Kamu / Özel / Fark Etmez | Hayır |

**Listelenen Uzman Kartı İçeriği:**
- Hekim/kurum adı ve unvanı
- Uzmanlık alanı
- Bağlı olduğu kurum / hastane / üniversite
- Şehir bilgisi
- Randevu yöntemi (MHRS / 182 / Acil 112 / özel)

**Kabul Kriterleri:**
- En fazla 5 uzman/kurum listelenir
- Gemini gerçek bilgi veremiyorsa boş liste döner, kullanıcıya MHRS yönlendirmesi gösterilir
- Kurum Tercihi filtresi (Kamu/Özel/Fark Etmez) her üç modda da geçerlidir

### 5.7 F-07 — Yasal Uyarı

**Açıklama:** Her analiz sonucunda ve uzman listesinde zorunlu yasal uyarı gösterilir.

**Uyarı Metni:**
> "⚠️ Health Compass bir tıbbi tanı aracı değildir. Sunulan bilgiler yalnızca genel yönlendirme amaçlıdır. Sağlık kararlarınız için mutlaka bir sağlık profesyoneliyle görüşünüz."

### 5.8 F-08 — Pusula Özelliği (Smooth Scroll + Otomatik Form Doldurma)

**Açıklama:** Health Compass'ı rakiplerinden ayıran temel özellik. Triage tamamlandıktan sonra kullanıcı "Bu Uzmanı Bul" butonuna tıkladığında iki şey eş zamanlı gerçekleşir:

1. **Smooth Scroll:** Sayfa, uzman arama formuna `window.scrollTo({ behavior: 'smooth' })` ile animasyonlu şekilde kayar.
2. **Otomatik Form Doldurma:** Triage'dan elde edilen `uzman_turu` değeri, DOM manipülasyonuyla uzman arama formundaki ilgili alana otomatik yazılır.

**Kabul Kriterleri:**
- "Bu Uzmanı Bul" butonuna tıklandığında sayfa yumuşak kaydırmayla uzman formuna iner
- Uzman türü alanı Gemini'nin önerdiği uzmanlıkla otomatik dolu gelir
- Kullanıcı yalnızca şehir alanını doldurmak zorunda kalır
- Otomatik doldurulan alan düzenlenebilir olmaya devam eder

---

## 6. Fonksiyonel Olmayan Gereksinimler

### 6.1 Performans

| Kriter | Hedef |
|---|---|
| Gemini API yanıt süresi | ≤ 10 saniye |
| Sayfa yükleme süresi | ≤ 3 saniye |
| API timeout durumunda kullanıcı bildirim süresi | ≤ 10 saniye |

### 6.2 Kullanılabilirlik

- Arayüz mobil uyumlu (responsive) olmalıdır
- Minimum 14px font boyutu kullanılmalıdır
- Renk körü kullanıcılar için aciliyet seviyeleri yalnızca renkle değil, ikonla da gösterilmelidir
- Türkçe karakter desteği tüm giriş alanlarında sağlanmalıdır

### 6.3 Güvenlik

| Risk | Önlem |
|---|---|
| API anahtarı sızması | `.env` dosyasında saklanır, `.gitignore`'a eklenir |
| Kullanıcı verisi gizliliği | Semptom verileri sunucuda depolanmaz |
| Spam / kötüye kullanım | `flask-limiter` ile rate limiting (IP başına dakikada 10 istek) |
| Yanlış tıbbi yönlendirme | Her yanıtta zorunlu yasal uyarı |

### 6.4 Erişilebilirlik

- WCAG 2.1 AA standardına uyum hedeflenir
- Tüm butonlar klavye ile erişilebilir olmalıdır
- Yükleme durumları ekran okuyuculara bildirilmelidir (`aria-live`)

---

## 7. Teknik Gereksinimler

### 7.1 Sistem Mimarisi

```
[KULLANICI TARAYICISI]
  HTML5 + CSS3 + Vanilla JS
        |
        | HTTP POST (JSON)
        v
[BACKEND — Python 3.11 + Flask 3.x]
  app.py / gemini_service.py / prompt_templates.py
        |
        | google-generativeai SDK
        v
[GOOGLE GEMİNİ 1.5 FLASH API]
```

### 7.2 Teknoloji Kararları

| Katman | Teknoloji | Görev |
|---|---|---|
| AI Modeli (Birincil) | Google Gemini 2.5 Flash | Hızlı semptom analizi ve garantili JSON yapılandırma |
| AI Modeli (Yedek) | Gemini 2.0 Flash → 1.5 Flash | Birincil modelin hata vermesi durumunda devreye girer |
| Kota Yönetimi | Akıllı 429 Fallback | Kota hatasında gereksiz istek atılmaz, kullanıcı bilgilendirilir |
| Frontend | Vanilla JS | Smooth Scroll ve DOM manipülasyonu (Pusula özelliği) |
| Frontend | Modern CSS3 | Glassmorphism efektleri ve kart animasyonları |
| Backend | Python & Flask | Sunucu, API endpoint'leri, Gemini entegrasyonu |
| Güvenlik | flask-limiter | Rate limiting (200/gün, 10/dakika) |
| Frontend Deploy | Netlify | Ücretsiz, otomatik CI/CD |
| Backend Deploy | Render.com | Ücretsiz Flask barındırma (gunicorn ile) |
| Ortam Yönetimi | python-dotenv | API anahtarı güvenliği, çoklu yol desteği |

### 7.3 API Endpoint Tanımları

| Endpoint | Method | Girdi | Çıktı |
|---|---|---|---|
| `/` | GET | — | `index.html` |
| `/api/analiz` | POST | `{semptom, ek_bilgi}` | `{aciliyet, gerekce, uzman_turu, adimlar, uyari}` |
| `/api/uzman-bul` | POST | `{uzman_turu, sehir, tercih}` | `{uzmanlar: [...]}` |

### 7.4 Hata Yönetimi

| Durum | Kullanıcıya Gösterilen Mesaj |
|---|---|
| Gemini API yanıt vermedi | "Şu an sunucuya ulaşamıyoruz. Lütfen birkaç dakika sonra tekrar deneyin." |
| 429 Kota Aşımı (ResourceExhausted) | "Kota dolmuş olabilir, lütfen biraz bekleyip tekrar deneyin." — fallback modele geçilmez |
| Geçersiz JSON yanıtı | "Analiz tamamlanamadı. Semptomlarınızı daha ayrıntılı yazarak tekrar deneyiniz." |
| Boş semptom girişi (< 10 karakter) | "Lütfen semptomlarınızı açıklayan en az birkaç kelime giriniz." |
| Gemini servisi yüklenemedi | 503 döner: "Yapay zeka servisine şu an ulaşılamıyor." |
| Uzman bulunamadı | "Bu şehir için kayıtlı uzman bulunamadı. MHRS (mhrs.gov.tr) üzerinden arama yapabilirsiniz." |

---

## 8. Kullanıcı Hikayeleri (User Stories)

| # | Hikaye | Kabul Kriteri |
|---|---|---|
| US-01 | Semptom yaşayan bir kullanıcı olarak, durumun aciliyetini öğrenmek istiyorum, böylece gereksiz yere acil servise gitmeyeyim. | Kullanıcı semptomunu girdiğinde renk kodlu aciliyet kartı gösterilir. |
| US-02 | Hasta yakını olarak, sevdiğimin semptomlarını girerek ne yapması gerektiğini anlamak istiyorum. | Semptom başkası adına da girilebilir, sonuç anlaşılır Türkçe ile sunulur. |
| US-03 | Küçük bir şehirde yaşayan biri olarak, uzmana ulaşmak için hangi şehre gitmem gerektiğini bilmek istiyorum. | Uzman arama sonuçlarında farklı şehirlerdeki kurumlar listelenebilir. |
| US-04 | Uygulamayı kullanan biri olarak, yapay zekanın kesin tanı koymadığını bilmek istiyorum. | Her sonuç ekranında yasal uyarı metni görünür. |
| US-05 | Kullanıcı olarak, hangi uzman türüne başvurmam gerektiğini anlamak istiyorum. | Triage sonucunda uzmanlık alanı açıkça belirtilir ve uzman aramaya otomatik aktarılır. |
| US-06 | Kullanıcı olarak, triage bittikten sonra uzman bulmak için hiçbir şeyi tekrar yazmak istemiyorum. | "Bu Uzmanı Bul" butonuyla form otomatik dolar, sayfa smooth scroll ile kayar. |
| US-07 | Şehrimde uzman bulamayan biri olarak, Türkiye'nin en iyi uzmanlarına ulaşmak istiyorum. | "Türkiye Geneli" seçeneğiyle konumdan bağımsız referans uzmanlar listelenir. |
| US-08 | Ekonomik tercihleri olan bir kullanıcı olarak, kamu veya özel hastane filtreleyebilmek istiyorum. | Kurum Tercihi (Kamu / Özel / Fark Etmez) filtresi uzman listesini buna göre daraltır. |

---

## 9. Başarı Metrikleri

### 9.1 Buildathon Kapsamı (Kısa Vadeli)

| Metrik | Hedef |
|---|---|
| Triage akışının baştan sona çalışması | %100 |
| Uzman arama akışının çalışması | %100 |
| Gemini API entegrasyonunun çalışması | %100 |
| Mobil uyumluluk | Tüm modern tarayıcılarda çalışır |
| Demo videosunun hazır olması | Evet |

### 9.2 Sosyal Etki Hedefleri (Uzun Vadeli)

| Hedef | Gösterge |
|---|---|
| Sağlık okuryazarlığını artırma | Kullanıcıların triage sonucunu anlayıp uygulaması |
| Acil servis yükünü azaltma | Gereksiz acil başvurularının önüne geçilmesi |
| Eşit erişim sağlama | Kırsal/küçük şehir kullanıcılarının da uzman bilgisine ulaşması |

---

## 10. Riskler ve Azaltma Stratejileri

| Risk | Olasılık | Etki | Azaltma Stratejisi |
|---|---|---|---|
| Gemini API yanlış triage seviyesi verebilir | Orta | Yüksek | Prompt mühendisliği + zorunlu yasal uyarı |
| Gemini gerçek olmayan uzman bilgisi verebilir | Orta | Yüksek | "Bilgiyi doğrulayın" uyarısı + MHRS yönlendirmesi |
| API kotasının dolması | Düşük | Orta | Rate limiting + fallback mesajı |
| Kullanıcının yanlış semptomu girmesi | Yüksek | Orta | Açık yönlendirici form + örnek semptom ipuçları |
| Deploy sürecinde teknik sorun | Düşük | Yüksek | Netlify + Render alternatif olarak birbirini destekler |

---

## 11. Ekler

### 11.1 Proje Dosya Yapısı

```
health-compass/
├── README.md
├── idea.md
├── user-flow.md
├── tech-stack.md
├── prd.md
├── tasks.md
├── requirements.txt
├── .env                    # Git'e yüklenmez
├── .env.example            # Örnek env şablonu
├── .gitignore
├── gemini_service.py       # Kök dizinde de mevcut (import uyumluluğu)
├── prompt_templates.py     # Kök dizinde de mevcut
└── features/
    ├── app.py              # Flask ana uygulama (python features/app.py ile çalıştırılır)
    ├── gemini_service.py   # Gemini API entegrasyonu
    ├── prompt_templates.py # Triage ve uzman prompt şablonları
    ├── static/
    │   ├── css/
    │   │   └── style.css
    │   └── js/
    │       └── (JS dosyaları)
    └── templates/
        └── index.html      # Tek sayfa uygulama (SPA benzeri)
```

### 11.2 Bağımlılıklar

```
flask==3.0.3
google-generativeai==0.8.6
python-dotenv==1.0.1
flask-limiter==3.5.0
requests==2.31.0
gunicorn==21.2.0
```

> `gunicorn` — Production deploy için gerekli WSGI sunucusu (Render.com'da kullanılır).

### 11.3 Referans Belgeler

- `idea.md` — Problem tanımı ve ürün fikri
- `tech-stack.md` — Teknoloji kararları ve gerekçeleri
- `user-flow.md` — Kullanıcı akış diyagramları
- `README.md` — Kurulum ve çalıştırma talimatları
