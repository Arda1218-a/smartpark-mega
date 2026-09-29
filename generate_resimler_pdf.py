import os
import subprocess

folder = r'c:\Users\LENOVO\Documents\oto\patent_files\duzeltilmis_patent'
os.makedirs(folder, exist_ok=True)

# TÜRKPATENT Yönetmeliğine %100 Uyumlu Resimler Sayfası
# Kurallar:
# 1. Başlık YOK (Şekiller, Resimler vb. yazılar tamamen silindi)
# 2. Kelime/Metin YOK (Sadece parça numaraları 10, 11, 12, 13, 14, 15, 16, 20, 21)
# 3. Şekil Numarası: "Şekil 1"
# 4. Sayfa Numarası: "1/1"
resimler_html = """<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>
  @page {
    size: A4 portrait;
    margin: 25mm 20mm 20mm 20mm;
  }
  body {
    margin: 0;
    padding: 0;
    font-family: 'Times New Roman', Times, serif;
    text-align: center;
    background: #ffffff;
  }
  .drawing-container {
    width: 100%;
    height: 780px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  svg {
    width: 680px;
    height: 520px;
  }
  .footer-page {
    position: fixed;
    bottom: 5mm;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 11pt;
    font-family: 'Times New Roman', serif;
  }
</style>
</head>
<body>

<div class="drawing-container">
  <svg viewBox="0 0 680 500" xmlns="http://www.w3.org/2000/svg">
    <!-- Giriş Kapısı (13) -->
    <rect x="30" y="50" width="130" height="60" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <text x="95" y="87" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">13</text>

    <!-- Aks Kantarı (11) -->
    <rect x="30" y="150" width="130" height="60" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <text x="95" y="187" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">11</text>

    <!-- LiDAR Tavan Sensörü (12) -->
    <rect x="30" y="250" width="130" height="60" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <text x="95" y="287" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">12</text>

    <!-- Merkezi İşlem Ünitesi (10) -->
    <rect x="250" y="130" width="170" height="150" fill="#ffffff" stroke="#000000" stroke-width="2.5"/>
    <text x="335" y="212" font-size="26" font-family="Times New Roman" text-anchor="middle" font-weight="bold">10</text>

    <!-- Güvenlik Bariyeri (14) -->
    <rect x="510" y="40" width="130" height="55" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <text x="575" y="75" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">14</text>

    <!-- Çıkış Bypass Şeridi (16) -->
    <rect x="510" y="120" width="130" height="55" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <text x="575" y="155" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">16</text>

    <!-- EV Şarj İstasyonu (15) -->
    <rect x="510" y="200" width="130" height="55" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <text x="575" y="235" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">15</text>

    <!-- 2FA Sahiplik Devri (20) & Sürücü Veritabanı (21) -->
    <rect x="510" y="280" width="130" height="55" fill="#ffffff" stroke="#000000" stroke-width="2"/>
    <text x="575" y="315" font-size="18" font-family="Times New Roman" text-anchor="middle" font-weight="bold">20, 21</text>

    <!-- Oklar -->
    <defs>
      <marker id="arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 9 5 L 0 9 z" fill="#000000"/>
      </marker>
    </defs>

    <!-- Giriş Okları -->
    <line x1="160" y1="80" x2="250" y2="160" stroke="#000000" stroke-width="2" marker-end="url(#arr)"/>
    <line x1="160" y1="180" x2="250" y2="195" stroke="#000000" stroke-width="2" marker-end="url(#arr)"/>
    <line x1="160" y1="280" x2="250" y2="230" stroke="#000000" stroke-width="2" marker-end="url(#arr)"/>

    <!-- Çıkış Okları -->
    <line x1="420" y1="165" x2="510" y2="70" stroke="#000000" stroke-width="2" marker-end="url(#arr)"/>
    <line x1="420" y1="185" x2="510" y2="145" stroke="#000000" stroke-width="2" marker-end="url(#arr)"/>
    <line x1="420" y1="215" x2="510" y2="225" stroke="#000000" stroke-width="2" marker-end="url(#arr)"/>
    <line x1="420" y1="245" x2="510" y2="300" stroke="#000000" stroke-width="2" marker-end="url(#arr)"/>

    <!-- Şekil Numarası -->
    <text x="335" y="440" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">Şekil 1</text>
  </svg>
</div>

<div class="footer-page">1/1</div>

</body>
</html>"""

html_path = os.path.join(folder, 'resimler.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(resimler_html)

chrome_paths = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'
]
browser_exe = next((p for p in chrome_paths if os.path.exists(p)), None)

out_pdf = os.path.join(folder, 'resimler.pdf')
cmd = f'"{browser_exe}" --headless --disable-gpu --print-to-pdf="{out_pdf}" "{html_path}"'
subprocess.run(cmd, shell=True)

print("Resimler PDF başarıyla üretildi!")
