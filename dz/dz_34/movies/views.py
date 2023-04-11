class UserInterface:
    def wait_user_answer(self):
        print('Действия с фильмами')
        print('1 - добавление фильма\n'
              '2 - каталог фильмов\n'
              '3 - просмотр определенного фильма\n'
              '4 - удаление фильма\n'
              'q - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer