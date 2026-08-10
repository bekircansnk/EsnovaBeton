# 🌐 EsnovaBeton — cPanel, E-posta Kurulumu & Cloudflare Altyapı Rehberi

Bu rehber, ekran görüntülerinde paylaştığınız `esnovabeton.com:2083` cPanel yönetim panelinize göre adım adım hazırlanmıştır.

---

## 📸 Mevcut cPanel Altyapı Bilgileriniz (Ekran Görüntüsünden Tespit Edilen)

- **Birincil Etki Alanı (Domain):** `esnovabeton.com`
- **Sunucu IP Adresi (Shared IP):** `5.180.185.253`
- **Ana Giriş Dizini:** `/home/esnovabe`
- **Web Yayın Dizini:** `/home/esnovabe/public_html`
- **SSL Sertifikası:** Aktif (cPanel Otomatik SSL)

---

## 📧 1. cPanel Üzerinden Kurumsal E-posta Adresi Kurulumu (`info@esnovabeton.com`)

cPanel panolarda ücretsiz olarak istediğiniz kadar kurumsal e-posta adresi açabilirsiniz.

### Adım Adım E-posta Hesabı Açma:
1. cPanel ana sayfasındaki **"E-posta"** bölümüne gelin.
2. **"E-posta Hesapları" (Email Accounts)** ikonuna tıklayın.
3. Sağ üstteki mavi **"+ Oluştur" (Create)** butonuna basın.
4. **Kullanıcı Adı:** `info`, `satis`, `teklif`, `muhasebe` veya kendi isminizi yazın (`info@esnovabeton.com` olur).
5. **Şifre:** Güçlü bir şifre belirleyin.
6. **Depolama Alanı:** Varsayılan (1024 MB) veya "Sınırsız" yapabilirsiniz.
7. **"Oluştur"** butonuna basarak e-posta adresinizi anında aktifleştirin.

---

## 🔄 2. cPanel E-postalarını Gmail / Telefona Bağlama & Yönlendirme

Açtığınız kurumsal e-posta adreslerini kişisel Gmail hesabınıza yönlendirebilir veya doğrudan cep telefonunuza (iPhone Mail / Android Mail) kurabilirsiniz.

### A) E-posta Yönlendirmesi (En Kolay Yöntem):
1. cPanel > **E-posta Yönlendirmesi (Email Forwarders)** alanına girin.
2. **"Yönlendirici Ekle"** butonuna tıklayın.
3. `info@esnovabeton.com` adresine gelen postaların doğrudan kişisel `@gmail.com` adresinize düşmesini sağlayın.

### B) Outlook / iPhone / Android SMTP & IMAP Ayarları:
- **Gelen Sunucu (IMAP):** `mail.esnovabeton.com` (Port: 993, SSL/TLS)
- **Giden Sunucu (SMTP):** `mail.esnovabeton.com` (Port: 465, SSL/TLS)
- **Kullanıcı Adı:** `info@esnovabeton.com`
- **Şifre:** Oluştururken belirlediğiniz şifre.

---

## ☁️ 3. Cloudflare Entegrasyonu (Neden Kullanmalıyız & Nasıl Kurulur?)

Cloudflare kullanmak web sitenizi 5 kat hızlandırır, ücretsiz DDoS ve bot koruması sağlar ve SSL sertifikasını küresel seviyeye çıkarır.

### Cloudflare Kurulum Adımları:
1. [Cloudflare.com](https://www.cloudflare.com) üzerinde ücretsiz bir hesap açın.
2. **"Add a Site"** diyerek `esnovabeton.com` domaininizi ekleyin ve **Free Plan** seçin.
3. Cloudflare mevcut DNS kayıtlarınızı otomatik tarayacaktır. A kaydı IP adresinizin `5.180.185.253` olduğundan emin olun.
4. Cloudflare size 2 adet **Nameserver (NS)** verecektir (Örn: `dara.ns.cloudflare.com`, `ned.ns.cloudflare.com`).
5. Domaini satın aldığınız firmanın panosuna girip (Natro, İsimtescil, Regru vb.) DNS Nameserver adreslerini Cloudflare'inki ile değiştirin.
6. **Sonuç:** Web siteniz Cloudflare kalkanı arkasına geçer. cPanel e-postalarınız hiç bozulmadan çalışmaya devam eder.

---

## 📁 4. cPanel Üzerinden Web Sitesini Yayına Alma (`public_html`)

Geliştireceğimiz modern web sitesini canlıya almak son derece kolaydır.

### Adım Adım Dosya Yükleme:
1. cPanel > **"Dosya Yöneticisi" (File Manager)** ikonuna tıklayın (2. ekran görüntünüzdeki ekran açılır).
2. Sol menüden **`public_html`** klasörüne çift tıklayın.
3. Şu anda orada olan varsayılan `index.html` ve `cgi-bin` dosyalarını silin.
4. Üst menüdeki **"Yükle" (Upload)** butonuna basarak hazırladığımız web projesinin çıktılarını (`.zip` halinde) buraya yükleyin.
5. Yüklenen `.zip` dosyasına sağ tıklayıp **"Çıkar" (Extract)** deyin.
6. `https://esnovabeton.com` adresine girdiğinizde yeni web siteniz anında canlıya geçecektir!
