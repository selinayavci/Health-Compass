"""
Health Compass — Google Gemini API Entegrasyonu
Semptom analizi ve uzman bulma işlemleri bu modülde yapılır.
"""

import os
import json
import traceback
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

try:
    from google.api_core.exceptions import ResourceExhausted as _ResourceExhausted
except ImportError:
    _ResourceExhausted = None

from prompt_templates import TRIAGE_PROMPT, UZMAN_PROMPT, UZMAN_PROMPT_TURKIYE, UZMAN_PROMPT_YAKIN

# .env: proje kökünden yükle (app features/ altından çalışsa bile anahtar bulunsun)
_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")
load_dotenv()  # cwd'deki .env varsa onu da dene


def _log_api_key_status():
    """API anahtarının varlığını ve formatını loglar."""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("[GEMINI] ⚠️  GEMINI_API_KEY ortam değişkeni BULUNAMADI (.env dosyasını kontrol edin)")
        return False
    # Anahtarın ilk/son birkaç karakterini göster (güvenlik için tam gösterme)
    masked = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
    print(f"[GEMINI] ✓ API anahtarı yüklendi: {masked}")
    return True


def _parse_gemini_json(text: str) -> dict:
    """Gemini yanıtından sadece saf JSON'u alır ve parse eder."""
    raw = (text or "").strip()
    if not raw:
        raise ValueError("Empty Gemini response")

    # Markdown code block temizliği:
    # - ```json\n{...}\n```  => { ... }
    # - metin içinde kod bloğu olsa bile içeriği seçmeye çalışır.
    if "```" in raw:
        parts = raw.split("```")
        if len(parts) >= 3:
            # genelde: [prefix, "json\\n{...}", suffix]
            raw = parts[1].strip()
            if raw.lower().startswith("json"):
                raw = raw[4:].lstrip()

    # Ek metin olasılığı için sadece { ... } aralığını al
    start = raw.find("{")
    end = raw.rfind("}")
    if start != -1 and end != -1 and end > start:
        raw = raw[start:end + 1]

    return json.loads(raw)


# Gemini API yapılandırması
# google-generativeai: model adı kısa form ("gemini-...") kullanılır; "models/..." bazen sorun çıkarır.
# GEMINI_MODEL ile .env üzerinden tek model seçebilirsiniz (örn: gemini-2.5-flash).
# Fallback: sadece kota/limit DIŞI hatalarda denenir; 429'da ikinci modele istek atılmaz (kota israfını önler).
_DEFAULT_PRIMARY = "gemini-2.5-flash"
_DEFAULT_FALLBACKS = ["gemini-2.0-flash", "gemini-1.5-flash"]

GEMINI_PRIMARY_MODEL = (os.getenv("GEMINI_MODEL") or _DEFAULT_PRIMARY).strip()
GEMINI_FALLBACK_MODELS = [
    m.strip()
    for m in (os.getenv("GEMINI_FALLBACK_MODELS") or ",".join(_DEFAULT_FALLBACKS)).split(",")
    if m.strip() and m.strip() != GEMINI_PRIMARY_MODEL
]

api_key = os.getenv('GEMINI_API_KEY')
if api_key:
    try:
        genai.configure(api_key=api_key)
        _log_api_key_status()
        model = genai.GenerativeModel(GEMINI_PRIMARY_MODEL)
        print(f"[GEMINI] Model: {GEMINI_PRIMARY_MODEL}")
    except Exception as e:
        print(f"[GEMINI] ✗ API yapılandırma hatası: {e}")
        model = None
else:
    model = None
    _log_api_key_status()


def _default_analiz() -> dict:
    return {
        "aciliyet": "YARIN",
        "aciliyet_gerekce": "Analiz şu an tamamlanamadı. Lütfen tekrar deneyin.",
        "uzman_turu": "Aile Hekimliği",
        "onerilen_adimlar": ["Bir sağlık profesyoneline danışın."],
        "uyari": "Bu bir tıbbi tanı değildir. Sağlık kararlarınız için mutlaka bir sağlık profesyoneliyle görüşünüz."
    }


def _is_quota_or_rate_limit(exc: BaseException) -> bool:
    """429 / kota: ikinci modele denemeyi bırak (aynı proje kotası genelde paylaşılır)."""
    if _ResourceExhausted is not None and isinstance(exc, _ResourceExhausted):
        return True
    s = str(exc).lower()
    return "429" in s or "quota" in s or "resource exhausted" in s or "rate limit" in s


def _generate_json(prompt: str) -> dict:
    """
    Gemini'den JSON almak için dener (response_mime_type application/json ile).
    """
    models_to_try = []
    if model is not None:
        models_to_try.append(model)

    for mname in GEMINI_FALLBACK_MODELS:
        try:
            models_to_try.append(genai.GenerativeModel(mname))
        except Exception:
            continue

    last_err = None
    for m in models_to_try:
        try:
            response = m.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            raw_text = getattr(response, 'text', None)
            if raw_text is None:
                try:
                    if response.candidates:
                        raw_text = response.candidates[0].content.parts[0].text
                    else:
                        raw_text = str(response)
                except Exception as e:
                    raise ValueError("Gemini yanıtından metin çıkarılamadı") from e
            return _parse_gemini_json(raw_text)
        except Exception as e:
            last_err = e
            if _is_quota_or_rate_limit(e):
                print("[GEMINI] Kota / limit (429 veya ResourceExhausted) — fallback atlanıyor.")
                break
            continue

    raise last_err if last_err else ValueError("Gemini JSON üretilemedi")


def semptomu_analiz_et(semptom: str, ek_bilgi: dict) -> dict:
    """
    Semptom ve ek bilgileri Gemini'ye gönderir, triage sonucu döner.
    
    Args:
        semptom: Kullanıcının yazdığı semptom açıklaması
        ek_bilgi: {yas, kronik_hastalik, semptom_suresi} — opsiyonel alanlar
    
    Returns:
        {
            "aciliyet": "ACİL" | "BUGÜN" | "YARIN" | "EV_TAKİBİ",
            "aciliyet_gerekce": str,
            "uzman_turu": str,
            "onerilen_adimlar": list,
            "uyari": str
        }
    """
    if not model:
        return _default_analiz()

    prompt = TRIAGE_PROMPT.format(
        semptom=semptom or "Belirtilmedi",
        yas=ek_bilgi.get('yas', 'Belirtilmedi') if ek_bilgi else 'Belirtilmedi',
        cinsiyet=ek_bilgi.get('cinsiyet', 'Belirtilmedi') if ek_bilgi else 'Belirtilmedi',
        kronik=ek_bilgi.get('kronik_hastalik', 'Belirtilmedi') if ek_bilgi else 'Belirtilmedi',
        sure=ek_bilgi.get('semptom_suresi', 'Belirtilmedi') if ek_bilgi else 'Belirtilmedi'
    )

    try:
        data = _generate_json(prompt)
        if not isinstance(data, dict):
            return _default_analiz()

        default = _default_analiz()
        result = {
            "aciliyet": data.get("aciliyet", default["aciliyet"]),
            "aciliyet_gerekce": data.get("aciliyet_gerekce", default["aciliyet_gerekce"]),
            "uzman_turu": data.get("uzman_turu", default["uzman_turu"]),
            "onerilen_adimlar": data.get("onerilen_adimlar", default["onerilen_adimlar"]),
            "uyari": data.get("uyari", default["uyari"]),
        }

        if not isinstance(result.get("onerilen_adimlar"), list):
            result["onerilen_adimlar"] = default["onerilen_adimlar"]
        # Liste elemanlarını string'e normalize et
        result["onerilen_adimlar"] = [str(x) for x in result["onerilen_adimlar"] if str(x).strip()]
        if not result["onerilen_adimlar"]:
            result["onerilen_adimlar"] = default["onerilen_adimlar"]
        return result
    except Exception as e:
        print(f"[GEMINI] analiz fallback: {type(e).__name__}: {e}")
        return _default_analiz()


def uzman_bul(uzman_turu: str, sehir: str, tercih: str = "Fark Etmez", 
              turkiye_geneli: bool = False, konum_yakin: bool = False, semptom: str = "") -> dict:
    """
    Şehir ve uzman türüne göre Gemini'den uzman listesi alır.
    
    Args:
        uzman_turu: Örn. "Kardiyoloji", "Nöroloji"
        sehir: Aranacak şehir (konum_yakin veya turkiye_geneli'nde farklı kullanım)
        tercih: Kamu / Özel / Fark Etmez
        turkiye_geneli: True ise konumdan bağımsız, Türkiye genelinde en iyi uzmanlar
        konum_yakin: True ise sehir'de en yakın sağlık kuruluşları
        semptom: Kullanıcı semptomları (uzman önerisi için)
    
    Returns:
        {"uzmanlar": [{ad, uzmanlik, kurum, sehir, randevu}, ...]}
    """
    if not model:
        return {"uzmanlar": []}

    semptom_ctx = semptom.strip() if semptom else "Belirtilmedi"

    if turkiye_geneli:
        prompt = UZMAN_PROMPT_TURKIYE.format(
            uzman_turu=uzman_turu or "Genel",
            tercih=tercih or "Fark Etmez",
            semptom=semptom_ctx
        )
    elif konum_yakin:
        prompt = UZMAN_PROMPT_YAKIN.format(
            sehir=sehir or "Belirtilmedi",
            semptom=semptom_ctx,
            uzman_turu=uzman_turu or "Genel",
            tercih=tercih or "Fark Etmez"
        )
    else:
        prompt = UZMAN_PROMPT.format(
            uzman_turu=uzman_turu or "Genel",
            sehir=sehir or "Belirtilmedi",
            tercih=tercih or "Fark Etmez"
        )

    try:
        data = _generate_json(prompt)
        if isinstance(data, dict) and isinstance(data.get("uzmanlar"), list):
            return data
        return {"uzmanlar": []}
    except Exception as e:
        print(f"[GEMINI] uzman fallback: {type(e).__name__}: {e}")
        return {"uzmanlar": []}
