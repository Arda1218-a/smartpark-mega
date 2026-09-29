# T.C. TÜRK PATENT VE MARKA KURUMU
## PATENT BAŞVURU DOSYASI

---

### 1. BULUŞ BAŞLIĞI
**FİZİKSEL BOYUT VE AKS YÜKÜ FİLTRELİ, ÇOK KAPILI VARYANS MİNİMİZASYONLU DENGELİ OTOPARK İŞLETİM VE DENETİM SİSTEMİ**

---

### 2. ÖZET
Bu buluş; kapalı otopark tesislerinde araç kabulü, yer tahsisi, operasyonel güvenlik ve ücretlendirme süreçlerini yöneten akıllı bir otopark kontrol sistemidir. Buluş; otopark giriş kapılarında konumlandırılan aks kantarı (11) ve LiDAR tavan yükseklik sensörü (12) ile araçların fiziksel kütle ve yükseklik profilini ölçerek, 2.5 ton üzeri ve 2.10 metre üzerindeki ağır ve yüksek araçları zorunlu olarak güçlendirilmiş zemin kata (Kat 1) yönlendiren; standart araçları ise katlar arası varyans minimizasyonu ($\min \sigma^2$) algoritması ile homojen dağıtan bir merkezi işlem birimi (10) içermektedir. Buluş ayrıca, yanlış park ihlallerini metal plakadan bağımsız olarak sürücü kimliği (21) ile eşleştiren 2 adımlı araç sahiplik devri protokolü (20), her katta yer alan elektrikli araç şarj istasyonu (15) çatışma çözücü algoritması ve dakika hassasiyetli kademeli fiyatlandırma mekanizması ile karakterize edilmektedir.

---

### 3. TARİFNAME

#### A. Buluşun İlgili Olduğu Teknik Alan
Buluş; akıllı ulaşım sistemleri (ITS), otopark yönetim altyapıları, araç ağırlık ve boyut algılama sensörleri, dağıtık kapı kuyruk arbitrajı ve elektrikli araç şarj yönetim teknolojileri ile ilgilidir.

#### B. Tekniğin Bilinen Durumu (Önceki Teknik)
Geleneksel otopark sistemlerinde araçlar boş bir kata veya ilk kata sırayla yığılmakta, bu durum kat rampalarında ve koridorlarda trafik kilitlenmelerine (gridlock) yol açmaktadır. Ayrıca yüksek tavanlı (SUV, Pickup) veya ağır tonajlı araçların tavan yüksekliği ve zemin taşıma kapasitesi kontrol edilmeksizin üst katlara kabul edilmesi ciddi yapısal hasarlara sebep olmaktadır. Mevcut sistemlerde cezalar yalnızca plakaya kesilmekte, araç el değiştirdiğinde masum yeni araç sahipleri mağdur olmaktadır.

#### C. Buluşun Çözdüğü Teknik Problemler
1. Rampa ve koridorlardaki araç yığılmalarını kat doluluk varyansını minimize ederek engellemek.
2. Ağır ve yüksek araçların üst kat tavan ve zeminlerine zarar vermesini giriş kantar/LiDAR filtresiyle fiziksel olarak önlemek.
3. Araç satışlarında geçmiş cezaların yeni araç sahibine geçmesini engelleyen 2 adımlı sürücü-plaka ayrıştırma altyapısı sunmak.
4. Elektrikli araçların normal park yerine gitmeyip doğrudan şarj istasyonuna yönelmesi durumunda ceza kesilmesini önleyen akıllı tarife geçişi sağlamak.

#### D. Şekillerin Açıklaması
* **Şekil 1:** Çok kapılı giriş sensör dizisi ve merkezi işlem mimarisi blok diyagramı.
* **Şekil 2:** Varyans minimizasyonlu dengeli kat doluluk algoritması akış şeması.
* **Şekil 3:** 2 Adımlı araç sahiplik devri ve sürücü ceza ayrıştırma protokolü.

#### E. Parça ve Referans Numaraları
* **(10)** Merkezi Kontrol ve Dağıtım Ünitesi
* **(11)** Aks Kantarı (Load-Cell Ağırlık Sensörü)
* **(12)** LiDAR / Lazer Tavan Yükseklik Sensörü
* **(13)** Dağıtık Giriş Kapıları (Kuzey, Güney, Doğu, Batı)
* **(14)** Güvenlik Bariyeri ve Hibrit Bilet Yazıcı
* **(15)** 120 kW Hızlı DC EV Şarj İstasyonları
* **(16)** Çıkış Bypass ve Tahliye Şeridi
* **(20)** 2FA Araç Sahiplik Devir Modülü
* **(21)** Sürücü Kimlik ve Ceza Veritabanı

#### F. Buluşun Detaylı Açıklaması
Giriş kapısına (13) yanaşan bir aracın ağırlığı aks kantarı (11) ile, tavan yüksekliği LiDAR sensörü (12) ile milisaniyeler mertebesinde ölçülür. Ölçülen kütle değeri 2500 kg'dan veya yükseklik değeri 2100 mm'den büyükse, merkezi kontrol ünitesi (10) bu aracı zorunlu olarak yalnızca Kat 1'deki güçlendirilmiş slotlara tahsis eder. Kat 1'deki ağır araç kapasitesi dolu ise güvenlik bariyeri (14) açılmaz ve araç çıkış bypass şeridine (16) yönlendirilir.

Standart araçlar için merkezi kontrol ünitesi (10), $K$ adet kat arasındaki doluluk oranlarının varyansını hesaplar:
$$\min \sigma^2 = \frac{1}{K}\sum_{f=1}^{K}(O_f - \bar{O})^2$$
Araç, o an doluluk yüzdesi en düşük olan kata atanarak katlar arası homojen doluluk sağlanır.

Hatalı park durumunda ceza puanı plaka yerine sürücü profiline (21) işlenir. Araç satıldığında yeni sahip 2FA devir modülü (20) ile plakayı kendi profiline bağlar; plaka üzerindeki kısıtlamalar sıfırlanırken eski sahibin sicilindeki cezalar korunur.

---

### 4. İSTEMLER (CLAIMS)

**İstem 1:** Akıllı bir kapalı otopark yönetim sistemi olup;
* Otopark girişinde araç kütlesini ölçen en az bir aks kantarı (11),
* Araç yüksekliğini ölçen en az bir tavan LiDAR sensörü (12),
* Araçları katlara doluluk varyansını minimize ederek yönlendiren bir merkezi kontrol ünitesi (10) ile **karakterize edilen otopark kontrol sistemi.**

**İstem 2:** İstem 1'e uygun bir sistem olup; ölçülen kütlenin 2500 kg üzerinde veya yüksekliğin 2100 mm üzerinde olması halinde aracı yalnızca güçlendirilmiş Kat 1 slotlarına yönlendiren, Kat 1 dolu olduğunda bariyeri (14) kilitleyip aracı bypass şeridine (16) sevk eden güvenlik kilidi mekanizması ile **karakterize edilmektedir.**

**İstem 3:** İstem 1'e uygun bir sistem olup; araçları katlara atarken kat doluluk oranlarının ($O_f$) ortalama doluluktan ($\bar{O}$) olan varyansını ($\sigma^2$) minimize edecek şekilde en az dolu kata dinamik yönlendirme yapan dağıtım algoritması ile **karakterize edilmektedir.**

**İstem 4:** İstem 1'e uygun bir sistem olup; park ihlal cezalarını doğrudan sürücü kimlik hesabına (21) kaydeden, araç el değiştirdiğinde iki faktörlü (2FA) doğrulama kodu ile plakanın yeni sahibine temiz sicille devredilmesini sağlayan araç sahiplik devir modülü (20) ile **karakterize edilmektedir.**

**İstem 5:** İstem 1'e uygun bir sistem olup; elektrikli bir aracın tahsis edilen normal slot yerine doğrudan katta yer alan elektrikli şarj istasyonuna (15) park etmesi halinde ceza ihlali oluşturmayarak sistemi otomatik olarak şarj tarifesine geçiren akıllı çatışma çözücü algoritması ile **karakterize edilmektedir.**

**İstem 6:** İstem 1'e uygun bir sistem olup; ilk 60 dakika için her dakika başına $1.0\text{ TL}$, 60 dakikadan sonraki süreler için ise tam saat tabanı ile artık dakika çarpanının ($H \times 60 + H \times M$) toplanmasıyla hesaplanan kademeli dakika fiyatlandırma motoru ile **karakterize edilmektedir.**

**İstem 7:** İstem 1'e uygun bir sistem olup; akıllı telefon veya QR koda sahip olmayan sürücüler için tek tıkla barkodlu kağıt bilet üreten ve çıkışta görevliye nakit ödeme imkanı sağlayan hibrit gişe ünitesi ile **karakterize edilmektedir.**
