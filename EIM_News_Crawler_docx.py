import datetime
import os
import requests
import docx
from bs4 import BeautifulSoup
from datetime import datetime
from htmldocx import HtmlToDocx
from docx import Document
from docx.enum.dml import MSO_THEME_COLOR_INDEX

"""
Autor: Christian Fladung
letzter Build: 11.04.2024
Beschreibung: Webcrawler, der dazu dient, Nachrichtenartikel von der Website der Fakultät für 
Elektrotechnik, Informatik und Mathematik der Universität Paderborn) zu extrahieren und als DOCX-Dateien zu speichern.
Git: https://github.com/FladChris/EIM_News_Crawler.git
"""


def add_hyperlink(paragraph, text, url):
    """
    Fügt einen Hyperlink in einem Word-Dokument hinzu.

    Parameter:
    - paragraph (docx.text.paragraph.Paragraph): Der Absatz, zu dem der Hyperlink hinzugefügt werden soll.
    - text (str): Der Text, der für den Hyperlink angezeigt werden soll.
    - url (str): Die URL, zu der der Hyperlink navigieren soll.

    Rückgabe:
    - hyperlink (docx.oxml.shared.OxmlElement): Das erstellte Hyperlink-Element.
    """
    part = paragraph.part
    r_id = part.relate_to(
        url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id, )

    new_run = docx.oxml.shared.OxmlElement('w:r')
    rPr = docx.oxml.shared.OxmlElement('w:rPr')

    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)

    r = paragraph.add_run()
    r._r.append(hyperlink)

    r.font.color.theme_color = MSO_THEME_COLOR_INDEX.HYPERLINK
    r.font.underline = True

    return hyperlink


# Funktion zum Erstellen eines Verzeichnisses für das eingegebene Jahr
def create_directory_for_year(news_year):
    if not os.path.exists(news_year):
        os.mkdir(news_year)


def save_news_article(news_year, article_date, output_filename, article_content, news_headline, clearurl, image_urls, contact_cards):
    """
    Speichert einen News-Artikel als .docx-Datei.

    Parameter:
    - news_year (str): Das Jahr der News.
    - article_date (str): Das Datum des Artikels.
    - output_filename (str): Der Name der Ausgabedatei.
    - article_content (list): Eine Liste mit dem Inhalt des Artikels.
    - news_headline (str): Die Überschrift der News.
    - clearurl (str): Die klare URL des Artikels.
    - image_urls (list): Eine Liste mit den URLs der Bilder.
    - contact_cards (dict): Ein Dictionary mit den Kontaktinformationen.

    Rückgabewert:
    - None
    """
    article_clear = HtmlToDocx()
    doc = Document()
    # level gibt die Überschriftsgröße bzw. Art an
    doc.add_heading(news_headline, level=2)
    for content in article_content:
        content = str(content).replace('\xad', '').replace('|', '')
        article_clear.add_html_to_document(content, doc)
        paragraph_url_article = doc.add_paragraph("URL des Artikels: ")
        add_hyperlink(paragraph_url_article, clearurl, clearurl)
        if not image_urls:
            doc.add_paragraph("Kein Bild vorhanden")
        else:
            for url in image_urls:
                paragraph_picture = doc.add_paragraph("Url des Bildes: ")
                add_hyperlink(paragraph_picture, url, url)
        if not contact_cards:
            doc.add_paragraph("Kein Kontakt vorhanden")
        else:
            for key, card in contact_cards.items():
                doc.add_paragraph(f"Kontakt {key}:")
                paragraph_contact_img = doc.add_paragraph("Bild-URL: ")
                add_hyperlink(paragraph_contact_img,
                              card['image_url'], card['image_url'])
                doc.add_paragraph(f"Name des Kontakts: {card['link_text']}")
                paragraph_contact_link = doc.add_paragraph("PM-Url: ")
                add_hyperlink(paragraph_contact_link,
                              card['link_url'], card['link_url'])
    doc.save(f'{news_year}/{article_date}{output_filename}.docx')


def main():
    """
    Durchsucht die EIM-News-Liste nach Artikeln des eingegebenen Jahres und speichert die relevanten Informationen.

    Die Funktion fragt den Benutzer nach einem Jahr und durchsucht dann die EIM-News-Liste nach Artikeln, die in diesem Jahr veröffentlicht wurden.
    Die relevanten Informationen wie Datum, Überschrift, Artikeltext, Bilder und Kontaktinformationen werden extrahiert und in einer Datei gespeichert.
    """

    page_number = 1
    news_counter = 0
    crawl_counter = True

    news_year = input("Aus welchem Jahr sollen die Berichte sein?\n")
    begin_year = datetime.date(datetime(int(news_year), 1, 1))
    end_year = datetime.date(datetime(int(news_year), 12, 31))

    create_directory_for_year(news_year)

    while crawl_counter == True:
        url = f'https://www.eim.uni-paderborn.de/eim-news-list/seite-{page_number}'
        news_response = requests.get(url)
        news_details = BeautifulSoup(news_response.content, 'html.parser')
        news_items = news_details.find_all('div', class_='news-list-item_body')
        for article in news_items:
            date_span = article.find('span', class_='news-list-item_date')
            if date_span is not None:
                date = date_span.text.strip()
                article_date = datetime.strptime(date, '%d.%m.%Y').date()
                if begin_year <= article_date <= end_year:
                    news_headline = article.find(
                        'h3', class_='news-list-item_headline').text
                    print(date, news_headline)
                    news_counter += 1
                    url_news = article.find('a')['href']
                    output_filename = url_news.replace(
                        '/', '_').replace('-single', '')
                    news_response = requests.get(
                        'https://www.eim.uni-paderborn.de' + url_news)
                    clearurl = 'https://www.eim.uni-paderborn.de' + url_news
                    news_result = BeautifulSoup(
                        news_response.content, 'html.parser')
                    news_article = news_result.find_all(
                        'div', class_='news-detail_content')
                    try:
                        image_sections = news_result.find_all(
                            'div', class_="mediaelement mediaelement-image")
                        image_urls = []
                        for section in image_sections:
                            if section is not None:
                                href_tags = section.find_all('a')
                                for href_tag in href_tags:
                                    if href_tag is not None:
                                        print(href_tag['href'])
                                        image_urls.append(
                                            "https://www.eim.uni-paderborn.de/" + href_tag['href'])
                        else:
                            pass
                    except AttributeError:
                        print("Kein Bild vorhanden")
                    try:
                        contact_sections = news_result.find_all(
                            'div', class_="business-card teaser last")
                        contact_image_urls = []
                        contact_link_texts = []
                        contact_link_urls = []
                        contact_cards = {}
                        for section in contact_sections:
                            if section is not None:
                                image_tags = section.find_all('img')
                                for image_tag in image_tags:
                                    if image_tag is not None:
                                        contact_image_urls.append(
                                            "https://www.eim.uni-paderborn.de"+image_tag.get('src'))
                                link_tags = section.find_all('a')
                                for link_tag in link_tags:
                                    if link_tag is not None:
                                        contact_link_texts.append(
                                            link_tag.text)
                                        contact_link_urls.append(
                                            link_tag.get('href'))
                                for i in range(len(contact_image_urls)):
                                    card = {
                                        'image_url': contact_image_urls[i],
                                        'link_text': contact_link_texts[i],
                                        'link_url': contact_link_urls[i]
                                    }
                                    contact_cards[i] = card
                        else:
                            pass
                    except:
                        print("Keine Kontaktbox vorhanden")

                    if news_article is not None:
                        save_news_article(news_year, article_date, output_filename, news_article,
                                          news_headline, clearurl, image_urls, contact_cards)
                    else:
                        print('Kein Artikeltext vorhanden')

        page_number += 1

        if begin_year >= article_date:
            crawl_counter = False
        if crawl_counter == False:
            print('Anzahl der News: ', news_counter)
            print('Crawl beendet')

if __name__ == '__main__':
    main()
