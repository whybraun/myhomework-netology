import requests
import bs4
import fake_headers
import time
from pprint import pprint
import json

headers_gen = fake_headers.Headers(browser='firefox', os='win')
response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers_gen.generate())
main_html = response.text
main_soup = bs4.BeautifulSoup(main_html, 'lxml')

parsed_data = []
keywords = ['Django', 'Flask']

main_article_list_tag = main_soup.find('main', class_='vacancy-serp-content')

article_tags = main_article_list_tag.find_all(class_="vacancy-serp-item__layout")

for article in article_tags:
    vacancy_name = article.find('a', class_='serp-item__title')
    link = vacancy_name['href']

    response_article_full = requests.get(link, headers=headers_gen.generate())

    if response_article_full.status_code != 200:
        continue
    time.sleep(0.1)
    response_article_full_html = response_article_full.text
    article_full_soup = bs4.BeautifulSoup(response_article_full_html, features='lxml')
    article_full_tag = article_full_soup.find('div', class_='vacancy-branded-user-content')

    if article_full_tag is None:
        continue

    salary = article_full_soup.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite')
    article_full_text = article_full_tag.text

    city = article.find('div', class_="bloko-text", attrs={'data-qa': 'vacancy-serp__vacancy-address'})
    
    parsed_data.append({
        'Ссылка': link,
        'Вилка ЗП': salary.text.replace('\xa0', ' ') if salary else 'Отсутствует',
        'Компания': name_company.text if (name_company := article.find('a', class_='bloko-link bloko-link_kind-tertiary')) else 'Не указана',
        'Город': city.text.strip() if city else 'Не указан'
    })


with open('vacancies.json', 'w', encoding='utf-8') as json_file:
    json.dump(parsed_data, json_file, ensure_ascii=False, indent=4)