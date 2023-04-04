''' Реализовать парсинг данных из любого интернет ресурса с однотипными данными
и сохранить их в формате csv. '''


import csv
import requests

from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text

    raise ConnectionError('Ошибка подключения')


def write_product(product: list):
    try:
        with open('book.csv') as file:
            pass

    except FileNotFoundError:
        with open('book.csv', 'w') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            writer.writerow(['Название', 'Автор', 'Цена', 'URL изображения'])

    with open('book.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\r')
        writer.writerow(product)


def get_product(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    product_list = soup.find_all('article', class_='product-card')
    return product_list


def main():
    pages = 20   # на сайте 2192 страницы

    for page in range(1, pages + 1):
        url = 'https://www.chitai-gorod.ru/catalog/books/hudozhestvennaya-literatura-9657?page=' + str(page)
        html = get_html(url)
        books = get_product(html)

        for book in books:
            title = book.find('div', class_='product-title__head').text.strip()
            author = book.find('div', class_='product-title__author').text.strip()
            price = book.find('div', class_='product-price__value').text.strip()
            img = book.find('img', class_='product-picture__img').get('data-src')
            write_product([title, author, price, img])


if __name__ == '__main__':
    main()







