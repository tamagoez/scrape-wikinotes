import requests
from bs4 import BeautifulSoup


xmlraw = requests.get('https://vividarmy-wikinotes.vercel.app/sitemap.xml')
# print(xmlraw.text)
xmlsoup = BeautifulSoup(xmlraw.text, "xml")
# print(xmlsoup)
findsoup = xmlsoup.find_all('loc')
for item in findsoup:
  print(item.text)
