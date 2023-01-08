import requests
from bs4 import BeautifulSoup as bs

url = "https://lenta.ru/"
response = requests.get(url).text

soup = bs(response, 'html.parser')

page = soup.find('a', class_ = "card-mini _topnews").find('div').find('span')

print(page)
