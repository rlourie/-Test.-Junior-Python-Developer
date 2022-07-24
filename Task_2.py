import requests
from bs4 import BeautifulSoup


def get_viki(url):
    response = requests.get(url).text
    return response


result = {}
counter = 0
first = ''
alfa = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФЧЦЧШЪЫЬЭЮЯ'
next = 'https://inlnk.ru/jElywR'
while first != 'A':
    html_doc = get_viki(next)
    soup = BeautifulSoup(html_doc, 'html.parser')
    buf = soup.find_all('div', {"class": "mw-category mw-category-columns"})
    soup2 = BeautifulSoup(str(buf), 'html.parser')
    for tag in soup2.find_all('li'):
        first = tag.text[0]
        if first in alfa:
            if result.get(first) is None:
                result[first] = 1
            else:
                result[first] = result.get(first) + 1
                counter += 1
        if counter == 200:
            counter = 0
            next = 'https://ru.wikipedia.org' + \
                   soup.find_all('a', {"title": "Категория:Животные по алфавиту"})[1].attrs['href']
for i in alfa:
    if result.get(i) is None:
        print(f'{i}: None')
    else:
        print(f'{i}:{result[i]}')
