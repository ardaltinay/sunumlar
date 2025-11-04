# -*- coding: utf-8 -*-
"""
Medici Ailesi — 8 Dakikalık Sunum için PowerPoint üretici
Gereksinimler:
  - Python 3.8+
  - pip install python-pptx

Yerelde çalıştırmak istersen:
  python build_medici_presentation.py
Çıktı:
  Medici_Ailesi_Sunum.pptx (16:9)
"""

from pptx import Presentation
from pptx.util import Inches

def add_content_slide(prs, title, bullets, notes):
    slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title and Content
    slide.shapes.title.text = title
    body = slide.placeholders[1].text_frame
    body.clear()
    if bullets:
        for i, b in enumerate(bullets):
            if i == 0:
                body.text = b
            else:
                p = body.add_paragraph()
                p.text = b
                p.level = 0
    # Konuşmacı notları
    notes_tf = slide.notes_slide.notes_text_frame
    notes_tf.clear()
    notes_tf.text = notes.strip()
    return slide

def main():
    prs = Presentation()
    # 16:9 boyut
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    # Slide 1 — Kapak
    slide1 = prs.slides.add_slide(prs.slide_layouts[0])  # Title
    slide1.shapes.title.text = "Medici Ailesi — Bankadan Şehre"
    slide1.placeholders[1].text = "Finans, Sanat ve Kubbe — 8 Dakikalık Sunum\nFinans → Sanat → Şehir"
    slide1.notes_slide.notes_text_frame.text = """Bugün sizi, bankacılığın sanata, sanatın da bir şehrin kimliğine nasıl dönüştüğünü anlatan bir hikâyeye götürmek istiyorum. Kahramanlarımız Medici ailesi; sahnemiz, 15. yüzyılın Floransa’sı. Medici’ler, finansal güçlerini yalnızca servet biriktirmek için değil, "görünür iyilik" üretmek ve kalıcı bir şehir markası yaratmak için kullandılar. Bu hikâye, bankadan şehre uzanan bir dönüşüm modeli."""

    # Slide 2 — Floransa’da Zemin
    add_content_slide(
        prs,
        "Floransa’da Zemin",
        ["Loncalar", "Ticaret ağları", "Risk ve sermaye"],
        """Önce zemin: Floransa, yün ve ipek loncalarıyla Avrupa ticaretinin kilit şehirlerinden biriydi.
Loncalar yalnızca üretimi değil, kamusal işleri, yarışmaları ve standartları da belirleyen kurumlardı.
Akdeniz ticaret ağı şehre sermaye, risk ve bilgi akışı sağladı. Böyle bir ortamda finansal inovasyonlar filizlendi."""
    )

    # Slide 3 — Medici Bankası
    add_content_slide(
        prs,
        "Medici Bankası",
        ["1397", "Papalık ilişkisi", "Şube ağı"],
        """1397’de Giovanni di Bicci de’ Medici’nin kurduğu Medici Bankası, kısa sürede Avrupa’nın en nüfuzlu kurumlarından biri oldu.
Güçlerinin sırrı; Roma, Venedik, Londra, Brugge gibi şehirlerdeki şube ağı ve özellikle papalıkla kurdukları yüksek güven ilişkisiydi.
Disiplinli defter tutma, temkinli risk yönetimi ve esnek temsilcilik modeliyle “güven + ağ = ölçek” formülünü işlettiler."""
    )

    # Slide 4 — Neden Sanat?
    add_content_slide(
        prs,
        "Neden Sanat?",
        ["Meşruiyet", "Görünür iyilik", "Kamusal hafıza"],
        """Peki finansal güç neden sanata akar? Çünkü sanat, gücün en görünür, en kalıcı ve en az itiraz gören yüzüdür.
Medici’ler özel zenginliği kamusal iyiliğe tercüme ederek meşruiyet ürettiler.
Saray cepheleri, şenlikler, heykeller, şapeller… Hepsi “Medici adı şehrin hafızasına nasıl kazınır?” sorusunun cevabıydı.
Hami, sadece para veren değil; zevki ve ideali şekillendiren bir aktöre dönüştü."""
    )

    # Slide 5 — Himaye Ağı
    add_content_slide(
        prs,
        "Himaye Ağı",
        ["Botticelli", "Michelangelo", "Leonardo"],
        """Medici çevresi, yetenekleri erken fark eden ve doğru çevrelerle buluşturan bir “yaratıcı ekosistem”di.
Botticelli’nin Primavera ve Venüs’ün Doğuşu, Medici çevresinin mitoloji ve neoplatonizmle bezenmiş zevkini yansıtır.
Genç Michelangelo, Lorenzo “il Magnifico”nun sarayındaki heykel bahçesinde antik formu yakından gözledi.
Leonardo’nun Floransa yılları da bu entelektüel iklimle iç içe geçti; siparişlerin ve fikirlerin dolaşımı Medici düğümünde hızlandı."""
    )

    # Slide 6 — Michelangelo ve Medici
    add_content_slide(
        prs,
        "Michelangelo ve Medici",
        ["Lorenzo il Magnifico", "Medici Şapeli"],
        """Lorenzo’nun himayesi, Michelangelo’nun erken biçimlenişinde belirleyiciydi.
Bu ilişki yıllar sonra Medici Şapeli’nde —Yeni Sakristi’de— olgunlaştı.
“Gece” ve “Gündüz”, “Alacakaranlık” ve “Şafak” figürleri, bir aile anıtının ötesinde; zaman, güç ve fanilik üzerine taşta yazılmış bir felsefedir.
Medici adı, Michelangelo’nun mermerinde bir dünya görüşüne dönüşür: Kalıcılık yalnızca taşa değil, fikre de kazınmalıdır."""
    )

    # Slide 7 — Duomo Kubbesi
    add_content_slide(
        prs,
        "Duomo Kubbesi",
        ["Brunelleschi", "Çift kabuk", "Balıkkılçığı"],
        """Şimdi kentin kalbine, Santa Maria del Fiore’nin kubbesine bakalım.
Brunelleschi, merkezleme iskelesi olmadan devasa açıklığı geçmek için çift kabuklu kubbe, balıkkılçığı örgülü tuğla ve özgün kaldırma makineleri tasarladı.
Proje Yüncüler Loncası’nın girişimiydi; ancak Medici’lerin biçimlendirdiği kültürel-ekonomik iklim, böyle bir teknik cesareti ödüllendiren bir şehir düzeni yarattı.
Aynı dönemde Medici’ye yakın San Lorenzo’da yürütülen yapılar, kamusal-özel ekseninde yeni bir mimari dilin yayıldığını gösterir."""
    )

    # Slide 8 — Kapanış
    add_content_slide(
        prs,
        "Kapanış",
        ["Finans → Sanat → Şehir", "Ders: Görünür yatırım"],
        """Medici hikâyesi, sermayenin imgeye, imgenin şehre dönüşümünün el kitabıdır: Finans → Sanat → Şehir.
Botticelli’nin renklerinde, Michelangelo’nun mermerinde, Brunelleschi’nin kubbesinde aynı formül görünür: güven, ağ, vizyon ve görünür yatırım.
Bugün de şehirler ve markalar için ders açık: Kaynağı büyütmek yetmez; onu kamusal hafızaya dönüştürmek kalıcılığı getirir.
Medici’lerin Floransa’sı bunun kanıtıdır."""
    )

    prs.save("Medici_Ailesi_Sunum.pptx")
    print("Medici_Ailesi_Sunum.pptx oluşturuldu")

if __name__ == "__main__":
    main()
