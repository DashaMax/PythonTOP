def decoration(text: str):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f' {text} '.center(50, '='))
            data = func(*args, **kwargs)
            print('=' * 50 + '\n')
            return data
        return wrap
    return wrapper


class UserInterface:
    @decoration('Пользовательский ввод')
    def wait_answer(self):
        print('1 - добавление фильма\n'
              '2 - каталог фильмов\n'
              '3 - просмотр определенного фильма\n'
              '4 - удаление фильма\n'
              '5 - редактирование фильма\n'
              'q - выход из программы')
        answer = input('Выберите вариант действия: ')
        return answer

    @decoration('Добавление нового фильма')
    def add_movie(self):
        movie = [
            input('Название фильма: '),
            input('Жанр: '),
            input('Режиссер: '),
            input('Год выпуска: '),
            input('Длительность: '),
            input('Студия: '),
            input('Актеры (перечислите актерский состав через пробел): ').split()
        ]
        return movie

    @decoration('Редактирование фильма')
    def edit_movie(self):
        movie = [
            input('Жанр: '),
            input('Режиссер: '),
            input('Год выпуска: '),
            input('Длительность: '),
            input('Студия: '),
            input('Актеры (перечислите актерский состав через пробел): ').split()
        ]
        return movie

    @decoration('Каталог фильмов')
    def get_catalog(self, catalog):
        for index, movie in enumerate(catalog, start=1):
            print(f'{index}. {movie}')

    @decoration('Название фильма')
    def get_movie(self, text):
        movie = input(f'Введите название фильма, данные которого хотите {text}: ')
        return movie

    @decoration('Данные фильма')
    def movie_data(self, movie):
        print(f'Название фильма: {movie.title}')
        print(f'Жанр: {movie.genre}')
        print(f'Режиссер: {movie.director}')
        print(f'Год выпуска: {movie.year}')
        print(f'Длительность: {movie.time}')
        print(f'Студия: {movie.studio}')
        print(f'Актеры: {", ".join(movie.actors)}')

    @decoration('Сообщение')
    def get_message(self, text):
        message = {
            'catalog': 'Ваш каталог пуст',
            'movie not found': 'Фильм не найден'
        }
        print(message[text])

    @decoration('Удаление фильма')
    def delete_movie(self, movie):
        print(f'Фильм {movie} успешно удален')

    @decoration('Ошибка ввода')
    def error_action(self):
        print('Выберите верное действие')