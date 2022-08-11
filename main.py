import bs4
import requests

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.5005.148 YaBrowser/22.7.2.899 Yowser/2.5 Safari/537.36'}

MY_TAGS = {'IT-системы', 'фото', 'web', 'python'}
response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)
    print(hubs)

    date = article.find('time').text
    title = article.find('a', class_='tm-article-snippet__title-link')
    span_title = title.find('span').text
    print(span_title)

    if MY_TAGS & hubs:
        href = title['href']
        url = 'https://habr.com' + href
        print(f'Дата: {date} - Заголовок: {span_title} - Ссылка: {url}')
