"""
Autor: Christian Fladung
last build: 14.12.2023
Description: Webcrawler, der dazu dient, Nachrichtenartikel von der Website der Fakultät für 
Elektrotechnik, Informatik und Mathematik der Universität Paderborn) zu extrahieren und als DOCX-Dateien zu speichern.
Git: https://github.com/FladChris/EIM_News_Crawler.git
"""
import os
import requests
import docx
from bs4 import BeautifulSoup
from datetime import datetime
from htmldocx import HtmlToDocx
from docx import Document
from docx.enum.dml import MSO_THEME_COLOR_INDEX


def add_hyperlink(paragraph, text, url):
    # This gets access to the document.xml.rels file and gets a new relation id value
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    # Create the w:hyperlink tag and add needed values
    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id, )

    # Create a w:r element and a new w:rPr element
    new_run = docx.oxml.shared.OxmlElement('w:r')
    rPr = docx.oxml.shared.OxmlElement('w:rPr')

    # Join all the xml elements together add add the required text to the w:r element
    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)

    # Create a new Run object and add the hyperlink into it
    r = paragraph.add_run ()
    r._r.append (hyperlink)

    # A workaround for the lack of a hyperlink style (doesn't go purple after using the link)
    # Delete this if using a template that has the hyperlink style in it
    r.font.color.theme_color = MSO_THEME_COLOR_INDEX.HYPERLINK
    r.font.underline = True

    return hyperlink

def file_for_year(news_year):
    if not os.path.exists(news_year):
        os.mkdir(news_year)

def save_document(news_year, act_date, url_news_output, news_article, news_headline, clearurl, image_urls, contact_cards):
    article_clear = HtmlToDocx()
    doc = Document()
    doc.add_heading(news_headline, level=2)  #level gibt die Überschriftsgröße bzw. Art an
    for garbage in news_article:
        garbage = str(garbage).replace('\xad', '').replace('|', '')
        article_clear.add_html_to_document(garbage, doc)
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
                add_hyperlink(paragraph_contact_img, card['image_url'], card['image_url'])
                doc.add_paragraph(f"Name des Kontakts: {card['link_text']}")
                paragraph_contact_link = doc.add_paragraph("PM-Url: ")
                add_hyperlink(paragraph_contact_link, card['link_url'], card['link_url'])
    doc.save(f'{news_year}/{act_date}{url_news_output}.docx')

def main():
    page_number = 1
    news_counter = 0
    crawl_counter = True

    news_year = input("Aus welchem Jahr sollen die Berichte sein?\n")
    begin_year = datetime.date(datetime(int(news_year), 1, 1))
    end_year = datetime.date(datetime(int(news_year), 12, 31))

    file_for_year(news_year)
    
    while crawl_counter == True:
        url = f'https://www.eim.uni-paderborn.de/eim-news-list/seite-{page_number}'
        webseite = requests.get(url)
        results = BeautifulSoup(webseite.content, 'html.parser')
        news = results.find_all('div', class_='news-list-item_body')
        for article in news:
            date_span = article.find('span', class_='news-list-item_date')
            if date_span is not None:
                date = date_span.text.strip()
                act_date = datetime.strptime(date, '%d.%m.%Y').date()
                if begin_year <= act_date <= end_year:
                    news_headline = article.find('h3', class_='news-list-item_headline').text
                    print(date, news_headline)
                    news_counter += 1
                    url_news = article.find('a')['href']
                    url_news_output = url_news.replace(
                        '/', '_').replace('-single', '')
                    response = requests.get(
                        'https://www.eim.uni-paderborn.de' + url_news)
                    clearurl = 'https://www.eim.uni-paderborn.de' + url_news
                    news_result = BeautifulSoup(
                        response.content, 'html.parser')
                    news_article = news_result.find_all(
                        'div', class_='news-detail_content')
                    try:
                        media_sections = news_result.find_all('div', class_="mediaelement mediaelement-image")
                        image_urls = []
                        for media_section in media_sections:
                            if media_section is not None:       
                                image_tags = media_section.find_all('img')
                                for image_tag in image_tags:
                                    if image_tag is not None:
                                        image_urls.append("https://www.eim.uni-paderborn.de"+image_tag.get('src'))
                        else:   
                            pass                      
                    except AttributeError:
                        print("Kein Bild vorhanden")
                    try:
                        business_card_sections = news_result.find_all('div', class_="business-card teaser last")
                        contact_image_urls = []
                        contact_link_texts = []
                        contact_link_urls = []
                        contact_cards = {}
                        for business_card_section in business_card_sections:
                            if business_card_section is not None:
                                image_tags = business_card_section.find_all('img')
                                for image_tag in image_tags:
                                    if image_tag is not None:
                                        contact_image_urls.append("https://www.eim.uni-paderborn.de"+image_tag.get('src'))
                                link_tags = business_card_section.find_all('a')
                                for link_tag in link_tags:
                                    if link_tag is not None:
                                        contact_link_texts.append(link_tag.text)
                                        contact_link_urls.append(link_tag.get('href'))
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
                        save_document(news_year, act_date, url_news_output, news_article, news_headline, clearurl, image_urls,contact_cards)
                    else:
                        print('Kein Artikeltext vorhanden')

        page_number += 1

        if begin_year >= act_date:
            crawl_counter = False
        if crawl_counter == False:
            print('Anzahl der News: ', news_counter)

if __name__ == '__main__':
    main()
