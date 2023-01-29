from config import *
from pymongo import MongoClient
from random  import randint

class DrawVideo():
    def __init__(self) -> None:
        self.client             = MongoClient(config[MONGO_URL])
        self.db                 = self.client["watchlist"]
        self.collectionMovies   = self.db["movies"]
        self.collectionShows    = self.db['shows']

    def countMovies(self):
        return self.collectionMovies.count_documents({})

    def countShows(self):
        return self.collectionShows.count_documents({})

    def drawMovie(self):
        pos =  randint(0,self.countMovies()-1)
        return self.collectionMovies.find()[pos]['guid']
    
    def drawShow(self):
        pos = randint(0,self.countShows()-1)
        return self.collectionShows.find()[pos]['guid']
    

if __name__ == '__main__':
    d = DrawVideo()
    print(d.drawMovie())