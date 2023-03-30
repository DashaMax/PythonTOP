''' Есть некоторый словарь, который хранит название стран и столиц.
 Название стран используется в качестве ключа, название столицы в качестве значения.
 Необходимо реализовать:
 добавление, удаление, поиск, редактирование и просмотр данных (используя упаковку и распаковку данных) '''


from json import dump, load


def dump_data(data: dict):
    with open('dz_31/countries.json', 'w') as file:
        dump(data, file, ensure_ascii=False)


active = None

while active != '6':
    print('\n' + '*' * 30)

    with open('dz_31/text.txt') as file:
        active = input(file.read())

    try:
        with open('dz_31/countries.json') as file:
            countries = load(file)

    except FileNotFoundError:
        countries = {}

    if active == '1':
        country = input('Введите название страны (с заглавной буквы): ')
        capital = input('Введите название столицы (с заглавной буквы): ')
        countries[country] = capital
        dump_data(countries)
        print('Файл сохранён')

    elif active == '2':
        country = input('Введите название страны (с заглавной буквы), данные которой хотите удалить: ')

        if country not in countries:
            print(f'Страна {country} не найдена')

        else:
            del countries[country]
            dump_data(countries)
            print(f'Страна {country} успешно удалена')

    elif active == '3':
        country = input('Введите название страны (с заглавной буквы), данные которой хотите найти: ')

        if country not in countries:
            print(f'Страна {country} не найдена')

        else:
            print(f'Страна {country} найдена')

    elif active == '4':
        country = input('Введите название страны (с заглавной буквы), данные которой хотите отредактировать: ')
        capital = input('Введите новое название столицы (с заглавной буквы): ')

        if country not in countries:
            print(f'Страна {country} не найдена!')

        else:
            countries[country] = capital
            dump_data(countries)
            print('Данные успешно отредактированы!')

    elif active == '5':
        print(countries)

    else:
        print('Выберите корректное действие!')



