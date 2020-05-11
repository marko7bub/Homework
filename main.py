import urllib.request
import json
import random

m1 = input("Enter your first favorite movie: ")
m2 = input("Enter your second favorite movie: ")
m3 = input("Enter your third favorite movie: ")


class MovieRecomendation:
    ''' Class for recommending movies '''

    def __init__(self, movie_list):
        '''
        (lst) -> None
        '''
        self.movies = movie_list

    def give_recommendations(self):
        '''
        Give three movie recommendations
        '''
        BASE_URL1 = "http://omdbapi.com/?t={}&apikey=52c58877".format(
            '+'.join(self.movies[0].split()))
        f1 = urllib.request.urlopen(BASE_URL1)
        data1 = json.loads(f1.read())
        BASE_URL2 = "http://omdbapi.com/?t={}&apikey=52c58877".format(
            '+'.join(self.movies[1].split()))
        f2 = urllib.request.urlopen(BASE_URL2)
        data2 = json.loads(f2.read())
        BASE_URL3 = "http://omdbapi.com/?t={}&apikey=52c58877".format(
            '+'.join(self.movies[2].split()))
        f3 = urllib.request.urlopen(BASE_URL3)
        data3 = json.loads(f3.read())
        genres = set()
        genres.update(data1['Genre'].split(','))
        genres.update(data2['Genre'].split(','))
        genres.update(data3['Genre'].split(','))
        years = sorted([int(data1['Year']), int(
            data2['Year']), int(data3['Year'])])
        movies_list = []
        with open('newdata.txt', encoding="utf8", errors='ignore') as f:
            lines = f.readlines()
        for movie in lines:
            try:
                if (years[0] - 10) <= int(movie.split('\t')
                                          [5].strip()) <= (years[-1] + 10):
                    if all(elem in list(genres)
                           for elem in movie.split('\t')[-1].strip().split(',')):
                        movies_list.append(movie.split('\t')[2])
            except ValueError:
                continue
        three_movies = []
        for i in range(3):
            three_movies.append(random.choice(movies_list))
        print("We think you'd like:")
        for i in three_movies:
            BASE_URL = "http://omdbapi.com/?t={}&apikey=52c58877".format(
                '+'.join(i.split()))
            f = urllib.request.urlopen(BASE_URL)
            data = json.loads(f.read())
            print("Movie: " + data['Title'])
            print("Genre: " + data['Genre'])
            print("Year: " + data['Year'])
            print("Plot: " + data['Plot'])
            print('\n')
        return "Be sure to check theses movies out!"


a = MovieRecomendation([m1, m2, m3])
print(a.give_recommendations())
