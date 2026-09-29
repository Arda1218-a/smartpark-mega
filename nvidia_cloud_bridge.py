"""
SmartPark DeepTech — NVIDIA Cloud NIM Microservice Bridge (v9.0)
Patent Application: TR 2026/014052 (Arda CENGİZ)
"""

import os
import json
import urllib.request
import urllib.error

NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

def call_nvidia_nim(api_key: str, prompt_text: str, model: str = "meta/llama-3.2-11b-vision-instruct"):
    """
    NVIDIA Build (build.nvidia.com) NIM endpoint'ine doğrudan HTTP POST isteği gönderir.
    """
    if not api_key:
        return {"error": "API anahtarı bulunamadı. Lütfen nvapi-... anahtarınızı girin."}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"SmartPark Mega Hub Akıllı Otopark Giriş Analizi: {prompt_text}"
            }
        ],
        "temperature": 0.2,
        "max_tokens": 150
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(NVIDIA_API_URL, data=data, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_body = response.read().decode("utf-8")
            res_json = json.loads(res_body)
            answer = res_json.get("choices", [{}])[0].get("message", {}).get("content", "")
            return {
                "success": True,
                "model": model,
                "response": answer
            }
    except urllib.error.HTTPError as e:
        return {"error": f"NVIDIA API HTTP Hatası: {e.code} - {e.reason}"}
    except Exception as e:
        return {"error": f"Bağlantı hatası: {str(e)}"}

if __name__ == "__main__":
    test_key = os.environ.get("NVIDIA_API_KEY", "")
    if test_key:
        print("🟢 Test Anahtarı Bulundu, NVIDIA Bulutuna Bağlanılıyor...")
        result = call_nvidia_nim(test_key, "34 VIP 1000 plakalı TOGG T10X aracının plaka ve gövde sınıfını teyit et.")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("ℹ️ NVIDIA_API_KEY çevre değişkeni tanımlanmadı. Yerel simülasyon modu devrede.")
