#!/usr/bin/env python3
"""
EsnovaBeton — Trello Power-Up Özel İçe Aktarım Üreticisi
Bu betik Trello 'JSON/CSV İçe Aktar' ekranına %100 birebir uyan 'esnova_trello_import_perfect.csv' dosyasını üretir.
"""

import csv
import os

TASKS = [
    # Faz 0
    {
        "name": "📧 cPanel Üzerinden info@esnovabeton.com E-posta Açılışı",
        "listName": "🌐 Faz 0: Domain, cPanel & E-posta Altyapısı (BUGÜN)",
        "desc": "cPanel > E-posta Hesapları > Oluştur adımıyla info@esnovabeton.com, satis@esnovabeton.com ve teklif@esnovabeton.com hesapları açılacaktır.\n\nKontrol Adımları:\n- info@esnovabeton.com açıldı\n- satis@esnovabeton.com açıldı\n- Gmail yönlendirmesi yapıldı\n- Mobil telefon SSL ayarları yapıldı",
        "labels": "Altyapı, Kritik"
    },
    {
        "name": "☁️ Cloudflare DNS, SSL & DDoS Koruma Entegrasyonu",
        "listName": "🌐 Faz 0: Domain, cPanel & E-posta Altyapısı (BUGÜN)",
        "desc": "Cloudflare üzerinde hesap açılıp esnovabeton.com eklenecek, NS adresleri domain panosuna girilip 5.180.185.253 IP'si yönlendirilecektir.\n\nKontrol Adımları:\n- Cloudflare hesabı açıldı\n- Domain NS adresleri güncellendi\n- Ücretsiz SSL aktifleştirildi",
        "labels": "Altyapı, Güvenlik"
    },
    {
        "name": "📁 cPanel public_html Yayın Klasörü Hazırlığı",
        "desc": "cPanel Dosya Yöneticisi > /home/esnovabe/public_html içerisindeki eski varsayılan dosyalar temizlenecek, ilk karşılama sayfası yüklenecektir.\n\nKontrol Adımları:\n- Eski index.html temizlendi\n- Geçici açılış sayfası yüklendi",
        "listName": "🌐 Faz 0: Domain, cPanel & E-posta Altyapısı (BUGÜN)",
        "labels": "Altyapı"
    },
    # Faz 1
    {
        "name": "🔍 Rakip Beton Firmaları Analizi (Türkiye & Dünya)",
        "listName": "📌 Faz 1: Marka & Derin Pazarlama Araştırması (1. Gün)",
        "desc": "Akçansa, Çimsa, Oyak Beton, Holcim, CEMEX, Heidelberg Materials firmalarının web siteleri, renk paletleri, görsel dilleri ve teklif alma mekanizmaları incelenecektir.\n\nKontrol Adımları:\n- Türk beton devleri web incelemesi\n- Küresel beton devleri web incelemesi\n- Teklif alma & m³ hesaplayıcı kıyaslaması",
        "labels": "Araştırma, Kritik"
    },
    {
        "name": "🎨 Beton Sektörü Renk Paleti & Psikoloji Raporu",
        "listName": "📌 Faz 1: Marka & Derin Pazarlama Araştırması (1. Gün)",
        "desc": "Beton grisi (#4A5568), Güven Mavisi (#1E3A8A), Şantiye Turuncusu (#EA580C) ve Çevre Yeşili (#059669) dengesi ve renk psikolojisi raporlanmıştır.\n\nKontrol Adımları:\n- Ana renk seçimi\n- Vurgu rengi\n- Lucide Icon seti",
        "labels": "Tasarım, Kurumsal Kimlik"
    },
    {
        "name": "🤖 AI_RESEARCH_PROMPTS.md Promptlarının Çalıştırılması",
        "listName": "📌 Faz 1: Marka & Derin Pazarlama Araştırması (1. Gün)",
        "desc": "ChatGPT, Claude, Perplexity ve Gemini Deep Research araçlarına hazırlanan 4 ana prompt girilecek, derin raporlar toplanacaktır.\n\nKontrol Adımları:\n- Prompt 1 çalıştırıldı\n- Prompt 2 çalıştırıldı\n- Prompt 3 çalıştırıldı\n- Prompt 4 çalıştırıldı",
        "labels": "AI Prompt, Araştırma"
    },
    # Faz 2
    {
        "name": "✏️ EsnovaBeton Logo & Vektörel Amblem Tasarımı",
        "listName": "🎨 Faz 2: Kurumsal Kimlik & Görsel Hafıza (2-3. Gün)",
        "desc": "Beton mikseri, sağlamlık geometrisi, küp basınç test simgesi ve dinamik E/B harf yapısıyla akılda kalıcı 3 alternatif amblem çizimi.\n\nKontrol Adımları:\n- Vektörel logo alternatifleri\n- Kartvizit & Başlıklı kağıt\n- Transmiksör araç giydirme",
        "labels": "Kurumsal Kimlik"
    },
    {
        "name": "📐 Tipografi & Slogan (Value Proposition)",
        "listName": "🎨 Faz 2: Kurumsal Kimlik & Görsel Hafıza (2-3. Gün)",
        "desc": "'Geleceğin Sağlam Temelleri', 'Yüksek Dayanım, Zamanında Teslimat' vb. slogan varyasyonları ve modern tipografi.\n\nKontrol Adımları:\n- Kurumsal slogan seçimi\n- Font ailesi tanımları\n- Kullanım kılavuzu",
        "labels": "Kurumsal Kimlik"
    },
    # Faz 3
    {
        "name": "🏗️ Hero Bölümü & Likit Cam / WebGL Görsel Efektler",
        "listName": "💻 Faz 3: Web Sitesi Mimarisi & UI/UX (4-7. Gün)",
        "desc": "Kullanıcıyı ilk bakışta büyüleyecek 'WOW Factor' Likit Cam / WebGL parçacık efektli interaktif Hero alanı ve Bento Grid KPI kartları.\n\nKontrol Adımları:\n- Hero alanı tasarımı\n- Bento Grid KPI kartları\n- 44px dokunma hedefleri",
        "labels": "Web Geliştirme, UI/UX"
    },
    {
        "name": "🧮 İnteraktif Metreküp & Pompa Hesaplayıcı Modülü",
        "listName": "💻 Faz 3: Web Sitesi Mimarisi & UI/UX (4-7. Gün)",
        "desc": "Müteahhitlerin ve bireysel yapı sahiplerinin en-boy-yükseklik girerek ihtiyaç duyduğu hazır beton miktarını (m³) ve pompa tipini hesaplayan interaktif araç.\n\nKontrol Adımları:\n- Ölçü girdi alanları\n- Beton sınıf seçimi (C25/30 - C50/60)\n- Teklif al butonu entegrasyonu",
        "labels": "Web Geliştirme, Özellik"
    },
    {
        "name": "📜 Ürünler, Beton Sınıfları & Kalite Laboratuvarı Sayfası",
        "listName": "💻 Faz 3: Web Sitesi Mimarisi & UI/UX (4-7. Gün)",
        "desc": "Kırılma basınç testleri, Ar-Ge laboratuvarı, brüt beton, şap betonu, kendiliğinden yerleşen beton (KYB) ürün katalog ekranları.\n\nKontrol Adımları:\n- Beton sınıf kartları\n- TSE/ISO kalite belgeleri\n- Laboratuvar görselleri",
        "labels": "Web Geliştirme"
    },
    # Faz 4
    {
        "name": "🎯 B2B Müteahhit & Şantiye Hızlı Teklif Formu",
        "listName": "📝 Faz 4: İçerik, SEO & B2B Formlar (8-10. Gün)",
        "desc": "Şantiye adresi, döküm tarihi, döküm hızı (m³/saat) ve pompa ihtiyacı içeren dinamik teklif talebi formu (info@esnovabeton.com entegreli).\n\nKontrol Adımları:\n- Form tasarımı\n- WhatsApp hızlı döküm hattı\n- E-posta bildirim testi",
        "labels": "İçerik, SEO"
    },
    {
        "name": "🔎 Hazır Beton SEO & AIO Optimizasyonu",
        "listName": "📝 Faz 4: İçerik, SEO & B2B Formlar (8-10. Gün)",
        "desc": "'Hazır beton fiyatları', 'C30 beton metreküp fiyatı', 'Pompalı beton dökümü' anahtar kelimeleri ve JSON-LD şema verileri.\n\nKontrol Adımları:\n- Meta başlık & açıklamalar\n- Schema.org JSON-LD\n- Google Benim İşletmem kaydı",
        "labels": "SEO"
    },
    # Faz 5
    {
        "name": "📹 Şantiye & Transmiksör Aksiyon Video İçerikleri",
        "listName": "📲 Faz 5: 360° Sosyal Medya & Saha Pazarlaması (11-14. Gün)",
        "desc": "Instagram Reels & YouTube Shorts için taze beton döküm anı, slump testi, taze beton sıcaklık ölçümü ve mikser aksiyon videoları.\n\nKontrol Adımları:\n- Slump testi video çekimi\n- Transmiksör tanıtım videosu\n- Şantiye referans videosu",
        "labels": "Sosyal Medya"
    },
    {
        "name": "💼 LinkedIn B2B Müteahhit Kampanyası",
        "listName": "📲 Faz 5: 360° Sosyal Medya & Saha Pazarlaması (11-14. Gün)",
        "desc": "İnşaat mühendisleri, şantiye şefleri ve müteahhitlere yönelik kurumsal B2B bilgilendirici teknik gönderiler ve vaka analizleri.\n\nKontrol Adımları:\n- Teknik makale paylaşımları\n- Bölgesel müteahhit duyurusu\n- Referans proje görselleri",
        "labels": "B2B Pazarlama"
    },
    # Faz 6
    {
        "name": "🌐 Web Sitesi Canlıya Alınması & cPanel Upload",
        "listName": "🚀 Faz 6: Saha Lansmanı & Canlıya Geçiş (15. Gün)",
        "desc": "Web platformunun public_html klasörüne yüklenmesi, Cloudflare Edge & SSL kontrolü, mobilde 60 FPS performans testi.\n\nKontrol Adımları:\n- public_html yüklemesi yapıldı\n- Google Search Console kaydı\n- Dijital katalog teslimi",
        "labels": "Lansman, Kritik"
    }
]

def generate():
    filepath = os.path.join(os.path.dirname(__file__), "esnova_trello_import_perfect.csv")
    with open(filepath, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "listName", "desc", "labels"])
        writer.writeheader()
        for t in TASKS:
            writer.writerow(t)
    print(f"✅ Özel Trello CSV üretildi: {filepath}")

if __name__ == "__main__":
    generate()
