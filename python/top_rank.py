import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.google.com/search?q=vividarmy&ie=UTF-8&num=100')
soup = BeautifulSoup(response.text, 'html.parser')
h3 = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
num = 0
for item in h3:
  # scrape = item[0].split('>')[1].split('</title')[0]
  title = item.text
  # print(title)
  # https://note.nkmk.me/python-str-search/
  # print('WikiNotes' in title)
  if 'WikiNotes' in title:
      print(num)
  else:
      num += 1
