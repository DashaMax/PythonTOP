from views import UserInterface
from models import MovieModel


class Controller:
    def __init__(self):
        self.user_interface = UserInterface()
        self.movie_model = MovieModel()

    def run(self):
        action = None

        while action != 'q':
            action = self.user_interface.wait_answer()
            self.check_answer(action)

    def check_answer(self, action):
        if action == '1':
            movie = self.user_interface.add_movie()
            self.movie_model.add_movie(movie)

        elif action == '2':
            catalog = self.movie_model.get_movies()
            self.check_movie(catalog, self.user_interface.get_catalog, 'catalog')

        elif action == '3':
            movie = self.user_interface.get_movie('посмотреть')
            movie_data = self.movie_model.get_movie(movie)
            self.check_movie(movie_data, self.user_interface.movie_data, 'movie not found')

        elif action == '4':
            movie = self.user_interface.get_movie('удалить')
            movie_delete = self.movie_model.delete_movie(movie)
            self.check_movie(movie_delete, self.user_interface.delete_movie, 'movie not found')

        elif action == '5':
            movie = self.user_interface.get_movie('отредактировать')
            check = self.movie_model.get_movie(movie)

            if check:
                data = self.user_interface.edit_movie()
                self.movie_model.edit_movie(movie, data)
            else:
                self.user_interface.get_message('movie not found')

        elif action == 'q':
            self.movie_model.save_data()

        else:
            self.user_interface.error_action()

    def check_movie(self, movie, func, text):
        if movie:
            func(movie)
        else:
            self.user_interface.get_message(text)
