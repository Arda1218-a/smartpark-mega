# ⚖️ SMARTPARK DEEPTECH — HUKUKİ YÖNETMELİK, İHLAL YAPTIRIMLARI VE KULLANICI SÖZLEŞMESİ
**Patent Başvuru No:** `TR 2026/014052`  
**Buluş Sahibi:** Arda CENGİZ  
**Sürüm:** v9.8 — Hukuki Güvence & İdari Yaptırım Modeli  

---

## 📌 1. HUKUKİ DAYANAKLAR VE MEVZUAT ÇERÇEVESİ

SmartPark tesisine giriş yapan her sürücü ile işletme arasında Türk Hukuku uyarınca **"Karma Nitelikli Otopark İşletme ve Saklama (Vedia) Sözleşmesi"** (TBK m. 502 vd.) kurulmuş sayılır.

| İlgili Mevzuat | Madde / Hüküm | Uygulama ve Dayanak |
| :--- | :--- | :--- |
| **Türk Borçlar Kanunu (TBK)** | **m. 179 - m. 182** (Ceza Koşulu / İhbar) | Sözleşmeye aykırı hatalı park veya süre aşımında kademeli cezai şart uygulanması. |
| **Karayolları Trafik Kanunu (KTK)** | **m. 61/o** (Engelli Park Alanı İhlali) | Engelli araç park yerlerine engelsiz araçların park etmesi durumunda 2 kat para cezası ve çekici işlemi. |
| **Türk Ceza Kanunu (TCK)** | **m. 179** (Trafik & Yapı Güvenliğini Tehlikeye Sokma) | Taşıma kapasitesi üstünde ağır araçların (SUV/Pickup) üst kat kule rampalarını zorlaması halinde doğan kamu davası hakkı. |
| **6502 Sayılı Tüketicinin Korunması Kanunu** | **m. 5** (Açık Bilgilendirme İlkesi) | Giriş bariyerinde ve dijital ekranda tarife ve kuralların açıkça ilan edilmesi suretiyle zımni rıza oluşumu. |
| **6698 Sayılı KVKK** | **m. 5/2-f** (Meşru Menfaat & Tesis Güvenliği) | Plaka tanıma, LiDAR ve tavan kameralarıyla araç güvenliğinin ve otopark nizamının sağlanması. |

---

## 🚦 2. GİRİŞTE "ZIMNİ SÖZLEŞME" (IMPLIED CONSENT) NASIL KURULUR?

1. **Giriş Kiosk Ekranı & Hukuki İlan:**  
   Bariyer açılmadan önce ekranda:  
   *"Bu tesise giriş yapan sürücüler SmartPark Tesis Yönetmeliğini, 5 Dakika Çıkış Kuralını ve İhlal Tarifelerini zımnen kabul etmiş sayılır."* uyarısı yer alır.
2. **Kamera & Plaka Zaman Damgası:**  
   Aracın giriş anı milisaniyelik `ISO 23374` telemetri logu ile şifrelenerek saklanır; inkâr edilemez hukuki delil (HMK m. 199 Elektronik Belge) teşkil eder.

---

## 🛑 3. ÖZEL İHLAL SENARYOLARI VE KADEMELİ YAPTIRIMLAR

### ♿ İHLAL 1: Engelli (Row A) Alanına Yetkisiz / Bilerek Park Etme
* **Senaryo:** Sürücü engelli olmadığı halde AVM kapısına veya asansöre yakın diye Row A'ya bilerek park eder.
* **Hukuki Yaptırım:**
  1. **İdari Bildirim:** Sistem, emniyet/zabıta e-Tutanak modülüne KTK m. 61/o uyarınca otomatik fotoğraf ve plaka ihlal bildirimi düşer.
  2. **Tesis İçi Ceza Koşulu:** ₺2.500 "Haksız Öncelik Kullanım & İhlal Bedeli" çıkış faturasına eklenir.
  3. **Görsel İkaz:** Tavan lambası kırmızı acil durum çakarına geçer.
  4. **Tekerrür:** 2. kez aynı ihlali yapan araç, kat içi manevra çekicisiyle **Zemin Kat Bypass Güvenlik Alanına** çekilir; çekici ve otopark çekme masrafı sürücüye fatura edilir.

---

### 🌸 İHLAL 2: Kadın / Aile (Row B) Alanına Yetkisiz Park
* **Senaryo:** Yalnız erkek sürücünün Row B'yi işgal etmesi.
* **Hukuki Yaptırım:**
  1. **1. Aşama:** Güvenlik el terminaline anlık devriye bildirimi düşer, sürücünün cep telefonuna SMS/Uygulama uyarısı gönderilir.
  2. **2. Aşama:** 15 dakika içinde araç yer değiştirilmezse, otoparkın saatlik ücretine **3 Kat ($3\times$) Ceza Tarifesi** işletilir.

---

### ⚡ İHLAL 3: Yeşil Enerji Altyapısı Engelleme (ICEing) ve İnatla Standart Yere Park
* **Senaryo A (ICEing):** Benzinli/Dizel aracın 120kW DC Şarj İstasyonuna (Row C) park ederek elektrikli aracın şarj olmasını engellemesi.
* **Senaryo B (EV İnadı):** Elektrikli SUV kullanıcısının kendisine ayrılan şarj hubı yerine inatla başka araçların hakkı olan standart slotları işgal etmesi.
* **Hukuki Yaptırım:**
  1. **Yeşil Enerji Fırsat Maliyeti:** Saat başı normal ücrete ek olarak **₺350 "Atıl Şarj Kapasitesi Tazminatı"** tahsil edilir.
  2. Şarjı %100 dolduğu halde istasyondan ayrılmayan araçlar için şarj görevlisi fişi çeker; araç 10 dakika içinde alanı boşaltmazsa dakikası ₺10 işgal bedeli yansıtılır.

---

### ⏱️ İHLAL 4: Park Ücreti Ödeyip Çıkmama (5 Dakika Otopark İşgali)
* **Senaryo:** Sürücü 1 saatlik ücreti öder fakat 6 saat boyunca içeride kalmaya devam eder.
* **Hukuki Yaptırım:**
  * **5 Dakika Tolerans:** Ödeme sonrası 5 dakika içinde bariyerden çıkış serbesttir.
  * **1. İhlal:** Gecikilen sürenin **2 Katı ($2\times$)** ceza.
  * **2. İhlal:** Gecikilen sürenin **3 Katı ($3\times$)** ceza.
  * **3. İhlal:** Gecikilen sürenin **4 Katı ($4\times$)** ceza + **SİSTEMDEN KALICI MEN (Bariyer Kara Listesi)**.
  * Ödenmeyen bakiye, plaka üzerinden İcra İflas Kanunu (İİK m. 68) kapsamında ilamsız icra takibiyle tahsil edilir.

---

### 🛑 İHLAL 5: Ağır/SUV Araçların Üst Kat Spiral Rampalarını Zorlaması
* **Senaryo:** Ağır pickup veya SUV sürücüsünün Kat 1 yerine statik yük limiti olan Kat 2–5 kule rampalarına tırmanması.
* **Hukuki Yaptırım:**
  * **Statik Yapı Tehlike Bedeli:** ₺5.000 cezai şart faturaya yansıtılır.
  * Olay anında güvenlik terminaline **"KRİTİK MİMARİ RİSK"** alarmı düşer, araç kule girişindeki otomatik kilit bariyeriyle Zemin Kata zorunlu bypass edilir.

---

## 💡 4. YAPAY ZEKANIN STRATEJİK HUKUKİ ÖNERİLERİ (BEST PRACTICES)

Sistemin Tüketici Hakem Heyetleri veya mahkemelerde takılmaması için şu 4 altın kural uygulanmalıdır:

1. **"Tekerlek Kilidi (Wheel Clamp)" Yerine "Bariyer Blokajı":**  
   Fiziksel tekerlek kilidi bazı mahkemelerde *"hürriyeti tahdit"* veya *"mülkiyet hakkına müdahale"* olarak yorumlanabilmektedir. Bunun yerine **çıkış bariyerinin kalkmaması ve dijital icra takibi başlatılması** hukuken %100 risksiz ve meşrudur.
2. **Kamera Fotoğraf Delili ile Elektronik Tutanak:**  
   Her ihlalin tavan kamerası tarafından geniş açı ve plaka açısıyla çekilmiş yüksek çözünürlüklü fotoğrafı sistemde HMK m. 199 kapsamında kriptolu delil olarak saklanmalıdır.
3. **Orantılılık İlkesi:**  
   Cezalar *"fahiş ve cezalandırıcı"* değil, *"otoparkın doluluk kaybını ve kamu düzenini telafi edici (tazminat niteliğinde)"* formüle edilmelidir.
4. **HGS / e-Devlet Entegrasyonu:**  
   Gelecek fazda Türkiye Noterler Birliği ve Karayolları HGS sistemiyle entegre olunarak çıkışta ödenmeyen otopark ve ceza bedelleri doğrudan araç tescil borcuna veya HGS hesabına otomatik yansıtılmalıdır.

---

*Bu belge, SmartPark Mega Hub projesinin ticari işletme sözleşmelerine ve patent savunma dosyasına hukuki ek olarak hazırlanmıştır.*
