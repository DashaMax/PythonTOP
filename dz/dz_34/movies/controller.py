from views import UserInterface
from models import MovieModel


class Conroller:
    def __init__(self):
        self.user_interface = UserInterface()
        self.movie_model = MovieModel()

    def run(self):
        action = None

        while action != 'q':
            action = self.user_interface.wait_user_answer()


    def check_user_answer(self, action: str):
        pass
