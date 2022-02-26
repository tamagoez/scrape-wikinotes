import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.google.com/search?q=site:vividarmy-wikinotes.vercel.app&ie=UTF-8&num=100')
soup = BeautifulSoup(response.text, 'html.parser')
h3 = soup.find_all('h3')
for item in h3:
  print(item.text)
