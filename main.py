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

base_url = 'https://habr.com'
url = '/ru/all/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
resp = requests.get(base_url + url, headers=HEADERS)
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text,features='html.parser')
articles = soup.find('div', class_='tm-articles-list').find_all('article')

d = {}
for article in articles:
    id = article.get('id')
    href = article.find('h2').find('a').get('href')
    header = article.find('h2').find('a').find('span').text
    data = article.find('time').get('title')
    prevs = article.find_all('p')
    prevs_1 = ''.join([prev.text for prev in prevs])
    prevs_2 = article.find('div', class_='tm-article-body tm-article-snippet__lead').text


    d[id] = {'url':base_url + href,
             'header':header,
             'data':data,
             'preview':prevs_1 + prevs_2
             }
#pprint(d)

for key,val in d.items():
    for name in KEYWORDS3:
        text = val['preview'] + val['header']

        if name.lower() in text or name.capitalize() in text:
            print(val['data'], val['header'], val['url'])
            break















