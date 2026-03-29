"""
Health Compass — AI Destekli Semptom Analizi ve Uzman Yönlendirme
Flask Ana Uygulama - Final Versiyon
"""

import os
import traceback
from pathlib import Path

from flask import Flask, request, jsonify, render_template from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from flask_cors import CORS
# .env: proje kökünden yükle (çalışma dizininden bağımsız)
_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")
load_dotenv()

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static'
)
CORS(app, origins=[
    "https://eclectic-capybara-455bc7.netlify.app",
    "http://localhost:5000",
    "http://127.0.0.1:5000"
])
# Rate limiting: Güvenlik için istek sınırlama
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "10 per minute"]
)

# Gemini servisini içe aktar
try:
    from features.gemini_service import semptomu_analiz_et, uzman_bul
    GEMINI_HAZIR = True
except Exception as e:
    GEMINI_HAZIR = False
    print(f"⚠️ Gemini servisi yüklenemedi: {e}")

@app.route('/')
def anasayfa():
    """Ana sayfa."""
    return render_template('index.html')

@app.route('/api/analiz', methods=['POST'])
@limiter.limit("5 per minute")
def semptomu_analiz_et_endpoint():
    """Semptom analizi ve Triage sonucu."""
    if not request.is_json:
        return jsonify({"hata": "JSON bekleniyor"}), 400

    veri = request.get_json() or {}
    semptom = (veri.get('semptom') or '').strip()
    ek_bilgi = veri.get('ek_bilgi') or {}

    # 1. Temel Kontrol: Semptom uzunluğu
    if len(semptom) < 10:
        return jsonify({
            "hata": "Lütfen semptomlarınızı açıklayan en az birkaç kelime giriniz."
        }), 400

    # 2. Servis Kontrolü: API Anahtarı var mı?
    if not GEMINI_HAZIR or not os.getenv('GEMINI_API_KEY'):
        return jsonify({
            "hata": "Yapay zeka servisine şu an ulaşılamıyor. Lütfen daha sonra tekrar deneyiniz."
        }), 503

    # 3. AI Analiz Süreci
    try:
        sonuc = semptomu_analiz_et(semptom, ek_bilgi)
        
        # Veri Normalizasyonu: Frontend 'uzman_turu' bekler
        if isinstance(sonuc, dict):
            if not sonuc.get("uzman_turu") and sonuc.get("specialist"):
                sonuc["uzman_turu"] = sonuc.get("specialist")
        
        return jsonify(sonuc)
        
    except Exception as e:
        print(f"\n[API /api/analiz] HATA: {e}")
        traceback.print_exc()
        return jsonify({
            "hata": "Analiz sırasında bir sorun oluştu. Kota dolmuş olabilir, lütfen biraz bekleyip tekrar deneyin."
        }), 500

@app.route('/api/uzman-bul', methods=['POST'])
@limiter.limit("10 per minute")
def uzman_bul_endpoint():
    """Şehir ve uzman türüne göre arama."""
    if not request.is_json:
        return jsonify({"hata": "JSON bekleniyor"}), 400

    veri = request.get_json() or {}
    uzman_turu = (veri.get('uzman_turu') or '').strip() or "Genel"
    sehir = (veri.get('sehir') or '').strip()
    tercih = (veri.get('tercih') or 'Fark Etmez').strip()
    turkiye_geneli = bool(veri.get('turkiye_geneli', False))
    konum_yakin = bool(veri.get('konum_yakin', False))
    semptom = (veri.get('semptom') or '').strip()

    if not turkiye_geneli and not sehir:
        return jsonify({"hata": "Lütfen bir şehir giriniz."}), 400

    if not GEMINI_HAZIR or not os.getenv('GEMINI_API_KEY'):
        return jsonify({
            "hata": "Servis şu an kapalı. Lütfen daha sonra deneyiniz."
        }), 503

    try:
        sonuc = uzman_bul(uzman_turu, sehir, tercih, turkiye_geneli, konum_yakin, semptom)
        return jsonify(sonuc)
    except Exception as e:
        print(f"\n[API /api/uzman-bul] HATA: {e}")
        return jsonify({
            "hata": "Uzman arama tamamlanamadı. Lütfen bilgileri kontrol edip tekrar deneyin."
        }), 500

if __name__ == '__main__':
    # Başlangıç kontrolleri
    if not os.getenv('GEMINI_API_KEY'):
        print("⚠️ KRİTİK UYARI: GEMINI_API_KEY .env dosyasında bulunamadı!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)