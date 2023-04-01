''' Реализовать парсинг данных из любого интернет ресурса с однотипными данными
и сохранить их в формате csv. '''


import csv
import re
import requests

from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    raise ConnectionError


def get_src(a: str) -> str:
    find_src = re.findall(r'data-src="(.+)" data-srcset=', a)
    find_src = find_src[0] if find_src else ''
    return find_src


def write_product(product: list):
    try:
        with open('books.csv') as file:
            pass

    except FileNotFoundError:
        with open('books.csv', 'w') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            writer.writerow(['Название', 'Автор', 'Цена', 'URL изображения'])

    with open('books.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\r')
        writer.writerow(product)


def parse_data(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    product_list = soup.find_all('article', class_='product-card')

    for product in product_list:
        title = str(product.find('div', class_='product-title__head').text).strip()
        author = str(product.find('div', class_='product-title__author').text).strip()
        price = str(product.find('div', class_='product-price__value').text).strip()
        img = get_src(str(product.find('img', class_='product-picture__img')))
        write_product([title, author, price, img])


def main():
    pages = 21   # на сайте 2192 страницы

    for i in range(1, pages):
        if i == 1:
            url = 'https://www.chitai-gorod.ru/catalog/books/hudozhestvennaya-literatura-9657'
        else:
            url = 'https://www.chitai-gorod.ru/catalog/books/hudozhestvennaya-literatura-9657?page=' + str(i)

        html = get_html(url)
        parse_data(html)


if __name__ == '__main__':
    main()







