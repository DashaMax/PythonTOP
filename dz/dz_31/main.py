''' Есть некоторый словарь, который хранит название стран и столиц.
 Название стран используется в качестве ключа, название столицы в качестве значения. Необходимо реализовать:
 добавление, удаление, поиск, редактирование и просмотр данных (используя упаковку и распаковку данных). '''


from json import dump, load


def dump_data(data: dict):
    with open('countries.json', 'w') as f:
        dump(data, f, ensure_ascii=False)


def get_country(text: str, d: dict):
    ctr = input(f'Введите название страны, данные которой хотите {text}: ').capitalize()

    if ctr not in d:
        print(f'Страна {ctr} не найдена')
    else:
        return ctr


active = None

while active != '6':
    print('\n' + '*' * 30)

    with open('text.txt') as file:
        active = input(file.read())

    try:
        with open('countries.json') as file:
            countries = load(file)

    except FileNotFoundError:
        countries = {}

    if active == '1':
        country = input('Введите название страны: ').capitalize()
        capital = input('Введите название столицы: ').capitalize()
        countries[country] = capital
        dump_data(countries)
        print('Файл сохранён')

    elif active == '2':
        country = get_country('удалить', countries)

        if country:
            del countries[country]
            dump_data(countries)
            print(f'Страна {country} успешно удалена')

    elif active == '3':
        country = get_country('найти', countries)

        if country:
            print(f'Страна - {country}, столица - {countries[country]}')

    elif active == '4':
        country = get_country('отредактировать', countries)

        if country:
            capital = input('Введите новое название столицы: ').capitalize()
            countries[country] = capital
            dump_data(countries)
            print('Данные успешно отредактированы')

    elif active == '5':
        print(countries)

    else:
        print('Выберите корректное действие!')



