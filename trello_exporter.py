#!/usr/bin/env python3
"""
EsnovaBeton — Trello Board Exporter & Generator (v2.0)
cPanel, Domain, Cloudflare, E-posta, Pazarlama ve Web Kurulumu Trello Panosu
"""

import json
import csv
import os

TASKS_DATA = [
    {
        "list_name": "🌐 Faz 0: Domain, cPanel & E-posta Altyapısı (BUGÜN)",
        "cards": [
            {
                "name": "📧 cPanel Üzerinden info@esnovabeton.com E-posta Açılışı",
                "desc": "cPanel > E-posta Hesapları > Oluştur adımıyla info@esnovabeton.com, satis@esnovabeton.com ve teklif@esnovabeton.com kurumsal hesapları açılacaktır.",
                "labels": ["Altyapı", "Kritik"],
                "checklists": ["info@esnovabeton.com oluşturuldu", "satis@esnovabeton.com oluşturuldu", "E-posta yönlendirmesi kişisel Gmail'e bağlandı", "Mobil telefon IMAP/SMTP kurulumu yapıldı"]
            },
            {
                "name": "☁️ Cloudflare DNS, SSL & DDoS Koruma Entegrasyonu",
                "desc": "Cloudflare üzerinde ücretsiz hesap açılıp esnovabeton.com eklenecek, NS adresleri domain kaydediciye girilip 5.180.185.253 IP'si yönlendirilecektir.",
                "labels": ["Altyapı", "Güvenlik"],
                "checklists": ["Cloudflare hesabı oluşturuldu", "Domain NS adresleri güncellendi", "Ücretsiz SSL ve Edge Caching aktifleştirildi"]
            },
            {
                "name": "📁 cPanel public_html Yayın Klasörü Hazırlığı",
                "desc": "cPanel Dosya Yöneticisi > /home/esnovabe/public_html içerisindeki eski varsayılan dosyalar temizlenecek, ilk karşılama sayfası yüklenecektir.",
                "labels": ["Altyapı"],
                "checklists": ["Eski index.html temizlendi", "Geçici 'Yakında Hizmetinizde' açılış sayfası eklendi"]
            }
        ]
    },
    {
        "list_name": "📌 Faz 1: Marka & Derin Pazarlama Araştırması (1. Gün)",
        "cards": [
            {
                "name": "🔍 Rakip Beton Firmaları Analizi (Türkiye & Dünya)",
                "desc": "Akçansa, Çimsa, Oyak Beton, Holcim, CEMEX, Heidelberg Materials firmalarının web siteleri, renk paletleri, görsel dilleri ve teklif alma mekanizmaları incelenmiştir.",
                "labels": ["Araştırma", "Kritik"],
                "checklists": ["Türk beton devleri web incelemesi", "Küresel beton devleri web incelemesi", "Teklif alma & Metreküp hesaplayıcı kıyaslaması"]
            },
            {
                "name": "🎨 Beton Sektörü Renk Paleti & Psikoloji Raporu",
                "desc": "Beton grisi (#4A5568), Güven Mavisi (#1E3A8A), Şantiye Turuncusu (#EA580C) ve Çevre/Sürdürülebilirlik Yeşili (#059669) dengesi ve renk psikolojisi raporlanmıştır.",
                "labels": ["Tasarım", "Kurumsal Kimlik"],
                "checklists": ["Ana renk seçimi (Primary)", "Vurgu rengi (Accent)", "Endüstriyel ikonografi & Lucide Icon set"]
            },
            {
                "name": "🤖 AI_RESEARCH_PROMPTS.md Promptlarının Çalıştırılması",
                "desc": "ChatGPT, Claude, Perplexity ve Gemini Deep Research araçlarına hazırlanan 4 ana prompt girilecek, derin raporlar toplanacaktır.",
                "labels": ["AI Prompt", "Araştırma"],
                "checklists": ["Prompt 1 (Rakip Analizi) çalıştırıldı", "Prompt 2 (Renk Stratejisi) çalıştırıldı", "Prompt 3 (Web UX & Metreküp Hesaplayıcı) çalıştırıldı", "Prompt 4 (360° Pazarlama) çalıştırıldı"]
            }
        ]
    },
    {
        "list_name": "🎨 Faz 2: Kurumsal Kimlik & Görsel Hafıza (2-3. Gün)",
        "cards": [
            {
                "name": "✏️ EsnovaBeton Logo & Vektörel Amblem Tasarımı",
                "desc": "Beton mikseri, sağlamlık geometrisi, küp basınç test simgesi ve dinamik E/B harf yapısıyla akılda kalıcı 3 alternatif amblem çizimi.",
                "labels": ["Kurumsal Kimlik"],
                "checklists": ["Vektörel logo alternatifleri", "Kartvizit & Başlıklı Kağıt", "Transmiksör & Pompa Araç Giydirme Tasarımı"]
            },
            {
                "name": "📐 Tipografi & Slogan (Value Proposition)",
                "desc": "'Geleceğin Sağlam Temelleri', 'Yüksek Dayanım, Zamanında Teslimat' vb. slogan varyasyonları ve modern tipografi (Inter / Outfit / Roboto).",
                "labels": ["Kurumsal Kimlik"],
                "checklists": ["Kurumsal Slogan Seçimi", "Font Ailesi Tanımlamaları", "Kullanım Kılavuzu (Brand Guidelines)"]
            }
        ]
    },
    {
        "list_name": "💻 Faz 3: Web Sitesi Mimarisi & UI/UX (4-7. Gün)",
        "cards": [
            {
                "name": "🏗️ Hero Bölümü & Likit Cam / WebGL Görsel Efektler",
                "desc": "Kullanıcıyı ilk bakışta büyüleyecek 'WOW Factor' Likit Cam / WebGL parçacık efektli interaktif Hero alanı ve Bento Grid KPI kartları.",
                "labels": ["Web Geliştirme", "UI/UX"],
                "checklists": ["Hero Alanı Tasarımı", "Bento Grid KPI Kartları (Yıllık Kapasite, Tesis Sayısı, Pompa Parkı)", "Mobil Uyumlu 44px Dokunma Hedefleri"]
            },
            {
                "name": "🧮 İnteraktif Metreküp & Pompa Hesaplayıcı Modülü",
                "desc": "Müteahhitlerin ve bireysel yapı sahiplerinin en-boy-yükseklik girerek ihtiyaç duyduğu hazır beton miktarını (m³) ve pompa tipini hesaplayan interaktif araç.",
                "labels": ["Web Geliştirme", "Özellik"],
                "checklists": ["En-Boy-Yükseklik Girdi Alanları", "Beton Sınıfı Seçimi (C25/30, C30/37, C35/45, C40/50)", "Teklif Al Butonu Entegrasyonu"]
            },
            {
                "name": "📜 Ürünler, Beton Sınıfları & Kalite Laboratuvarı Sayfası",
                "desc": "Kırılma basınç testleri, Ar-Ge laboratuvarı, brüt beton, şap betonu, kendiliğinden yerleşen beton (KYB) ürün katalog ekranları.",
                "labels": ["Web Geliştirme"],
                "checklists": ["Beton Sınıf Kartları", "Kalite Belgeleri & ISO Sertifikaları", "Laboratuvar Test Görselleri"]
            }
        ]
    },
    {
        "list_name": "📝 Faz 4: İçerik, SEO & B2B Formlar (8-10. Gün)",
        "cards": [
            {
                "name": "🎯 B2B Müteahhit & Şantiye Hızlı Teklif Formu",
                "desc": "Şantiye adresi, döküm tarihi, döküm hızı (m³/saat) ve pompa ihtiyacı içeren dinamik teklif talebi formu (info@esnovabeton.com entegreli).",
                "labels": ["İçerik", "SEO"],
                "checklists": ["Form Alanları Tasarımı", "WhatsApp Hızlı Döküm Hattı Entegrasyonu", "Form Onay & E-posta Bildirimi"]
            },
            {
                "name": "🔎 Hazır Beton SEO & AIO (Yapay Zeka Arama) Optimizasyonu",
                "desc": "'Hazır beton fiyatları', 'C30 beton metreküp fiyatı', 'Pompalı beton dökümü' anahtar kelimeleri ve JSON-LD şema verileri.",
                "labels": ["SEO"],
                "checklists": ["Meta Başlık ve Açıklamalar", "Schema.org LocalBusiness & Product JSON-LD", "Google Maps & Benim İşletmem Kaydı"]
            }
        ]
    },
    {
        "list_name": "📲 Faz 5: 360° Sosyal Medya & Saha Pazarlaması (11-14. Gün)",
        "cards": [
            {
                "name": "📹 Şantiye & Transmiksör Aksiyon Video İçerikleri",
                "desc": "Instagram Reels & YouTube Shorts için taze beton döküm anı, slump testi, taze beton sıcaklık ölçümü ve mikser aksiyon videoları.",
                "labels": ["Sosyal Medya"],
                "checklists": ["Slump Testi Video Çekimi", "Transmiksör Filosu Tanıtım Şortu", "Müşteri Yorum & Şantiye Referans Videosu"]
            },
            {
                "name": "💼 LinkedIn B2B Müteahhit Kampanyası",
                "desc": "İnşaat mühendisleri, şantiye şefleri ve müteahhitlere yönelik kurumsal B2B bilgilendirici teknik gönderiler ve vaka analizleri.",
                "labels": ["B2B Pazarlama"],
                "checklists": ["Teknik Makale Paylaşımları", "Bölgesel Müteahhit Hedefli Duyurular", "Referans Proje Galeri Görselleri"]
            }
        ]
    },
    {
        "list_name": "🚀 Faz 6: Saha Lansmanı & Canlıya Geçiş (15. Gün)",
        "cards": [
            {
                "name": "🌐 Web Sitesi Canlıya Alınması & cPanel Upload",
                "desc": "Web platformunun public_html klasörüne yüklenmesi, Cloudflare Edge & SSL kontrolü, mobilde 60 FPS performans testi.",
                "labels": ["Lansman", "Kritik"],
                "checklists": ["public_html Yüklemesi Tamamlandı", "Google Search Console & Analytics Kaydı", "Saha Satış Ekibine Dijital Katalog Dağıtımı"]
            }
        ]
    }
]

def export_json(filepath):
    board_data = {
        "name": "EsnovaBeton — 360° Pazarlama, Altyapı & Web Kurulumu",
        "desc": "EsnovaBeton markasının cPanel, e-posta, Cloudflare, kurumsal kimlik ve web sitesi yol haritası.",
        "lists": []
    }
    for l_idx, l_data in enumerate(TASKS_DATA):
        trello_list = {
            "id": f"list_{l_idx+1}",
            "name": l_data["list_name"],
            "pos": (l_idx + 1) * 1000,
            "cards": []
        }
        for c_idx, c_data in enumerate(l_data["cards"]):
            card = {
                "id": f"card_{l_idx+1}_{c_idx+1}",
                "name": c_data["name"],
                "desc": c_data["desc"],
                "pos": (c_idx + 1) * 1000,
                "labels": [{"name": label} for label in c_data["labels"]],
                "checklists": [
                    {
                        "name": "Yapılacak Adımlar",
                        "checkItems": [{"name": item, "state": "incomplete"} for item in c_data["checklists"]]
                    }
                ]
            }
            trello_list["cards"].append(card)
        board_data["lists"].append(trello_list)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(board_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Trello JSON dosyası güncellendi: {filepath}")

def export_csv(filepath):
    with open(filepath, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Liste Adı", "Kart Adı", "Açıklama", "Etiketler", "Kontrol Listesi Adımları"])
        for l_data in TASKS_DATA:
            for c_data in l_data["cards"]:
                writer.writerow([
                    l_data["list_name"],
                    c_data["name"],
                    c_data["desc"],
                    ", ".join(c_data["labels"]),
                    " | ".join(c_data["checklists"])
                ])
    print(f"✅ Trello CSV dosyası güncellendi: {filepath}")

def export_markdown(filepath):
    lines = ["# 🏗️ EsnovaBeton — cPanel, Altyapı & Trello Görev Panosu\n\n"]
    lines.append("Bu rehber cPanel, e-posta, Cloudflare ve web kurulum adımlarını içerir.\n\n")
    for l_data in TASKS_DATA:
        lines.append(f"## {l_data['list_name']}\n")
        for c_data in l_data["cards"]:
            lines.append(f"### {c_data['name']}\n")
            lines.append(f"**Açıklama:** {c_data['desc']}\n\n")
            lines.append(f"**Etiketler:** `{', '.join(c_data['labels'])}`  \n")
            lines.append("**Kontrol Listesi:**\n")
            for item in c_data["checklists"]:
                lines.append(f"- [ ] {item}\n")
            lines.append("\n---\n\n")
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"✅ Trello Markdown rehberi güncellendi: {filepath}")

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    export_json(os.path.join(out_dir, "esnova_trello_board.json"))
    export_csv(os.path.join(out_dir, "esnova_trello_tasks.csv"))
    export_markdown(os.path.join(out_dir, "esnova_trello_markdown.md"))
