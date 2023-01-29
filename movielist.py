from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

from random import randint

from config import *



class MovieList:
    def __init__(self) -> None:
        self.plexAccount = MyPlexAccount(config[PLEX][USER], config[PLEX][PASS])
        self.plex = self.plexAccount.resource(config[PLEX][SERVERNAME]).connect()  # returns a PlexServer instance
        self.moviesList = self.plexAccount.watchlist(filter='available',libtype='movie',sort='titleSort:asc')
    def selectMovie(self):        
        movieListSize = len(self.moviesList)
        movieIdSelected = randint(0,movieListSize)
        self.movieSelected = self.moviesList[movieIdSelected]
        print(vars(self.movieSelected))
    
    def identifySelectedMovie(self):
        if self.movieSelected == None:
            self.selectMovie()
        result = self.plex.library.search(guid=self.movieSelected.guid,libtype=self.movieSelected.type)
        self.isSelectedMovieOnLib = len(result) > 0
        print(result)
        print(self.isSelectedMovieOnLib)

        
        



       
    
