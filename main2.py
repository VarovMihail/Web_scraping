# 2 Улучшить скрипт так, чтобы он анализировал не только preview-информацию статьи, но и весь текст статьи целиком.

from pprint import pprint
from bs4 import BeautifulSoup
import requests
#from fake_useragent import UserAgent
#
# user = UserAgent().random
# print(user)
# определяем список ключевых слов
KEYWORDS1 = ['дизайн', 'фото', 'web', 'python']
KEYWORDS2 = ['Сегодня']
KEYWORDS3 = ['Дизайн', 'Фото', 'Web', 'Python']
KEYWORDS4 = ['Оптимус Прайм']

base_url = 'https://habr.com'
url = '/ru/all/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
resp = requests.get(base_url + url, headers=HEADERS)
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text,features='html.parser')
articles = soup.find('div', class_='tm-articles-list').find_all('article')

d = {}
for article in articles:

    href = article.find('h2').find('a').get('href')
    resp = requests.get(base_url+href, headers=HEADERS)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, features='html.parser')
    text = soup.find('div', id='post-content-body').text

    id = article.get('id')
    header = article.find('h2').find('a').find('span').text
    data = article.find('time').get('title')


    d[id] = {'url':base_url+href,
             'header':header,
             'data':data,
             'text':text
             }
#pprint(d)

for key,val in d.items():
    for name in KEYWORDS2:
        text = val['text'] + val['header']

        if name.lower() in text or name.capitalize() in text:
            print(val['data'], val['header'], val['url'])
            break












