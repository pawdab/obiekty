# niestety mam totalnie urwanie głowy w pracy więc mogę zrobić zadania tylko po łebkach i wersja minimum

import random

from datetime import date
from faker import Faker
fake = Faker()

class Movie:
    def __init__(self, title, release_year, genre):
       self.title = title
       self.release_year = release_year
       self.genre = genre
       

        #Variables
       self.play_times = 0

    def __str__(self):
        return f'{self.title} ({self.release_year}) odtworzono: {self.play_times}'

    def play(self):
        self.play_times += 1

class TvSeries(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season} E{self.episode} odtworzono: {self.play_times}'

def genre_generator():
    new_genre = random.randint(1,3)
    if new_genre == 1:
        return "Comedy"
    elif new_genre == 2:
        return "Horror"
    else:
        return "Thriller"

def add_TV(x):
    for i in range (1,x + 1):
        new_TV_title = fake.text()[0:random.randint(5,15)]
        new_TV_year = random.randint(1960,2020)
        new_TV_genre = genre_generator()
        new_season = "0" + str(random.randint(1,5))
        new_episode = str(random.randint(1,15))
        if len(new_episode) == 1:
            new_episode = "0" + new_episode
        new_TV_series = TvSeries(season = new_season, episode= new_episode,title = new_TV_title, release_year = new_TV_year, genre = new_TV_genre)
        list.append(new_TV_series)
        i = i + 1

def add_Movie(x):
    for i in range (1,x + 1):
        new_movie_title = fake.text()[0:random.randint(5,15)]
        new_movie_year = random.randint(1960,2020)
        new_movie_genre = genre_generator()
        new_season = "0" + str(random.randint(1,5))
        new_movie = Movie(title = new_movie_title, release_year = new_movie_year, genre = new_movie_genre)
        list.append(new_movie)
        i = i + 1

def get_movies(list):
    movie_list = []
    for items in list:
        if type(items) == Movie:
            movie_list.append(items)
    movie_list = sorted(movie_list, key=lambda movie: movie.title)
    return movie_list

def get_TV_series(list):
    tv_list = []
    for items in list:
        if type(items) == TvSeries:
            tv_list.append(items)
    tv_list = sorted(tv_list, key=lambda tv: tv.title)
    return tv_list

def search(title):
    for item in list:
        if item.title == title:
            print("Znalazłem")
            print (item)


# wiem, że ofektywniej było by movie_tv.play_times = random.... ale skoro mam play to się nim bawie
def generate_views(list):
    movie_tv = list[random.randint(0,len(list)-1)]
    for i in range (1, random.randint(1,100)):
        if random.randint(0,1) == 1:
            movie_tv.play()
        #print(movie_tv)
        i = i + 1

def generate_views_run():
        for i in range(1,100):
            generate_views(list)
            i = i + 1

def top_titles(x):
    top_titles = sorted(list, key=lambda movie: movie.play_times, reverse=True)
    top_titles = top_titles[0:x]
    return top_titles

list = []

add_TV(100)
add_Movie(300)
generate_views_run()

#for movies in list:
#    print(movies)
#    print(movies.play_times)
#    for i in range (1,10):
#        if random.randint(1,2) == 1:
#            movies.play()
#        i = i + 1

#for movies in list:
#    print(movies)
#    print(movies.play_times)


movies_only = get_movies(list)
tv_only = get_TV_series(list)

print("all:")
for item in list:
    print(item)

print("filmy:")
for item in movies_only:
    print(item)

print("seriale:")
for item in tv_only:
    print(item)


search(list[2].title)

top_titles_list = top_titles(3)

today = date.today()
date = today.strftime("%d.%m.%Y")

print("top lista na dziś (" + str(date) + ")")
for item in top_titles_list:
    print(item)

