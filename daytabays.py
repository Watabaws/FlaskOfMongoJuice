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
    print "WE MADE IT"


def get_title(title):
    shetup()
    return list(laptopBros.movies.find({'title':title}))

def get_director(dir):
    shetup()
    return list(laptopBros.movies.find({'director': dir}))

def get_year(year):
    shetup()
    return list(laptopBros.movies.find({'year': year}))


def get_genre(gen):
    shetup()
    return list(laptopBros.find({'genre': gen}))
