'''
Adam Abbas and Holden Higgins
SoftDev2 pd7
K 05 -- Import/Export Bank
2017-02-25

Our dataset is the wikipedia movie data, containing data on over 18 thousand movies, including the year they were made, their director and of course the title.
To download this data, save it from this link: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json

We use the urllib2 library to open and read the json. After loading it in, we then loop through it, converting the entries into Mongo usable listings. We then add it to the database!
'''

import urllib2, json
from pymongo import MongoClient

conn = MongoClient('lisa.stuy.edu', 27017)
laptopBros = conn.movies

def shetup():

    #American Move JSON
    R = open("movies.json", "r")
    page = R.read()
    R.close()
    dat = json.loads(page)
    laptopBros.movies.insert(dat)
    #print "WE MADE IT"

def del_reps(movies):
    for movie in movies:
        cast=movie['cast']
        i=0
        self=False
        while i<len(movies):
            if cast==movies[i]['cast'] and self:
                #print cast
                #print "-----------------------"
                #print movies[i]['year']
                #print i
                movies.pop(i)
            elif cast==movies[i]["cast"]:
                self=True
                i+=1
            else:
                i+=1
    #print movies
    if len(movies)==0:
        movies=[{'title':"That query did not match any movies"}]
    #print movies
    return movies

def cases(string):
    string=string.lower()
    words=string.split(' ')
    new_words=''
    lowers=['a', 'an', 'the', 'at', 'by', 'for', 'in', 'of', 'on', 'to', 'up', 'and', 'as', 'but', 'or', 'nor', 'with']
    first=True
    for word in words:
        if len(word)==1:
            new_words+=word.upper()
        elif word not in lowers or first:
            new_words+=word[0].upper()+word[1:]
        else:
            new_words+=word
        new_words+=' '
        first=False
    new_words=new_words[:-1]
    return new_words

def get_title(title):
    title=cases(title)
    shetup()
    movies= list(laptopBros.movies.find({'title':title}))
    return del_reps(movies)

def get_director(director):
    director=cases(director)
    shetup()
    movies= list(laptopBros.movies.find({'director': director}))
    return del_reps(movies)

def get_year(year):
    shetup()
    movies=list(laptopBros.movies.find({'year': year}))
    return del_reps(movies)

def get_genre(gen):
    gen=cases(gen)
    shetup()
    movies= list(laptopBros.movies.find({'genre': gen}))
    return del_reps(movies)
