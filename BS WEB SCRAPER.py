from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('http://habr.com').text
soup = BeautifulSoup(source, 'lxml')
csv_file = open('habr_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary'])
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content')
    print(summary)
    print()
    csv_writer.writerow([headline, summary])
csv_file.close()
