# 🏗️ EsnovaBeton — cPanel, Altyapı & Trello Görev Panosu

Bu rehber cPanel, e-posta, Cloudflare ve web kurulum adımlarını içerir.

## 🌐 Faz 0: Domain, cPanel & E-posta Altyapısı (BUGÜN)
### 📧 cPanel Üzerinden info@esnovabeton.com E-posta Açılışı
**Açıklama:** cPanel > E-posta Hesapları > Oluştur adımıyla info@esnovabeton.com, satis@esnovabeton.com ve teklif@esnovabeton.com kurumsal hesapları açılacaktır.

**Etiketler:** `Altyapı, Kritik`  
**Kontrol Listesi:**
- [ ] info@esnovabeton.com oluşturuldu
- [ ] satis@esnovabeton.com oluşturuldu
- [ ] E-posta yönlendirmesi kişisel Gmail'e bağlandı
- [ ] Mobil telefon IMAP/SMTP kurulumu yapıldı

---

### ☁️ Cloudflare DNS, SSL & DDoS Koruma Entegrasyonu
**Açıklama:** Cloudflare üzerinde ücretsiz hesap açılıp esnovabeton.com eklenecek, NS adresleri domain kaydediciye girilip 5.180.185.253 IP'si yönlendirilecektir.

**Etiketler:** `Altyapı, Güvenlik`  
**Kontrol Listesi:**
- [ ] Cloudflare hesabı oluşturuldu
- [ ] Domain NS adresleri güncellendi
- [ ] Ücretsiz SSL ve Edge Caching aktifleştirildi

---

### 📁 cPanel public_html Yayın Klasörü Hazırlığı
**Açıklama:** cPanel Dosya Yöneticisi > /home/esnovabe/public_html içerisindeki eski varsayılan dosyalar temizlenecek, ilk karşılama sayfası yüklenecektir.

**Etiketler:** `Altyapı`  
**Kontrol Listesi:**
- [ ] Eski index.html temizlendi
- [ ] Geçici 'Yakında Hizmetinizde' açılış sayfası eklendi

---

## 📌 Faz 1: Marka & Derin Pazarlama Araştırması (1. Gün)
### 🔍 Rakip Beton Firmaları Analizi (Türkiye & Dünya)
**Açıklama:** Akçansa, Çimsa, Oyak Beton, Holcim, CEMEX, Heidelberg Materials firmalarının web siteleri, renk paletleri, görsel dilleri ve teklif alma mekanizmaları incelenmiştir.

**Etiketler:** `Araştırma, Kritik`  
**Kontrol Listesi:**
- [ ] Türk beton devleri web incelemesi
- [ ] Küresel beton devleri web incelemesi
- [ ] Teklif alma & Metreküp hesaplayıcı kıyaslaması

---

### 🎨 Beton Sektörü Renk Paleti & Psikoloji Raporu
**Açıklama:** Beton grisi (#4A5568), Güven Mavisi (#1E3A8A), Şantiye Turuncusu (#EA580C) ve Çevre/Sürdürülebilirlik Yeşili (#059669) dengesi ve renk psikolojisi raporlanmıştır.

**Etiketler:** `Tasarım, Kurumsal Kimlik`  
**Kontrol Listesi:**
- [ ] Ana renk seçimi (Primary)
- [ ] Vurgu rengi (Accent)
- [ ] Endüstriyel ikonografi & Lucide Icon set

---

### 🤖 AI_RESEARCH_PROMPTS.md Promptlarının Çalıştırılması
**Açıklama:** ChatGPT, Claude, Perplexity ve Gemini Deep Research araçlarına hazırlanan 4 ana prompt girilecek, derin raporlar toplanacaktır.

**Etiketler:** `AI Prompt, Araştırma`  
**Kontrol Listesi:**
- [ ] Prompt 1 (Rakip Analizi) çalıştırıldı
- [ ] Prompt 2 (Renk Stratejisi) çalıştırıldı
- [ ] Prompt 3 (Web UX & Metreküp Hesaplayıcı) çalıştırıldı
- [ ] Prompt 4 (360° Pazarlama) çalıştırıldı

---

## 🎨 Faz 2: Kurumsal Kimlik & Görsel Hafıza (2-3. Gün)
### ✏️ EsnovaBeton Logo & Vektörel Amblem Tasarımı
**Açıklama:** Beton mikseri, sağlamlık geometrisi, küp basınç test simgesi ve dinamik E/B harf yapısıyla akılda kalıcı 3 alternatif amblem çizimi.

**Etiketler:** `Kurumsal Kimlik`  
**Kontrol Listesi:**
- [ ] Vektörel logo alternatifleri
- [ ] Kartvizit & Başlıklı Kağıt
- [ ] Transmiksör & Pompa Araç Giydirme Tasarımı

---

### 📐 Tipografi & Slogan (Value Proposition)
**Açıklama:** 'Geleceğin Sağlam Temelleri', 'Yüksek Dayanım, Zamanında Teslimat' vb. slogan varyasyonları ve modern tipografi (Inter / Outfit / Roboto).

**Etiketler:** `Kurumsal Kimlik`  
**Kontrol Listesi:**
- [ ] Kurumsal Slogan Seçimi
- [ ] Font Ailesi Tanımlamaları
- [ ] Kullanım Kılavuzu (Brand Guidelines)

---

## 💻 Faz 3: Web Sitesi Mimarisi & UI/UX (4-7. Gün)
### 🏗️ Hero Bölümü & Likit Cam / WebGL Görsel Efektler
**Açıklama:** Kullanıcıyı ilk bakışta büyüleyecek 'WOW Factor' Likit Cam / WebGL parçacık efektli interaktif Hero alanı ve Bento Grid KPI kartları.

**Etiketler:** `Web Geliştirme, UI/UX`  
**Kontrol Listesi:**
- [ ] Hero Alanı Tasarımı
- [ ] Bento Grid KPI Kartları (Yıllık Kapasite, Tesis Sayısı, Pompa Parkı)
- [ ] Mobil Uyumlu 44px Dokunma Hedefleri

---

### 🧮 İnteraktif Metreküp & Pompa Hesaplayıcı Modülü
**Açıklama:** Müteahhitlerin ve bireysel yapı sahiplerinin en-boy-yükseklik girerek ihtiyaç duyduğu hazır beton miktarını (m³) ve pompa tipini hesaplayan interaktif araç.

**Etiketler:** `Web Geliştirme, Özellik`  
**Kontrol Listesi:**
- [ ] En-Boy-Yükseklik Girdi Alanları
- [ ] Beton Sınıfı Seçimi (C25/30, C30/37, C35/45, C40/50)
- [ ] Teklif Al Butonu Entegrasyonu

---

### 📜 Ürünler, Beton Sınıfları & Kalite Laboratuvarı Sayfası
**Açıklama:** Kırılma basınç testleri, Ar-Ge laboratuvarı, brüt beton, şap betonu, kendiliğinden yerleşen beton (KYB) ürün katalog ekranları.

**Etiketler:** `Web Geliştirme`  
**Kontrol Listesi:**
- [ ] Beton Sınıf Kartları
- [ ] Kalite Belgeleri & ISO Sertifikaları
- [ ] Laboratuvar Test Görselleri

---

## 📝 Faz 4: İçerik, SEO & B2B Formlar (8-10. Gün)
### 🎯 B2B Müteahhit & Şantiye Hızlı Teklif Formu
**Açıklama:** Şantiye adresi, döküm tarihi, döküm hızı (m³/saat) ve pompa ihtiyacı içeren dinamik teklif talebi formu (info@esnovabeton.com entegreli).

**Etiketler:** `İçerik, SEO`  
**Kontrol Listesi:**
- [ ] Form Alanları Tasarımı
- [ ] WhatsApp Hızlı Döküm Hattı Entegrasyonu
- [ ] Form Onay & E-posta Bildirimi

---

### 🔎 Hazır Beton SEO & AIO (Yapay Zeka Arama) Optimizasyonu
**Açıklama:** 'Hazır beton fiyatları', 'C30 beton metreküp fiyatı', 'Pompalı beton dökümü' anahtar kelimeleri ve JSON-LD şema verileri.

**Etiketler:** `SEO`  
**Kontrol Listesi:**
- [ ] Meta Başlık ve Açıklamalar
- [ ] Schema.org LocalBusiness & Product JSON-LD
- [ ] Google Maps & Benim İşletmem Kaydı

---

## 📲 Faz 5: 360° Sosyal Medya & Saha Pazarlaması (11-14. Gün)
### 📹 Şantiye & Transmiksör Aksiyon Video İçerikleri
**Açıklama:** Instagram Reels & YouTube Shorts için taze beton döküm anı, slump testi, taze beton sıcaklık ölçümü ve mikser aksiyon videoları.

**Etiketler:** `Sosyal Medya`  
**Kontrol Listesi:**
- [ ] Slump Testi Video Çekimi
- [ ] Transmiksör Filosu Tanıtım Şortu
- [ ] Müşteri Yorum & Şantiye Referans Videosu

---

### 💼 LinkedIn B2B Müteahhit Kampanyası
**Açıklama:** İnşaat mühendisleri, şantiye şefleri ve müteahhitlere yönelik kurumsal B2B bilgilendirici teknik gönderiler ve vaka analizleri.

**Etiketler:** `B2B Pazarlama`  
**Kontrol Listesi:**
- [ ] Teknik Makale Paylaşımları
- [ ] Bölgesel Müteahhit Hedefli Duyurular
- [ ] Referans Proje Galeri Görselleri

---

## 🚀 Faz 6: Saha Lansmanı & Canlıya Geçiş (15. Gün)
### 🌐 Web Sitesi Canlıya Alınması & cPanel Upload
**Açıklama:** Web platformunun public_html klasörüne yüklenmesi, Cloudflare Edge & SSL kontrolü, mobilde 60 FPS performans testi.

**Etiketler:** `Lansman, Kritik`  
**Kontrol Listesi:**
- [ ] public_html Yüklemesi Tamamlandı
- [ ] Google Search Console & Analytics Kaydı
- [ ] Saha Satış Ekibine Dijital Katalog Dağıtımı

---

