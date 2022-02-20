import requests
from bs4 import BeautifulSoup
import time
import random

xmlraw = requests.get('https://vividarmy-wikinotes.vercel.app/sitemap.xml')
# print(xmlraw.text)
xmlsoup = BeautifulSoup(xmlraw.text, "xml")
# print(xmlsoup)
findsoup = xmlsoup.find_all('loc')
lens = len(findsoup)
for item in findsoup:
  time.sleep(random.uniform((3600 / lens / 3), (3600 / lens))
  print(item.text)
  response = requests.get('https://www.google.com/search?q=' + item.text + '&ie=UTF-8&num=100')
  soup = BeautifulSoup(response.text, 'html.parser')
  h3 = soup.find_all('div')
  num = 0
  crawl = 'false'
  for item in h3:
    # scrape = item[0].split('>')[1].split('</title')[0]
    title = item.text
    print(title)
    # https://note.nkmk.me/python-str-search/
    # print('WikiNotes' in title)
    # https://note.nkmk.me/python-random-randrange-randint/
    if 'WikiNotes' in title:
        print(num)
    else:
        num += 1
        print('Failed')
