# Health Compass

AI destekli semptom analizi ve uzman yönlendirme uygulaması.

## Kurulum

### 1. Bağımlılıkları yükle

```bash
cd health-compass
pip install -r requirements.txt
```

### 2. Google Gemini API anahtarını ekle

1. [Google AI Studio](https://aistudio.google.com) adresine gidin
2. "Get API key" ile ücretsiz API anahtarı alın
3. Proje klasöründe `.env` dosyası oluşturun:

```bash
# Windows PowerShell
Copy-Item .env.example .env

# Sonra .env dosyasını düzenleyin ve GEMINI_API_KEY değerini yazın
```

4. `.env` dosyasının içeriği:

```
GEMINI_API_KEY=buraya_aldiginiz_api_anahtari
```

**Önemli:** `.env` dosyası Git'e yüklenmez (güvenlik için). API anahtarınızı asla paylaşmayın.

### 3. Uygulamayı çalıştır

```bash
python app.py
```

Tarayıcıda açın: **http://localhost:5000**

## Proje Yapısı

```
health-compass/
├── app.py              # Flask uygulaması
├── gemini_service.py   # Gemini API entegrasyonu
├── prompt_templates.py # AI prompt şablonları
├── requirements.txt
├── .env                # API anahtarı (kendiniz oluşturun)
└── features/
    ├── static/
    │   ├── css/style.css
    │   └── js/
    └── templates/
        └── index.html
```

## API Anahtarı Entegrasyonu

API anahtarı **`.env`** dosyasında saklanır. `gemini_service.py` bu dosyayı `python-dotenv` ile otomatik okur:

```python
# gemini_service.py içinde:
from dotenv import load_dotenv
load_dotenv()  # .env dosyasını yükler

api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)
```

`app.py` başlarken `.env` yüklendiği için `GEMINI_API_KEY` ortam değişkeni olarak kullanılabilir.
