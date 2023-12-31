"""
Autor: Christian Fladung
last build: 14.12.2023
Description: Webcrawler, der dazu dient, Nachrichtenartikel von der Website der Fakultät für 
Elektrotechnik, Informatik und Mathematik der Universität Paderborn) zu extrahieren und als txt-Dateien 
und Unformatiert zu speichern.
Git: https://github.com/FladChris/EIM_News_Crawler.git
"""
import os
import requests
import codecs
from bs4 import BeautifulSoup
from datetime import datetime

def file_for_year(news_year):
    if not os.path.exists(news_year):
        os.mkdir(news_year)

def save_document(news_year, act_date, url_news_output, news_article, news_headline):
    # Create a file with the specified filename
    txt_filename = f'{news_year}/{act_date}{url_news_output}.txt'

    # Open the file in write mode
    with codecs.open(txt_filename, 'w', encoding='UTF-8') as file_out:
        # Write the news headline to the file
        file_out.write(news_headline + '\n\n')

        # Write the news article content to the file
        for paragraph in news_article:
            file_out.write(paragraph.text)
            file_out.write('\n')

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
                    news_result = BeautifulSoup(
                        response.content, 'html.parser')
                    news_article = news_result.find_all(
                        'div', class_='news-detail_content')
                    if news_article is not None:
                        save_document(news_year, act_date, url_news_output, news_article, news_headline)
                    else:
                        print('Kein Artikeltext vorhanden')

        page_number += 1

        if begin_year >= act_date:
            crawl_counter = False
        if crawl_counter == False:
            print('Anzahl der News: ', news_counter)

if __name__ == '__main__':
    main()
