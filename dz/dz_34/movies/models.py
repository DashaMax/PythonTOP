import pickle
from os import path


class Movie:
    def __init__(self, title, genre, director, year, time, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.time = time
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return self.title


class MovieModel:
    def __init__(self):
        self.db = 'movies.txt'
        self.movies = self.load_data()

    def add_movie(self, movie):
        movie = Movie(*movie)
        self.movies[movie.title] = movie

    def get_movies(self):
        return self.movies

    def get_movie(self, movie):
        if movie in self.movies:
            return self.movies[movie]

    def delete_movie(self, movie):
        if movie in self.movies:
            return self.movies.pop(movie)

    def edit_movie(self, movie, data):
        self.movies[movie] = data

    def load_data(self):
        if path.exists(self.db):
            with open(self.db, 'rb') as file:
                return pickle.load(file)
        return dict()

    def save_data(self):
        with open(self.db, 'wb') as file:
            pickle.dump(self.movies, file)