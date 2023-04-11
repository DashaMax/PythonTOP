class MovieModel:
    def __init__(self, title: str, genre: str, director: str, year: int, time: int, studio: str, actors: list):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.time = time
        self.studio = studio
        self.actors = actors