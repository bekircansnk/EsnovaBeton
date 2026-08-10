# 🚀 cPanel & GitHub Otomatik Yayınlama (Auto-Deploy) Rehberi

Bu rehber, GitHub reponuza (`https://github.com/bekircansnk/EsnovaBeton`) kod gönderdiğinizde (git push), cPanel'in web sitenizi otomatik olarak canlıya alması (deploy etmesi) için adım adım hazırlanmıştır.

---

## 🔗 1. Oluşturulan Canlı GitHub Deposu

- **GitHub Repository URL:** `https://github.com/bekircansnk/EsnovaBeton`
- **Git Clone Adresi:** `https://github.com/bekircansnk/EsnovaBeton.git`
- **Ana Dal (Branch):** `main`
- **cPanel Deploy Konfigürasyonu:** [`.cpanel.yml`](file:///Users/bekir/Uygulamalarim/14-EsnovaBeton/.cpanel.yml)

---

## 🛠️ 2. cPanel Üzerinde Git™ Version Control Kurulumu

Ekran görüntünüzdeki cPanel > **Dosyalar** bölümündeki **"Git™ Version Control"** simgesine tıklayın:

1. Sağ üstteki **"Create" (Oluştur)** butonuna basın.
2. **Clone a Repository** anahtarını açık (ON) konuma getirin.
3. **Clone URL:** `https://github.com/bekircansnk/EsnovaBeton.git` yapıştırın.
4. **Repository Path:** `/home/esnovabe/repositories/EsnovaBeton` (cPanel otomatik doldurur).
5. **Repository Name:** `EsnovaBeton`
6. Alttaki **"Create"** butonuna basın. cPanel reponuzu birkaç saniyede klonlayacaktır.

---

## 🚀 3. İlk Tek Tıkla Canlıya Alma (Deploy)

1. cPanel > **Git™ Version Control** listesinde oluşan `EsnovaBeton` reposunun yanındaki **"Manage" (Yönet)** butonuna tıklayın.
2. Üst sekmeden **"Deploy HEAD Commit"** sekmesine gelin.
3. **"Deploy HEAD Commit"** butonuna tıklayın.
4. cPanel projedeki [`.cpanel.yml`](file:///Users/bekir/Uygulamalarim/14-EsnovaBeton/.cpanel.yml) dosyasını otomatik okuyacak ve `index.html` sayfasını `public_html` içine kopyalayarak `esnovabeton.com` adresini CANLIYA alacaktır!

---

## ⚡ 4. Her `git push` Sonrası Otomatik Canlıya Geçiş (GitHub Webhook)

Bilgisayarınızda veya bu ajan ile kod değiştirip `git push` yaptığınız anda cPanel'in otomatik çekmesi için:

1. cPanel > Git™ Version Control > **Manage** sayfasındaki **"Webhook URL"** adresini kopyalayın.
2. [GitHub Reponuza (`bekircansnk/EsnovaBeton`)](https://github.com/bekircansnk/EsnovaBeton) girin.
3. **Settings** > **Webhooks** > **Add webhook** butonuna tıklayın.
4. **Payload URL:** cPanel'den kopyaladığınız Webhook URL'sini yapıştırın.
5. **Content type:** `application/json` seçin.
6. **Add webhook** butonuna basın.

🎉 **Tebrikler!** Artık repoya gönderilen her güncelleme anında `esnovabeton.com` üzerinde canlıya geçecektir!
