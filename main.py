from bs4 import BeautifulSoup
import requests

page = 1
while True:
    url = f'https://www.youthall.com/tr/jobs/?page={page}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    adverts = soup.find_all('div', class_='l-grid__col'
                                          ' l-grid__col--lg-4 l-grid__col--md-4 '
                                          'l-grid__col--xs-12 u-gap-bottom-25')
    if not adverts:
        break

    for advert in adverts:
        company = advert.find('small', class_='u-clear-gap u-text-overflow').text
        program = advert.find('h5', class_='u-text-overflow').text
        lower_program = advert.find('h5', class_='u-text-overflow').text.lower()
        if 'python' in lower_program or 'data' in lower_program:
            print(f'''
            Company Name: {company}
            Program: {program}
            ''')
    page += 1
