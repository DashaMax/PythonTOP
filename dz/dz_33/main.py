from parse import Parser


def main():
    pages = 17

    for page in range(1, pages + 1):
        parse = Parser(f'https://www.labirint.ru/genres/2684/?page={str(page)}', 'product.txt')
        parse.run()


if __name__ == '__main__':
    main()