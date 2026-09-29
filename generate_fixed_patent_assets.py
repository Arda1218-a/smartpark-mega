import os
import subprocess

folder = r'c:\Users\LENOVO\Documents\oto\patent_files\duzeltilmis_patent'
os.makedirs(folder, exist_ok=True)

# 1. ÖZET HTML (Sayfa numaralı, link/tarih temizlenmiş)
ozet_html = """<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>
  @page { margin: 25mm 20mm 20mm 20mm; @bottom-center { content: "1"; } }
  body { font-family: 'Times New Roman', Times, serif; font-size: 12pt; line-height: 1.5; text-align: justify; }
  .header { text-align: center; font-weight: bold; margin-bottom: 20px; font-size: 14pt; }
  .footer { position: fixed; bottom: 0; left: 0; right: 0; text-align: center; font-size: 10pt; }
</style>
</head>
<body>
<div class='header'>ÖZET</div>
<p style='text-align: center; font-weight: bold; margin-bottom: 15px;'>FİZİKSEL BOYUT VE AKS YÜKÜ FİLTRELİ, ÇOK KAPILI VARYANS MİNİMİZASYONLU DENGELİ OTOPARK İŞLETİM VE DENETİM SİSTEMİ</p>
<p>Bu buluş; kapalı otopark tesislerinde araç kabulü, yer tahsisi, operasyonel güvenlik ve ücretlendirme süreçlerini yöneten akıllı bir otopark kontrol sistemidir. Buluş; otopark giriş kapılarında konumlandırılan aks kantarı (11) ve LiDAR tavan yükseklik sensörü (12) ile araçların fiziksel kütle ve yükseklik profilini ölçerek, 2.5 ton üzeri ve 2.10 metre üzerindeki ağır ve yüksek araçları zorunlu olarak güçlendirilmiş zemin kata (Kat 1) yönlendiren; standart araçları ise katlar arası varyans minimizasyonu algoritması ile homojen dağıtan bir merkezi işlem birimi (10) içermektedir. Buluş ayrıca, yanlış park ihlallerini metal plakadan bağımsız olarak sürücü kimliği (21) ile eşleştiren 2 adımlı araç sahiplik devri protokolü (20), her katta yer alan elektrikli araç şarj istasyonu (15) çatışma çözücü algoritması ve dakika hassasiyetli kademeli fiyatlandırma mekanizması ile karakterize edilmektedir.</p>
<div class='footer'>1</div>
</body>
</html>"""

# 2. İSTEMLER HTML (5'erli satır numaralı ve "olup, özelliği; ... içermesidir" formatında)
istemler_html = """<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>
  @page { margin: 25mm 20mm 20mm 20mm; }
  body { font-family: 'Times New Roman', Times, serif; font-size: 12pt; line-height: 2.0; text-align: justify; }
  .header { text-align: center; font-weight: bold; margin-bottom: 20px; font-size: 14pt; }
  .line-table { width: 100%; border-collapse: collapse; }
  .line-num { width: 35px; color: #555; vertical-align: top; font-size: 10pt; text-align: right; padding-right: 15px; user-select: none; }
  .line-text { vertical-align: top; }
  .footer { position: fixed; bottom: 0; left: 0; right: 0; text-align: center; font-size: 10pt; }
</style>
</head>
<body>
<div class='header'>İSTEMLER</div>

<table class='line-table'>
  <tr><td class='line-num'></td><td class='line-text'><b>1.</b> Buluş, akıllı bir kapalı otopark yönetim sistemi <b>olup, özelliği;</b></td></tr>
  <tr><td class='line-num'>5</td><td class='line-text'>- otopark girişinde araç kütlesini ölçen en az bir aks kantarı (11),</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>- araç tavan yüksekliğini ölçen en az bir tavan LiDAR sensörü (12),</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>- kütle ve yükseklik verilerine göre araçları katlara doluluk varyansını minimize</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>ederek yönlendiren en az bir merkezi kontrol ünitesi (10) <b>içermesidir.</b></td></tr>
  <tr><td class='line-num'>10</td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><b>2.</b> İstem 1'deki otopark yönetim sistemi <b>olup, özelliği;</b></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>- aks kantarından (11) ölçülen kütlenin 2500 kg üzerinde veya LiDAR sensöründen (12)</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>ölçülen yüksekliğin 2100 mm üzerinde olması halinde aracı yalnızca güçlendirilmiş</td></tr>
  <tr><td class='line-num'>15</td><td class='line-text'>zemin kat slotlarına yönlendiren, söz konusu katın dolu olması durumunda güvenlik</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>bariyerini (14) kilitleyerek aracı çıkış bypass şeridine (16) sevk eden güvenlik kilidi</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>mekanizması <b>içermesidir.</b></td></tr>
  <tr><td class='line-num'>20</td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><b>3.</b> İstem 1'deki otopark yönetim sistemi <b>olup, özelliği;</b></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>- araçları katlara tahsis ederken kat doluluk oranlarının ortalama doluluktan olan</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>varyansını minimize edecek şekilde araçları en az dolu olan kata dinamik olarak</td></tr>
  <tr><td class='line-num'>25</td><td class='line-text'>yönlendiren dağıtım algoritması <b>içermesidir.</b></td></tr>
  <tr><td class='line-num'></td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><b>4.</b> İstem 1'deki otopark yönetim sistemi <b>olup, özelliği;</b></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>- hatalı park ihlal cezalarını metal araç plakası yerine doğrudan sürücü kimlik</td></tr>
  <tr><td class='line-num'>30</td><td class='line-text'>hesabına (21) işleyen, araç mülkiyeti el değiştirdiğinde iki faktörlü (2FA) doğrulama</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>kodu ile plakanın yeni araç sahibine sıfırlanmış temiz sicille aktarılmasını sağlayan</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>araç sahiplik devir modülü (20) <b>içermesidir.</b></td></tr>
  <tr><td class='line-num'>35</td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><b>5.</b> İstem 1'deki otopark yönetim sistemi <b>olup, özelliği;</b></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>- elektrikli bir aracın tahsis edilen standart slot yerine doğrudan katta yer alan</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>elektrikli araç şarj istasyonuna (15) park etmesi halinde ceza ihlali oluşturmayarak</td></tr>
  <tr><td class='line-num'>40</td><td class='line-text'>sistemi otomatik olarak şarj tarifesine geçiren akıllı çatışma çözücü algoritması <b>içermesidir.</b></td></tr>
  <tr><td class='line-num'></td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><b>6.</b> İstem 1'deki otopark yönetim sistemi <b>olup, özelliği;</b></td></tr>
  <tr><td class='line-num'>45</td><td class='line-text'>- ilk 60 dakika için dakika başına sabit ücret, 60 dakikayı aşan süreler için ise tam saat</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>tabanı ile artık dakika çarpanının toplanmasıyla dinamik ücret hesaplayan kademeli</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>dakika fiyatlandırma motoru <b>içermesidir.</b></td></tr>
  <tr><td class='line-num'>50</td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><b>7.</b> İstem 1'deki otopark yönetim sistemi <b>olup, özelliği;</b></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>- dijital mobil uygulamaya veya QR koda sahip olmayan sürücüler için tek butonla</td></tr>
  <tr><td class='line-num'>55</td><td class='line-text'>barkodlu kağıt bilet üreten ve çıkışta görevliye nakit ödeme imkanı tanıyan hibrit</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>gişe ünitesi <b>içermesidir.</b></td></tr>
</table>
<div class='footer'>2</div>
</body>
</html>"""

# 3. TARİFNAME HTML (5'erli satır numaralı)
tarifname_html = """<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>
  @page { margin: 25mm 20mm 20mm 20mm; }
  body { font-family: 'Times New Roman', Times, serif; font-size: 11pt; line-height: 1.8; text-align: justify; }
  .header { text-align: center; font-weight: bold; margin-bottom: 15px; font-size: 13pt; }
  .line-table { width: 100%; border-collapse: collapse; }
  .line-num { width: 35px; color: #555; vertical-align: top; font-size: 9pt; text-align: right; padding-right: 15px; user-select: none; }
  .line-text { vertical-align: top; }
  h3 { font-size: 11pt; font-weight: bold; margin-top: 15px; margin-bottom: 5px; }
  .footer { position: fixed; bottom: 0; left: 0; right: 0; text-align: center; font-size: 10pt; }
</style>
</head>
<body>
<div class='header'>TARİFNAME</div>
<p style='text-align: center; font-weight: bold; margin-bottom: 15px;'>FİZİKSEL BOYUT VE AKS YÜKÜ FİLTRELİ, ÇOK KAPILI VARYANS MİNİMİZASYONLU DENGELİ OTOPARK İŞLETİM VE DENETİM SİSTEMİ</p>

<table class='line-table'>
  <tr><td class='line-num'></td><td class='line-text'><h3>Buluşun İlgili Olduğu Teknik Alan</h3></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>Buluş; akıllı ulaşım sistemleri (ITS), otopark yönetim altyapıları, araç ağırlık ve boyut</td></tr>
  <tr><td class='line-num'>5</td><td class='line-text'>algılama sensörleri, dağıtık kapı kuyruk arbitrajı ve elektrikli araç şarj yönetim teknolojileri ile ilgilidir.</td></tr>
  <tr><td class='line-num'></td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><h3>Tekniğin Bilinen Durumu (Önceki Teknik)</h3></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>Geleneksel otopark sistemlerinde araçlar boş bir kata veya ilk kata sırayla yığılmakta, bu durum</td></tr>
  <tr><td class='line-num'>10</td><td class='line-text'>kat rampalarında ve koridorlarda trafik kilitlenmelerine yol açmaktadır. Ayrıca yüksek tavanlı veya</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>ağır tonajlı araçların tavan yüksekliği ve zemin taşıma kapasitesi kontrol edilmeksizin üst katlara</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>kabul edilmesi ciddi yapısal hasarlara sebep olmaktadır. Mevcut sistemlerde cezalar yalnızca plakaya</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>kesilmekte, araç el değiştirdiğinde masum yeni araç sahipleri haksız kısıtlamalarla karşılaşmaktadır.</td></tr>
  <tr><td class='line-num'>15</td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><h3>Buluşun Çözdüğü Teknik Problemler</h3></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>1. Rampa ve koridorlardaki araç yığılmalarını kat doluluk varyansını minimize ederek engellemek.</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>2. Ağır ve yüksek araçların üst kat tavan ve zeminlerine zarar vermesini giriş kantar/LiDAR filtresiyle fiziksel olarak önlemek.</td></tr>
  <tr><td class='line-num'>20</td><td class='line-text'>3. Araç satışlarında geçmiş cezaların yeni araç sahibine geçmesini engelleyen 2 adımlı sürücü-plaka ayrıştırma altyapısı sunmak.</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>4. Elektrikli araçların normal park yerine gitmeyip doğrudan şarj istasyonuna yönelmesi durumunda ceza kesilmesini önleyen akıllı tarife geçişi sağlamak.</td></tr>
  <tr><td class='line-num'>25</td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><h3>Şekillerin Açıklaması</h3></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><b>Şekil 1:</b> Çok kapılı giriş sensör dizisi ve merkezi işlem mimarisi blok diyagramı.</td></tr>
  <tr><td class='line-num'></td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><h3>Parça ve Referans Numaraları</h3></td></tr>
  <tr><td class='line-num'>30</td><td class='line-text'>(10) Merkezi Kontrol ve Dağıtım Ünitesi</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>(11) Aks Kantarı (Load-Cell Ağırlık Sensörü)</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>(12) LiDAR / Lazer Tavan Yükseklik Sensörü</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>(13) Dağıtık Giriş Kapıları</td></tr>
  <tr><td class='line-num'>35</td><td class='line-text'>(14) Güvenlik Bariyeri ve Hibrit Bilet Yazıcı</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>(15) 120 kW Hızlı DC EV Şarj İstasyonları</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>(16) Çıkış Bypass ve Tahliye Şeridi</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>(20) 2FA Araç Sahiplik Devir Modülü</td></tr>
  <tr><td class='line-num'>40</td><td class='line-text'>(21) Sürücü Kimlik ve Ceza Veritabanı</td></tr>
  <tr><td class='line-num'></td><td class='line-text'></td></tr>
  <tr><td class='line-num'></td><td class='line-text'><h3>Buluşun Detaylı Açıklaması</h3></td></tr>
  <tr><td class='line-num'></td><td class='line-text'>Giriş kapısına (13) yanaşan bir aracın ağırlığı aks kantarı (11) ile, tavan yüksekliği LiDAR</td></tr>
  <tr><td class='line-num'>45</td><td class='line-text'>sensörü (12) ile ölçülür. Ölçülen kütle değeri 2500 kg'dan veya yükseklik değeri 2100 mm'den</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>büyükse, merkezi kontrol ünitesi (10) bu aracı zorunlu olarak yalnızca Kat 1'deki güçlendirilmiş</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>slotlara tahsis eder. Kat 1 dolu ise güvenlik bariyeri (14) açılmaz ve araç çıkış bypass şeridine (16)</td></tr>
  <tr><td class='line-num'></td><td class='line-text'>yönlendirilir. Standart araçlar için merkezi kontrol ünitesi (10), katlar arasındaki doluluk varyansını</td></tr>
  <tr><td class='line-num'>50</td><td class='line-text'>minimize edecek şekilde araçları en az dolu kata dinamik olarak yönlendirir.</td></tr>
</table>
<div class='footer'>3</div>
</body>
</html>"""

# 4. RESİMLER HTML (Yazısız teknik çizim, başlık yok, sadece "Şekil 1" ve referans numaraları, sayfa no "1/1")
resimler_html = """<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>
  @page { margin: 20mm; }
  body { font-family: 'Times New Roman', Times, serif; text-align: center; }
  svg { width: 700px; height: 500px; margin-top: 40px; }
  .footer { position: fixed; bottom: 10px; left: 0; right: 0; text-align: center; font-size: 11pt; font-family: 'Times New Roman', serif; }
</style>
</head>
<body>

<svg viewBox="0 0 700 500" xmlns="http://www.w3.org/2000/svg">
  <!-- 11: Aks Kantarı -->
  <rect x="50" y="80" width="160" height="80" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="130" y="125" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">11</text>

  <!-- 12: LiDAR -->
  <rect x="50" y="240" width="160" height="80" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="130" y="285" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">12</text>

  <!-- 10: Merkezi İşlem Ünitesi -->
  <rect x="290" y="140" width="180" height="120" fill="#ffffff" stroke="#000000" stroke-width="2.5"/>
  <text x="380" y="205" font-size="22" font-family="Times New Roman" text-anchor="middle" font-weight="bold">10</text>

  <!-- 14: Bariyer -->
  <rect x="540" y="80" width="130" height="80" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="605" y="125" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">14</text>

  <!-- 16: Bypass -->
  <rect x="540" y="240" width="130" height="80" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="605" y="285" font-size="20" font-family="Times New Roman" text-anchor="middle" font-weight="bold">16</text>

  <!-- Oklar / Çizgiler -->
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#000000"/>
    </marker>
  </defs>

  <line x1="210" y1="120" x2="285" y2="170" stroke="#000000" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="210" y1="280" x2="285" y2="230" stroke="#000000" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="470" y1="170" x2="535" y2="120" stroke="#000000" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="470" y1="230" x2="535" y2="280" stroke="#000000" stroke-width="2" marker-end="url(#arrow)"/>

  <text x="350" y="440" font-size="18" font-family="Times New Roman" text-anchor="middle" font-weight="bold">Şekil 1</text>
</svg>

<div class='footer'>1/1</div>
</body>
</html>"""

with open(os.path.join(folder, 'ozet.html'), 'w', encoding='utf-8') as f: f.write(ozet_html)
with open(os.path.join(folder, 'istemler.html'), 'w', encoding='utf-8') as f: f.write(istemler_html)
with open(os.path.join(folder, 'tarifname.html'), 'w', encoding='utf-8') as f: f.write(tarifname_html)
with open(os.path.join(folder, 'resimler.html'), 'w', encoding='utf-8') as f: f.write(resimler_html)

chrome_paths = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'
]
browser_exe = next((p for p in chrome_paths if os.path.exists(p)), None)

for name in ['ozet', 'istemler', 'tarifname', 'resimler']:
    in_html = os.path.join(folder, f'{name}.html')
    out_pdf = os.path.join(folder, f'{name}.pdf')
    cmd = f'"{browser_exe}" --headless --disable-gpu --print-to-pdf="{out_pdf}" "{in_html}"'
    subprocess.run(cmd, shell=True)

# JPG Dönüşümü (Şekil 1 saf JPG)
in_resim = os.path.join(folder, 'resimler.html')
out_png = os.path.join(folder, 'bulten_resim.png')
cmd_jpg = f'"{browser_exe}" --headless --disable-gpu --screenshot="{out_png}" --window-size=1000,750 "{in_resim}"'
subprocess.run(cmd_jpg, shell=True)

ps_script = f"""
Add-Type -AssemblyName System.Drawing
$inPath = "{out_png}"
$outPath = "{os.path.join(folder, 'bulten_resim.jpg')}"
$img = [System.Drawing.Image]::FromFile($inPath)
$img.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
$img.Dispose()
"""
ps_file = os.path.join(folder, 'convert_jpg.ps1')
with open(ps_file, 'w', encoding='utf-8') as f: f.write(ps_script)
subprocess.run(f'powershell -ExecutionPolicy Bypass -File "{ps_file}"', shell=True)

print("Tüm düzeltilmiş patent dosyaları hazır!")
