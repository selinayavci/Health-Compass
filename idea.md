# 💡 Proje Fikri: Health Compass

## Problem Tanımı

### Bağlam

Türkiye'de ve birçok gelişmekte olan ülkede sağlık hizmetlerine erişimde iki kritik boşluk bulunmaktadır. Bu boşluklar yalnızca coğrafi bir erişim sorunu değil; aynı zamanda **doğru bilgiye ve doğru uzmana ulaşma sorunudur.**

### Sorun 1: Aciliyet Belirsizliği (Triage Boşluğu)

Bireyler günlük yaşamda çeşitli semptomlar yaşadıklarında şu soruyla karşı karşıya kalırlar:

> *"Bu belirtiler için hemen acil servise mi gitmeliyim, yoksa yarın aile hekimime mi başvursam yeterli?"*

İnsanlar ne kadar acil olduğunu bilmedikleri için acil servisleri gereksiz meşgul ediyor. Bu belirsizliğin iki tehlikeli sonucu vardır:

- **Aşırı başvuru:** Acil olmayan vakalar acil servislere yığılır, gerçek acil hastalara müdahale gecikmesi yaşanır.
- **Geç başvuru:** Gerçekten acil olan vakalar hafife alınır ve ciddi sağlık kayıplarına yol açar.

### Sorun 2: Uzmanlık Eşitsizliği (Kritik Vakalarda Yönlendirme Boşluğu)

Karmaşık bir ameliyat veya nadir bir hastalık söz konusu olduğunda bireyler şu soruyla baş başa kalır:

> *"Bu alanda deneyimli, güvenilir bir uzman hekime nasıl ulaşabilirim? Şehrimde yoksa nereye gitmeliyim?"*

Sosyoekonomik açıdan dezavantajlı bireyler, bu bilgiye erişmekte en fazla güçlük çeken gruptur. Doğru uzmana ulaşmak çoğunlukla kişisel ilişkilere veya şansa bağlıdır.

---

## Kullanıcı Profili

### Birincil Kullanıcı

- Dijital araçlara erişimi olan, ancak tıbbi konularda profesyonel yönlendirmeden yoksun bireyler
- Yaş aralığı: 15–55
- Semptom yaşayan kişi ya da hasta yakını
- Acil mi değil mi kararını vermekte zorlanan herkes

### İkincil Kullanıcı

- Uzman hekim bulmakta güçlük çeken, küçük şehirlerde veya kırsal alanda yaşayan bireyler
- Yurtdışında yaşayan ve Türkiye'deki sağlık sistemine yabancı olan Türk vatandaşları

---

## Yapay Zekanın Rolü

Health Compass, yapay zekayı iki kritik aşamada kullanır. Arka planda **Google Gemini 2.5 Flash** modeli çalışır — bu model, hızlı yanıt süresi ve güvenilir JSON yapılandırma kapasitesiyle triage için özel olarak seçilmiştir.

### Aşama 1 — Semptom Analizi ve Öncelik Belirleme

| Girdi | Çıktı |
|---|---|
| Kullanıcının tarif ettiği semptomlar | Aciliyet seviyesi (ACİL / BUGÜN / YARIN / EV_TAKİBİ) |
| Yaş, cinsiyet, kronik hastalık bilgisi | Hangi uzmana başvurulması gerektiği |
| Semptomların ne zamandır sürdüğü | Net ve anlaşılır eylem önerisi + önerilen adımlar |

> **Not:** Yapay zeka kesin tıbbi tanı koymaz; yalnızca yönlendirme ve önceliklendirme yapar.

### Aşama 2 — Akıllı Uzman Eşleştirme (3 Mod)

| Mod | Tetikleyici | Çıktı |
|---|---|---|
| **Şehir Bazlı** | Kullanıcı şehir girer | O şehirdeki uzman ve kurumlar |
| **Türkiye Geneli** | "Türkiye'nin En İyi Uzmanları" seçilir | Konumdan bağımsız, ülke genelinde referans uzmanlar |
| **En Yakın Kurum** | "Konuma Göre" seçilir | Kullanıcının bulunduğu şehirdeki en yakın sağlık kuruluşları |

### Kesintisiz Deneyim: Akıllı Fallback Sistemi

Yoğun kullanım dönemlerinde API kota sınırlarına (429 hatası) karşı **çok katmanlı bir hata yönetimi** mevcuttur:

```
Gemini 2.5 Flash (birincil)
    ↓ hata / timeout durumunda
Gemini 2.0 Flash (birinci yedek)
    ↓ hata / timeout durumunda
Gemini 1.5 Flash (ikinci yedek)
    ↓ 429 Kota Hatası durumunda
Akıllı fallback atlanır → Kullanıcıya bilgilendirici mesaj
```

> **Teknik Not:** 429 (Kota Aşımı) hatasında fallback modele geçilmez — aynı proje kotası tüm modeller için paylaşıldığından gereksiz istek atılmaz. Bu, kaynakların verimli kullanılmasını sağlar.

---

## Health Compass'ı Farklı Kılan Nedir?

| Özellik | Genel Semptom Uygulamaları | Health Compass |
|---|---|---|
| Odak | "Ne hastalığım var?" | "Şimdi ne yapmalıyım?" |
| Uzman Yönlendirme | ❌ Yok | ✅ Var (3 farklı modda) |
| Aciliyet Sınıflandırma | Genel | Kişiselleştirilmiş (yaş + cinsiyet dahil) |
| Kurum Tercihi | ❌ Yok | ✅ Kamu / Özel / Fark Etmez |
| Türkiye Geneli Arama | ❌ Yok | ✅ Var (konumdan bağımsız) |
| Kritik Vaka Desteği | ❌ Yok | ✅ Var |
| Otomatik Form Doldurma | ❌ Yok | ✅ Var (Pusula özelliği) |
| Kota Yönetimi | ❌ Yok | ✅ Akıllı fallback + 429 koruması |
| Hedef Kitle | Genel | Dezavantajlı gruplara öncelik |

### 🧭 Pusula Özelliği

Health Compass, sadece uzman önermekle kalmaz; **"Pusula" özelliğiyle** kullanıcıyı uygulama içindeki forma otomatik yönlendirir ve alanı doldurur. Triage analizi tamamlandığında "Bu Uzmanı Bul" butonuna tıklamak yeterlidir — uzman türü, şehir bilgisi ve tercihler otomatik olarak uzman arama formuna aktarılır. Kullanıcının ekstra bir adım atmasına gerek kalmaz.

---

## Sosyal Etki Hedefi

Health Compass; sağlık bilgisine erişimin herkes için eşit olması gerektiği inancıyla tasarlanmıştır. Proje, UpSchool bünyesindeki "Birbirini Geliştiren Kadınlar" programı kapsamında geliştirilmiş olup bu program, kadınların teknoloji alanında kendilerini geliştirmesini destekleyen bir girişimdir.

Uygulamanın hedeflediği sosyal etkiler:

- Sağlık okuryazarlığını artırmak,
- Acil servis yükünü azaltmak,
- Ekonomik ve coğrafi engellerden bağımsız olarak herkesin doğru sağlık kararı alabilmesini sağlamak.
