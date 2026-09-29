# 📋 SmartPark Mega — Yapılan Güncellemeler, Saha İyileştirmeleri, Hata Günlüğü & Yol Haritası (Changelog & Roadmap)

> **Resmi Patent Başvuru Numarası:** `TR 2026/014052` (Patent Pending - Arda CENGİZ)  
> **Mevcut Kararlı Sürüm:** `v10.0 LTS` (Long Term Support — Endüstriyel Donma Sürümü)  
> **Ana Mühendislik İlkesi:** 🛡️ *"Çalışıyorsa Kurcalama!" (If it works, don't break it — Kararlılık ve Sıfır Regresyon İlkesi)*

---

## 🛡️ 1. MÜHENDİSLİK MANİFESTOSU: "ÇALIŞIYORSA KURCALAMA"

Bu proje v10.0 sürümü itibarıyla üretim ve canlı test kararlılığına (LTS) ulaşmıştır. Yazılım ve mekatronik sistemlerde en kritik altın kural **"Çalışan sistemi gereksiz refactor veya riskli müdahalelerle bozmamak"**tır.

* **Sıfır Regresyon:** Çalışan çekirdek dosyalara (`smartpark.js`, `entrance.html`, `floor.html`, `app.html`, `guard.html`, `portal.html`) onaylanmamış keyfi kod müdahaleleri yapılmaz.
* **Gelecek Özellikler Yol Haritasına:** Akla gelen her yeni fikir, deneysel özellik veya donanım eklemesi doğrudan kod tabanına plansızca sokulmaz; önce bu dokümandaki **Gelecek Fazlar & Yapılacaklar (Backlog)** listesine eklenir ve mimari testleri tamamlandıktan sonra kontrollü şekilde devreye alınır.
* **Hata İzolasyonu & Dokümantasyon:** Oluşan her sorun kök neden analiziyle kayıt altına alınır (DEBUG logları).

---

## 🗺️ 2. FAZ 1'DEN FAZ 10'A GELİŞİM KRONOLOJİSİ

| Faz No | Faz Başlığı | Gerçekleştirilen Mühendislik ve Tasarım Adımları | Durum |
| :--- | :--- | :--- | :--- |
| **Faz 1** | **TÜRKPATENT Başvurusu & Prototip** | 150 slotluk temel simülasyon, TÜRKPATENT resmi başvurusu (`TR 2026/014052`), temel plaka tanıma ve dinamik tarife motoru. | ✅ Tamamlandı |
| **Faz 2** | **Şekli Eksiklik Düzeltmesi** | Uzman İbrahim Yiğit'in resmi bildirimine istinaden istemler, 5'erli satır numaralandırmaları ve resmi çizim revizyonları tamamlandı. | ✅ Tamamlandı |
| **Faz 3** | **1000 Slotluk Mega Kapasite** | 5 Kat × 200 Slot = 1000 Araçlık 3+1 Segregated Mimari kuruldu. Kat 1 (Zemin) SUV ve Ağır Vasıtalara ayrıldı, Kat 2-5 Sedan katı yapıldı. | ✅ Tamamlandı |
| **Faz 4** | **Deterministik Sıralı Dolum** | Araçların boş katlara rastgele zıplamasını engelleyen kategori öncelikli dolum algoritması (`Category-First Sequential`) geliştirildi. | ✅ Tamamlandı |
| **Faz 5** | **Minimalist Açık Tasarım** | Gözü yoran neon mavi cyberpunk tema yerine saf beyaz kartlar, yumuşak açık gri zemin (`#f8fafc`), zümrüt yeşili ve kehribar sarısı uygulandı. | ✅ Tamamlandı |
| **Faz 6** | **Çatı Güneş Enerjisi Santrali (GES)** | 1420 kWh'lik çatı GES modeli entegre edildi. Tesisin anlık üretim-tüketim dengesi ve net şebeke akışı canlı simüle edildi. | ✅ Tamamlandı |
| **Faz 7** | **5 Dakika Çıkış İhlali & Kara Liste** | Ödeme yapıp 5 dakika içinde çıkmayanlara 1. İhlalde 2x, 2. İhlalde 3x, 3. İhlalde 4x ceza ve Kalıcı Kara Liste (Bariyer Engeli) mekanizması getirildi. | ✅ Tamamlandı |
| **Faz 8** | **EV Vale Attendant & Çoklu Ekranlar** | Sürücü mobil uygulaması (`app.html`), güvenlik/şarj görevlisi el terminali (`guard.html`) ve şarjı biten aracın fişini çekme istasyonu oluşturuldu. | ✅ Tamamlandı |
| **Faz 9** | **DeepTech, Cloud AI & Hukuki Sözleşme** | NVIDIA Cloud NIM (Llama-3.2-Vision OCR), dinamik AVP otonom rota grafı (6 aşamalı A*), araç çağırma (Summon) ve TBK/KTK cezai yaptırım sözleşmesi kuruldu. | ✅ Tamamlandı |
| **Faz 10 (LTS)** | **Kararlılık, Hızlı Kiosk & Hafif Kat Tablosu** | 1-Tık Hızlı Araç Butonları, otomatik EV algılama, otomatik bariyer açılışı, Türkçe sesli anons, performans dostu Canlı Kat & Slot Yönetim Tablosu teslim edildi. | ✅ Tamamlandı (Kararlı) |

---

## 🛠️ 3. KRİTİK DEBUG & POST-MORTEM HATA GÜNLÜĞÜ (DEBUG-01 — DEBUG-13)

| Kod | Belirti & Problem | Kök Neden (Root Cause) | Uygulanan Kesin Mühendislik Çözümü |
| :--- | :--- | :--- | :--- |
| **DEBUG-01** | Kat Zıplama Hatası (İki TOGG'dan biri Kat 1, diğeri Kat 4'e gidiyordu). | Dinamik yük dengeleyici boş katları `%0` dolulukla görüp araçları üst katlara savuruyordu. | **Category-First Sequential:** Kat 1 dolmadan Kat 2'ye geçiş engellendi. |
| **DEBUG-02** | SUV Araçların Spiral Rampaya Girmesi. | Gövde tipi filtresi yoktu; ağır araçlar üst katlara tırmanabiliyordu. | **SUV $\to$ Kat 1 Kuralı:** SUV/Pickup araçlar 0-Rampa Zemin Kata kilitlendi. |
| **DEBUG-03** | Dropdown Menü Beyazlık Hatası. | İşletim sistemi yerel select bileşeni CSS arka planını eziyordu. | CSS `select`, `optgroup`, `option` etiketleri `#0f172a` ve `#ffffff` ile izole edildi. |
| **DEBUG-04** | 5 Dakika Ödeyip Çıkmama (Park İşgali). | Çıkış bariyeri ile ödeme zamanı arasındaki fark denetlenmiyordu. | **Kademeli Ceza Motoru:** 5 dk aşımında 2x, 3x, 4x ve kalıcı kara liste getirildi. |
| **DEBUG-05** | EV Şarj Soketinin Dolu Araçça Rehin Alınması. | Fiş çıkarma işlemi sürücüye bırakılmıştı. | **EV Valet Attendant:** Görevlinin tek tıkla fişi çekmesi sağlandı (`valetUnplugVehicle`). |
| **DEBUG-06** | Cyberpunk Renk Yorgunluğu. | Aşırı doygun mavi/mor tonlar okunabilirliği bozuyordu. | Açık minimalist tema: `#ffffff` kartlar, yumuşak gri zemin, zümrüt yeşili vurgular. |
| **DEBUG-07** | `smartpark.js` Syntax Error (Bariyer ve Uygulama Kilitlenmesi). | `guardInspectPlate` fonksiyonunda kapanış süslü parantezi unutulmuş ve mükerrer `getStats` kalmıştı. | Fonksiyon kapatıldı, mükerrer blok silindi, `window.SP` ve `global.SP` universal export güvenceye alındı. |
| **DEBUG-08** | Giriş Kiosku Model Seçim Hatası. | `entrance.html` içinde iki farklı `onModelChange()` fonksiyonu birbirini eziyordu. | Fonksiyonlar tek bir deterministik `onModelChange(userTriggered)` gövdesinde birleştirildi. |
| **DEBUG-09** | TOGG Seçildiğinde Otomatik Elektrikli Gelmemesi. | Model seçimi `selectProfileByName('EV_CHARGING')` fonksiyonunu doğrudan tetiklemiyordu. | 1-Tık Hızlı Seçim Butonları (`⚡ TOGG T10X`, `⚡ Tesla Model Y`) eklendi, otomatik profil seçimi bağlandı. |
| **DEBUG-10** | Giriş Kioskunda Kapının Açılmaması Algısı. | Kullanıcı aracı seçtikten sonra butonun pasif kalması veya bariyer hareketinin hissedilmemesi. | Araç tıklandığı anda `submitEntry()` otomatik çalıştırıldı, bariyer kolu CSS `-85°` kalktı, sesli Türkçe anons eklendi. |
| **DEBUG-11** | Kiosk Doluluk Haritasında Metinlerin Sıkışması. | 200 slotluk harita 20 sütunluk sabit ızgaraya sığdırılmaya çalışılıyordu. | Esnek `repeat(auto-fill, minmax(48px, 1fr))` yapısına ve koridor filtre sekmelerine (A, B, C, D..) geçildi. |
| **DEBUG-12** | `floor.html` 2D/3D Haritasının Bozuk/Açılmıyor Görünmesi. | Ağır 2D/3D costmap canvas render motoru tarayıcı kaynaklarını tüketiyor ve slotları eksik gösteriyordu. | Kullanıcı talimatıyla ağır 2D/3D ızgara tamamen iptal edildi; ultra hızlı, ferah ve okunabilir **Canlı Kat & Slot Yönetim Tablosu** kuruldu. |
| **DEBUG-13** | Hızlı Testlerde Plaka Çakışması Hatası. | Test sırasında aynı plaka (`34 TGG 100`) tekrar gönderildiğinde sistem "Araç Zaten İçeride" diyordu. | Giriş fonksiyonuna her tıklamada benzersiz plaka üreten rastgele kuyruk algoritması entegre edildi. |

---

## 🛠️ 4. FİZİKSEL HAYATTA İYİLEŞTİRİLMESİ GEREKEN 6 KRİTİK SAHA DURUMU

Yazılım simülasyonundan gerçek betonarme ve donanım kurulumuna geçildiğinde sahada çözülmesi gereken mühendislik başlıkları:

### 1. 🔋 Şarjı Dolan Aracın Otonom Yer Değiştirmesi (Autonomous Relocation)
* **Saha Problemi:** Şarj görevlisi fişi çekse bile araç şarj yuvasında (Row C) durmaya devam ettiği için arkadan gelen EV şarj istasyonuna yanaşamaz.
* **Fiziksel Çözüm:** Şarj tamamlanıp vale fişi kilit mekanizmasından çıkardığında, araca V2I sinyaliyle *"Yanındaki boş standart slota (Row D..H) otonom geç"* komutu verilmeli; 120kW DC şarj istasyonu hemen arkadaki araca tahsis edilmelidir.

### 2. 📅 Rezervasyon Çakışması ve Sarı Slot Ön-Kilitleme (Slot Pre-Locking)
* **Saha Problemi:** Bir müşteri evinden `Kat 1 / C-01` rezervasyonu yaptığında, otoparka plansız gelen bir sürücü kapıdan geçip bu yeri kapabilir.
* **Fiziksel Çözüm:** Rezervasyon oluşturulduğu anda fiziksel park yerindeki **Tavan RGB Lambası SARI yanmalı** ve slottaki elektromekanik zemin bariyeri (park lock) yukarı kalkarak habersiz girişleri engellemelidir.

### 3. 🔥 Dikey Yangın & Termal Kaçak (Thermal Runaway İzolasyonu)
* **Saha Problemi:** 1000 araçlık kapalı binada 100 adet 120kW hızlı şarj çalışırken lityum-iyon bataryada termal kaçak başlarsa zehirli duman spiral rampalardan üst katlara hızla tırmanabilir.
* **Fiziksel Çözüm:** Şarj sıralarının (Row C) üstüne tavan içi **Otomatik Duman Perdesi (Fire Smoke Curtain)** ve **Aerosol Yangın Söndürme Nozulları** konulmalıdır. O kattaki spiral rampa duman damperleri milisaniyede kapanıp spiral rampayı duman bacası olmaktan korumalıdır.

### 4. 📶 Betonarme İçinde Radyo & LiDAR Kör Noktaları
* **Saha Problemi:** Çok katlı binalardaki 40-50 cm kalınlığındaki perde beton kolonlar Wi-Fi ve UWB radyo frekanslarını absorbe eder, kör noktalar yaratır.
* **Fiziksel Çözüm:** Koridor tavanlarına her 15 metrede bir yerleştirilen **Mesh UWB Beacon ağı** kurulmalı; sinyal tek bir merkezi antenden değil, tavan lambaları üzerinden atlamalı (daisy-chain) taşınmalıdır.

### 5. 🛞 Tekerlek Kilidi Yerine Çıkış Bariyer Kilit & HGS Entegrasyonu
* **Saha Problemi:** Tekerlek kilidi takmak sahada sürücüyle güvenlik arasında fiziksel sürtüşmeye yol açar ve personeli meşgul eder.
* **Fiziksel Çözüm:** Ceza tahsilatı çıkış bariyerinde dijital olarak yapılır. Plakaya borç işlenir ve Türkiye Noterler Birliği / HGS / Karayolları veri tabanı ile entegre olunarak ceza bedeli aracın ilk HGS geçişinden veya araç satışından otomatik tahsil edilir.

### 6. ☀️ Çatı GES Panellerinin Toz/Kir Verim Kaybı
* **Saha Problemi:** Şehir içi tozu güneş panellerinin elektrik üretimini %20-30 oranında düşürür.
* **Fiziksel Çözüm:** Çatıya yağmur suyu toplama deposuna bağlı **Otomatik Robotik Panel Temizleme Rayları (Robotic Wiper)** planlanmalıdır.

---

## 🏛️ 5. YENİ AR-GE VE PROTOKOL MİMARİSİ: RESMİ (SİYAH) & DİPLOMATİK (YEŞİL) PLAKA PARK DÜZENİ

Kamu görevlileri, askeri erkan ve yabancı diplomatik misyon araçlarının otoparka kabulü, güvenliği ve tahsisi için tasarlanan ileri seviye protokol mimarisi:

### A. Araç ve Plaka Sınıflandırması
1. **Siyah Zemin Üzerine Beyaz Karakterli Plakalar (Resmi Hizmete Mahsus Devlet Araçları):**
   * **Kapsam:** TSK / Askeri Garnizon ve Tugay Komutanlıkları, İl/İlçe Emniyet Müdürlükleri (Polis), Valilik & Kaymakamlık Makam Araçları, Cumhuriyet Başsavcılıkları, MİT, Devlet Denetleme ve Kamu Müfettişleri.
   * **Örnek Format:** `06 ...`, `34 ...` siyah zeminli resmi plakalar.
2. **Yeşil Zemin Üzerine Beyaz Karakterli Plakalar (Diplomatik Misyon & Konsolosluk Araçları):**
   * **Kapsam:** Büyükelçilikler (`CD` - Corps Diplomatique), Konsolosluklar (`CC` - Corps Consulaire), Uluslararası Misyon Şefleri ve Ataşeler.
   * **Örnek Format:** `34 CD 001`, `06 CC 100` yeşil zeminli resmi plakalar.

### B. Protokol Park ve Güvenlik İşletim Modeli
1. **Çift Renk Spektrumlu OCR Algılama (NVIDIA NIM Metropolis Vision):**
   * Giriş kamerasındaki yapay zeka sadece karakterleri değil, plakanın renk histogramını da denetler. Siyah veya yeşil zemin algılandığı anda sistem *"Protokol / Resmi Araç"* modunu devreye sokar.
2. **Kat 1 Zemin Kat Güçlendirilmiş Protokol Peronu (Row P / Row K):**
   * **0-Rampa Kuralı:** Güvenlik ve sabotaj riski nedeniyle resmi ve diplomatik araçlar kesinlikle spiral rampadan üst katlara çıkartılmaz.
   * **Zırhlı Araç Statik Yük Desteği:** Mercedes S-Guard, Audi A8 Security, Toyota Land Cruiser Armor gibi 3.5 - 4.5 tonluk zırhlı araçlar için Kat 1'de 5000 kg aks taşıma kapasiteli özel güçlendirilmiş peronlar tahsis edilir.
   * **Doğrudan Çıkış & Güvenlik Görüşü:** Protokol slotları ana güvenlik kulübesinin (`guard.html`) doğrudan 15 metre görüş açısında ve binadan acil tahliye arteri üzerindedir.
3. **₺0 Ücret ve Yasal Muafiyet:**
   * 237 sayılı Taşıt Kanunu ve Viyana Diplomatik İlişkiler Sözleşmesi uyarınca resmi ve diplomatik araçlara hiçbir otopark ücreti, bekleme bedeli veya gecikme cezası uygulanmaz (Tarife: ₺0 / Tam Muafiyet).
   * Kapıya yaklaştığında bariyer duraksamadan otomatik kalkar.
4. **Güvenlik Terminali Sessiz Alarmı (Silent Protocol Alert):**
   * Araç bariyere girdiği anda güvenlik görevlisinin el terminaline (`guard.html`) *"DİKKAT: Resmi/Diplomatik Heyet Giriş Yaptı - Peron P-01"* şeklinde sessiz titreşimli ikaz gönderilir. Güvenlik personeli peronda karşılama yapar.
   * Slot çevresinde LiDAR tabanlı 1.5 metrelik sanal güvenlik çemberi oluşturulur; yetkisiz yaklaşmalar güvenlik ekranında anlık uyarı verir.

---

## 🔮 6. GELECEK FAZLAR & YAPILACAKLAR LİSTESİ (BACKLOG)

> [!NOTE]
> *"Çalışıyorsa kurcalama"* ilkesi uyarınca, aşağıdaki başlıklar mevcut v10.0 kod tabanına plansızca entegre edilmeyecek; her biri kendi fazı geldiğinde izole dalda (branch) geliştirilecektir.

* [ ] **Faz 11: 3D Dijital İkiz (WebGL Three.js & NVIDIA Isaac Sim):**
  * `floor.html` için hafifletilmiş, GPU hızlandırmalı, 60 FPS WebGL 3D otopark izleme katmanı.
  * Gerçek LiDAR nokta bulutu (Point Cloud) ve kolon-duvar çarpışma korumalı görsel model.
* [ ] **Faz 12: Otonom Şarj Sonrası Yer Değiştirme Simülasyonu:**
  * Mobil uygulamaya *"Şarj Bitti ➔ Araç Normal Slota Otomatik Park Etti"* V2I senaryosunun eklenmesi.
* [ ] **Faz 13: IoT Zemin Kilidi ve Akıllı Tavan RGB Lambası Modülü:**
  * Rezerve edilen yerlerin sarı renkli yanması ve elektromekanik kilit animasyonu.
* [ ] **Faz 14: e-Tutanak Yazdırma ve Zabıta/Emniyet Webhook API:**
  * Güvenlik el terminalinden (`guard.html`) KTK m.61 ihlali için PDF formatında resmi tutanak dökümü alma.
* [ ] **Faz 15: HGS / Karayolları Otomatik Borç Tahsilat Entegrasyonu:**
  * Bariyerden kaçan veya borcunu ödemeyen araçlar için PTT HGS borç bildirim simülasyonu.
* [ ] **Faz 16: Resmi (Siyah) & Diplomatik (Yeşil) Plaka Protokol Yönetim Modülü:**
  * Siyah ve yeşil plaka OCR tanıma, Kat 1 Zemin Protokol Koridoru tahsisi, ₺0 muafiyet ve güvenlik terminali protokol eskort bildirimi.

---

## 📊 7. DOSYA SAĞLIK VE KARARLILIK MATRİSİ

| Dosya | Görevi | Kararlılık Statüsü | Son İşlem |
| :--- | :--- | :--- | :--- |
| [`smartpark.js`](file:///c:/Users/LENOVO/Documents/oto/smartpark.js) | Çekirdek Motor, NIM API, Rota Grafı, Veri Tabanı | 🟢 **%100 Sağlıklı** | Syntax hatası giderildi, universal export aktif |
| [`entrance.html`](file:///c:/Users/LENOVO/Documents/oto/entrance.html) | Giriş Kiosku, Hızlı Butonlar, Bariyer & Ses | 🟢 **%100 Sağlıklı** | 1-Tık TOGG/Tesla butonları, otomatik açılış eklendi |
| [`floor.html`](file:///c:/Users/LENOVO/Documents/oto/floor.html) | Canlı Kat & Slot Yönetim Tablosu | 🟢 **%100 Sağlıklı** | Ağır 2D/3D kaldırıldı, hızlı tablo kuruldu |
| [`app.html`](file:///c:/Users/LENOVO/Documents/oto/app.html) | Sürücü Mobil Simülatörü, Navigasyon, Summon | 🟢 **%100 Sağlıklı** | Canlı AVP rota ve ceza sayacı aktif |
| [`guard.html`](file:///c:/Users/LENOVO/Documents/oto/guard.html) | Güvenlik & Şarj Vale Terminali | 🟢 **%100 Sağlıklı** | Fiş çekme ve ceza tutanağı aktif |
| [`portal.html`](file:///c:/Users/LENOVO/Documents/oto/portal.html) | Web Portalı, 2FA Ruhsat Devri, Rezervasyon | 🟢 **%100 Sağlıklı** | Dinamik QR ve VIP rezervasyon aktif |
| [`upcoming.html`](file:///c:/Users/LENOVO/Documents/oto/upcoming.html) | Yakında Eklenecekler & AR-GE Laboratuvarı | 🟢 **%100 Sağlıklı** | "Çalışıyorsa kurcalama" ilkesi ve gelecek fazlar vitrini |

---

*Bu belge, projenin endüstriyel kararlılığını korumak ve tüm geliştirme geçmişini kayıt altında tutmak amacıyla düzenli olarak güncellenmektedir.*

