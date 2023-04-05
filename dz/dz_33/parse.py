from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self, url: str, path: str):
        self.url = url
        self.path = path
        self.html = ''

    def _get_html(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            self.html = BeautifulSoup(response.text, 'html.parser')
        else:
            raise ConnectionError

    def _parsing(self):
        products = self.html.find('div', class_='genres-catalog').find_all('div', class_='genres-carousel__item')

        for product in products:
            try:
                title = product.find('a', class_='product-title-link').get('title')
            except AttributeError:
                title = '-'

            try:
                author = product.find('div', class_='product-author').find('a').get('title')
            except AttributeError:
                author = '-'

            try:
                price = product.find('span', class_='price-val').text.strip()
            except AttributeError:
                price = '-'

            data = f'{"*" * 30}\nКнига: {title}\nАвтор: {author}\nЦена: {price}\n\n'
            self._write_to_file(data)

    def _write_to_file(self, data: str):
        with open(self.path, 'a') as file:
            file.write(data)

    def run(self):
        self._get_html()
        self._parsing()