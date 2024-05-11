from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.youthall.com/tr/jobs/?page=1').text
soup = BeautifulSoup(html_text, 'lxml')
adverts = soup.find_all('div', class_ = 'l-grid__col l-grid__col--lg-4 l-grid__col--md-4 l-grid__col--xs-12 u-gap-bottom-25')
for advert in adverts:
    company = advert.find('small', class_ = 'u-clear-gap u-text-overflow').text
    program = advert.find('h5', class_ = 'u-text-overflow').text
    print(company, program, end="\n\n")



