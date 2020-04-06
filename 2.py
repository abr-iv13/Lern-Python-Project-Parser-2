import requests
from bs4 import BeautifulSoup
import csv


def refined(s):
    r = s.split(' ')[0]
    return r.replace(',', '')

def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'], data['url'], data['rating']))
 
def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')

        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(r)
        print(rating)

        data = {"name" : name,
                'url': url,
                'rating': rating }
        write_csv(data)

    # return plugins

def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__=='__main__':
    main()