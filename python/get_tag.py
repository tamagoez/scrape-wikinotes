import requests
from bs4 import BeautifulSoup

xmlraw = requests.get('https://vividarmy-wikinotes.vercel.app/sitemap.xml')
# print(xmlraw.text)
xmlsoup = BeautifulSoup(xmlraw.text, "xml")
# print(xmlsoup)
findsoup = xmlsoup.find_all('loc')
for x in findsoup:
  print(x.text)
  rawurl = x.text.split('https://vividarmy-wikinotes.vercel.app/')
  # print(rawurl[1])
  raw = requests.get('https://raw.githubusercontent.com/tamagoez/vividarmy-wikinotes/main/' + rawurl[1] + '.mdx')
  rawsoup = BeautifulSoup(raw.text, 'html.parser')
  if 'tags:' in rawsoup.text:
    rawsoupcut = rawsoup.text.split('tags: [')[1].split(']')[0]
    trimraw = rawsoupcut.split(', ')
    print(trimraw)
  else:
    print('no tag')
  print()
